from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch

# -------------------
# 1. LLM
# -------------------
llm = ChatOllama(model="llama3", temperature=0)

# -------------------
# 2. Router function (simple + reliable)
# -------------------
def route(input_dict):
  text = input_dict["input"].lower()
  if any(op in text for op in ["+", "-", "*", "/", "calculate", "solve"]):
    return "math"
  elif "summarize" in text:
    return "summary"
  else:
    return "general"

# -------------------
# 3. Chains
# -------------------
math_chain = ChatPromptTemplate.from_template(
  "Solve step by step:\n{input}"
) | llm

summary_chain = ChatPromptTemplate.from_template(
  "Summarize clearly:\n{input}"
) | llm

general_chain = ChatPromptTemplate.from_template(
  "Answer clearly:\n{input}"
) | llm


# -------------------
# 4. Proper Router (FIXED)
# -------------------
chain = RunnableBranch(
  (lambda x: route(x) == "math", math_chain),
  (lambda x: route(x) == "summary", summary_chain),
  general_chain
)

# -------------------
# 5. TEST
# -------------------
print(chain.invoke({"input": "What is 25 * 18 + 10?"}))
print(chain.invoke({"input": "Summarize LangChain in simple terms"}))
print(chain.invoke({"input": "What is AI?"}))