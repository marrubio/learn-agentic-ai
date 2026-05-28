from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# Prompt
prompt = ChatPromptTemplate.from_template("Explain {topic} in simple terms")

# Llama3 model via Ollama
model = ChatOllama(model="llama3")

# Parser
parser = StrOutputParser()

# LCEL chain
chain = prompt | model | parser

# Run
print(chain.invoke({"topic": "Kubernetes"}))