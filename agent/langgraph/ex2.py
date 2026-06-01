# ================================
# LangGraph ReAct Agent (Full Code)
# ================================


from typing import TypedDict, List
from langgraph.graph import StateGraph, END
import ollama
import re


# -------------------------------
# 1. Define State
# -------------------------------
class AgentState(TypedDict):
  input: str
  messages: List[str]
  result: str



# -------------------------------
# 2. Tools
# -------------------------------
def get_weather(city: str):
  print(f"[TOOL] get_weather({city})")
  return "30" # mock temperature



def calculator(expr: str):
  print(f"[TOOL] calculator({expr})")
  try:
    return str(eval(expr))
  except Exception as e:
    return f"error: {e}"


TOOLS = {
  "weather": get_weather,
  "calculator": calculator
}



# -------------------------------
# 3. LLM Call (Ollama)
# -------------------------------
def call_llm(prompt: str):
  response = ollama.chat(
   model="llama3", # make sure you ran: ollama run llama3
   messages=[{"role": "user", "content": prompt}]
  )
  return response["message"]["content"]

# -------------------------------
# 4. Nodes
# -------------------------------

# THINK NODE
def think(state: AgentState):
  print("\n[THINK]")

  history = "\n".join(state["messages"])

  prompt = f"""
You are a smart AI agent.

User Question:
{state['input']}

Conversation so far:
{history}

Decide next step STRICTLY in one of these formats:

1. To call tool:
 ACTION: weather Delhi
 ACTION: calculator 30+10

2. If final answer:
 FINAL: your answer

Rules:
- Do NOT explain
- ONLY output ACTION or FINAL
- Stop after 5 retries

"""
  response = call_llm(prompt)
  print("[LLM]:", response)
  state["messages"].append(response)
  return state





# ACT NODE

def act(state: AgentState):
  print("\n[ACT]")

  last_message = state["messages"][-1]

  action_match = re.search(r"ACTION:\s*(\w+)\s*(.*)", last_message)

  if not action_match:
    print("No valid action found.")
    return state

  tool_name = action_match.group(1)
  tool_input = action_match.group(2).strip()

  if tool_name not in TOOLS:
    observation = f"Unknown tool: {tool_name}"
  else:
    observation = TOOLS[tool_name](tool_input)

  obs_text = f"OBSERVATION: {observation}"
  print(obs_text)

  state["messages"].append(obs_text)
  return state


# FINISH NODE
def finish(state: AgentState):
  print("\n[FINISH]")

  last_message = state["messages"][-1]

  if "FINAL:" in last_message:
   state["result"] = last_message.replace("FINAL:", "").strip()

  return state


# -------------------------------
# 5. Routing Logic
# -------------------------------
def router(state: AgentState):
  last_message = state["messages"][-1]

  if "FINAL:" in last_message:
    return "finish"
  elif "ACTION:" in last_message:
    return "act"
  else:
    return "think"


# -------------------------------
# 6. Build Graph
# -------------------------------
def build_graph():
  graph = StateGraph(AgentState)

  graph.add_node("think", think)
  graph.add_node("act", act)
  graph.add_node("finish", finish)

  graph.set_entry_point("think")

  graph.add_conditional_edges("think", router)
  graph.add_conditional_edges("act", router)

  graph.add_edge("finish", END)

  return graph.compile()


# -------------------------------
# 7. Run
# -------------------------------
if __name__ == "__main__":
  app = build_graph()

  user_input = "What is the weather in Delhi and add 10 to it?"

  result = app.invoke({
    "input": user_input,
    "messages": [],
    "result": ""
  })

  print("\n====================")
  print("FINAL RESULT:", result["result"])
  print("====================")