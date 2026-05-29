from langchain_ollama import OllamaLLM
import re

llm = OllamaLLM(model="llama3")

# -- Tools --
def get_temperature(city):
    print("\nget_temperature:", city)
    return "24" # mock temperature in celsius

def calculator(expr):
    print("\ncalculator:", expr)
    return str(eval(expr)) # mock calculator, be careful with eval in production code

TOOLS = {
    "get_temperature": get_temperature,
    "calculator": calculator
}

# --- ReAct Prompt Template --
SYSTEM_PROMPT = """
You are a AI agent.

Available tools:
- get_temperature(city): returns the current temperature in celsius for the given city.
- calculator(expr): evaluates a mathematical expression and returns the result.

Follow this format strictly:

Question: ...
Thought: ...
Action: tool_name
Action Input: ...

Important rules:
- Return exactly one action per turn.
- Never invent or write Observation values.
- Observation is added only by the runtime after tool execution.
- Do not repeat the same tool call with the same input if an Observation already exists.
- As soon as you have enough information, return Final Answer.

Repeat until done.

Final Answer: ...
"""

# --- Agent Loop ---
def run_react(question, max_steps=5):
    context = SYSTEM_PROMPT + f"\nQuestion: {question}\n"
    tool_cache = {}
 
    for step in range(max_steps):

        print("\n ***** STEP ", step, " *****\n")
        output = llm.invoke(context)
        print("\nLLM Raw Output:\n", output)
 
        action_match = re.search(r"(?mi)^Action:\s*([a-zA-Z_]\w*)", output)
        input_match = re.search(r"(?mi)^Action Input:\s*(.+)\s*$", output)
        final_match = re.search(r"(?mi)^Final Answer:\s*(.*)$", output)
        fallback_final_match = re.search(r"(?is)final answer\s*(?:is|:)\s*(.+)", output)
 
        if final_match and not action_match:
            return final_match.group(1).strip()

        if fallback_final_match and not action_match:
            return fallback_final_match.group(1).strip()

        if not action_match or not input_match:
            return f"Parse error. Model output was:\n{output}"

        #action = "get_temperature"
        #action_input = "Valencia"
        action = action_match.group(1)
        action_input = input_match.group(1).strip()
        print(f"\nParsed Action: {action}")
        print(f"Parsed Action Input: {action_input}")

        if action.lower() == "none":
            if final_match:
                return final_match.group(1).strip()
            if fallback_final_match:
                return fallback_final_match.group(1).strip()
            return output

        call_key = (action, action_input)
 
        # --- Execute Tool ---
        if call_key in tool_cache:
            print("\nTool call repeated, using cached observation")
            result = tool_cache[call_key]
        elif action in TOOLS:
            result = TOOLS[action](action_input)
            tool_cache[call_key] = result
        else:
            result = "Unknown tool"
 
        # --- Add Observation ---
        context += f"""
    Action: {action}
    Action Input: {action_input}
Observation: {result}
"""
 
    return "Max steps reached"
   
 
# --- Run ---
print(run_react("Find temperature in Madrid and convert to Fahrenheit"))
