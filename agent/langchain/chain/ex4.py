#parallem chain
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama

model = ChatOllama(model="llama3")

# Prompts
summary_prompt = ChatPromptTemplate.from_template(
  "Summarize this text: {text}"
)

keyword_prompt = ChatPromptTemplate.from_template(
  "Extract keywords from this text: {text}"
)

# Clean text output parser
parser = StrOutputParser()

# Chains
summary_chain = summary_prompt | model | parser
keyword_chain = keyword_prompt | model | parser

# Parallel execution
parallel_chain = RunnableParallel(
  summary=summary_chain,
  keywords=keyword_chain
)

result = parallel_chain.invoke({
  "text": "LangChain is used for building AI applications"
})

print(result)