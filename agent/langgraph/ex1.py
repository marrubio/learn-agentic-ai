from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
#from langchain_community.chat_models import ChatOllama
#from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama

#2 Initialize LLM (Ollama)
llm = ChatOllama(model="llama3")

#3 Define Tools
def calculator_tool(input_text: str) -> str:
  print("Inside calculator")
  try:
    return str(eval(input_text))
  except:
    return "Error in calculation"
#4 Define Agent State
from typing import TypedDict

class AgentState(TypedDict, total=False):
  input: str
  decision: str
  result: str 
  output: str

#5 Node 1: Reasoning (Decision Making)

def think(state):
  user_input = state.get("input")
  print("user put, inside think",user_input)
  if not user_input:
     raise ValueError("Missing input")
  response = llm.invoke(user_input)
  state["decision"] = response.content
  return state


#6. Node 2: Tool Execution
def act(state):
  print("act111",state)
  decision = state["decision"]
  print("act222",decision)
  if "TOOL:" in decision:
    expression = decision.split("TOOL:")[1].strip()
    print("act expression",expression)
    result = calculator_tool(expression)
    print("act result",result)
    print("act1222",result)
    state["result"] = result
  #print("inside act,state",state["result"])
  return state

#7. Node 3: Final Answer

def respond(state):
  print("respond 111",state)
  if "result" in state:
    state["output"] = f"Tool Result: {state['result']}"
  else:
    state["output"] = state["decision"]
  return state

#8. Build LangGraph Workflow

graph = StateGraph(AgentState)
graph.add_node("think", think)
graph.add_node("act", act)
graph.add_node("respond", respond)
graph.set_entry_point("think")
graph.add_edge("think", "act")
graph.add_edge("act", "respond")
graph.add_edge("respond", END)
app = graph.compile()

#9. Run the Agent
result = app.invoke({"input": "What is 25 * 4 + 10?"})
print(result["output"])