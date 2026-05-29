from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_community.llms import Ollama

# 1. Load LLM (Ollama local model)
llm = Ollama(model="llama3")

# 2. Memory (stores full conversation history)
memory = ConversationBufferMemory()

# 3. Create Conversation Chain
conversation = ConversationChain(
  llm=llm,
  memory=memory,
  verbose=True   # shows internal prompt flow
)

# 4. Start conversation
response1 = conversation.predict(input="Hi, my name is Mario")
print("AI:", response1)

response2 = conversation.predict(input="I work as a software engineer.")
print("AI:", response2)

response3 = conversation.predict(input="What is my name and profession?")
print("AI:", response3)


# 5. Print stored memory (chat history)
print("\n--- Conversation History ---")
print(memory.buffer)