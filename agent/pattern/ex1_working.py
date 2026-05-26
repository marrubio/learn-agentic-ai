from langchain_community.llms import Ollama
import re


llm = Ollama(model="llama3")


# -- Tools --
def get_weather(city):
    return "30" # mock temperature in celsius

def calculator(expr):
    return str(eval(expr)) # mock calculator, be careful with eval in production code

TOOLS = {
    "get_weather": get_weather,
    "calculator": calculator
}

# --- ReAct Prompt Template --
SYSTEM_PROMPT = """
You are a ReAct AI agent.

Available tools:
- get_weather(city): returns the current temperature in celsius for the given city.
- calculator(expr): evaluates a mathematical expression and returns the result.

Follow this format strictly:

Question: ...
Thought: ...
Action: tool_name
Action Input: ...
Observation: ...

Repeat until done.

Final Answer: ...
"""

# --- Agent Loop ---
def run_react(question, max_steps=5):
    context = SYSTEM_PROMPT + f"\nQuestion: {question}\n"
 
    for step in range(max_steps):
        output = llm.invoke(context)
        print("\nLLM Output:\n", output)
 
        # --- Extract Action ---
        #Your code extracts action
        #Extracts:
 
        #action = "get_weather"
        #input = "Delhi"
        action_match = re.search(r"Action:\s*(\w+)", output)
        input_match = re.search(r"Action Input:\s*(.*)", output)
 
        if not action_match:
            return output  # Final Answer case
        #action = "get_weather"
        #action_input = "Delhi"
        action = action_match.group(1)
        action_input = input_match.group(1).strip()
 
        # --- Execute Tool ---
        if action in TOOLS:
            result = TOOLS[action](action_input)
        else:
            result = "Unknown tool"
 
        # --- Add Observation ---
        context += f"""
{output}
Observation: {result}
"""
 
        # --- Stop if final answer ---
        if "Final Answer:" in output:
            return output
 
    return "Max steps reached"
   
 
# --- Run ---
print(run_react("Find temperature in Delhi and convert to Fahrenheit"))
