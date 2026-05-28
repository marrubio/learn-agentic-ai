from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

# -----------------------------
# Step 1: Model
# -----------------------------
model = ChatOllama(model="llama3")

# -----------------------------
# Step 2: Prompts
# -----------------------------
definition_prompt = ChatPromptTemplate.from_template(
  "Define {topic} in simple terms"
)

advantages_prompt = ChatPromptTemplate.from_template(
  "List advantages of {topic}"
)

final_prompt = ChatPromptTemplate.from_template(
  "Combine the following into a clean explanation:\n\nDefinition:\n{definition}\n\nAdvantages:\n{advantages}"
)

# -----------------------------
# Step 3: Parser
# -----------------------------
parser = StrOutputParser()

# -----------------------------
# Step 4: Custom Logic (pre-processing)
# -----------------------------
def add_context(input_data):
# modify input before sending to LLM
  input_data["topic"] = input_data["topic"] + " in cloud computing"
  return input_data

preprocess = RunnableLambda(add_context)

# -----------------------------
# Step 5: Parallel Execution
# -----------------------------
parallel_chain = RunnableParallel(
  definition=definition_prompt | model | parser,
  advantages=advantages_prompt | model | parser
)

# -----------------------------
# Step 6: Final Chain
# -----------------------------
chain = (
  preprocess
  | parallel_chain
  | final_prompt
  | model
  | parser
)

# -----------------------------
# Step 7: Streaming Output
# -----------------------------
print("Streaming output:\n")

for chunk in chain.stream({"topic": "Docker"}):
  print(chunk, end="", flush=True)