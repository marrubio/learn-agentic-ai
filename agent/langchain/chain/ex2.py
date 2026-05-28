from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# Prompts
explain_prompt = ChatPromptTemplate.from_template(
 "Explain {topic} in detail"
)

summarize_prompt = ChatPromptTemplate.from_template(
 "Summarize this in 2 lines:\n{input}"
)

# Model
model = ChatOllama(model="llama3")

# Parser
parser = StrOutputParser()

# Chain
chain = explain_prompt | model | parser | summarize_prompt | model | parser

# Run
result = chain.invoke({"topic": "Docker"})
print(result)