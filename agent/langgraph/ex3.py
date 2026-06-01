#1. Looping Agent with Retry (Error Handling)


from typing import TypedDict
from langgraph.graph import StateGraph, END
import random

class State(TypedDict):
  count: int
  result: str


def call_api(state: State):
  print("Calling API...")

  # simulate failure randomly
  if random.random() < 0.6:
    print("❌ Failed")
    return {**state, "count": state["count"] + 1, "result": "fail"}
  else:
    print("✅ Success")
    return {**state, "result": "data fetched"}


def check(state: State):
  if state["result"] == "data fetched":
    return "end"
  elif state["count"] >= 3:
    return "end"
  else:
    return "retry"


graph = StateGraph(State)

graph.add_node("api", call_api)

graph.set_entry_point("api")

graph.add_conditional_edges("api", check, {
  "retry": "api",
  "end": END
})

app = graph.compile()

print(app.invoke({"count": 3, "result": ""}))