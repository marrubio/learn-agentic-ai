#Multi-Step Pipeline (Like LangChain but Better


from typing import TypedDict
from langgraph.graph import StateGraph, END
import ollama


class State(TypedDict):
  topic: str
  explanation: str
  summary: str
  translation: str



def llm(prompt):
  return ollama.chat(
   model="llama3",
   messages=[{"role": "user", "content": prompt}]
  )["message"]["content"]


def explain(state: State):
  print("Explain step")
  text = llm(f"Explain {state['topic']} in detail")
  return {**state, "explanation": text}


def summarize(state: State):
  print("Summarize step")
  text = llm(f"Summarize:\n{state['explanation']}")
  return {**state, "summary": text}


def translate(state: State):
  print("Translate step")
  text = llm(f"Translate to Hindi:\n{state['summary']}")
  return {**state, "translation": text}


graph = StateGraph(State)


graph.add_node("explain", explain)
graph.add_node("summarize", summarize)
graph.add_node("translate", translate)

graph.set_entry_point("explain")

graph.add_edge("explain", "summarize")
graph.add_edge("summarize", "translate")
graph.add_edge("translate", END)

app = graph.compile()

result = app.invoke({"topic": "Artificial Intelligence"})
print(result["translation"])