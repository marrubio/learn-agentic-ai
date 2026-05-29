from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_classic.chains import RetrievalQA

# 1️⃣ Load LLM (local)
llm = ChatOllama(model="llama3")


# 2️⃣ Load document
loader = TextLoader("data.txt")
documents = loader.load()

# 3️⃣ Split into chunks
text_splitter = CharacterTextSplitter(
  chunk_size=200,
  chunk_overlap=20
)

docs = text_splitter.split_documents(documents)

# 4️⃣ Create embeddings (IMPORTANT)
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# 5️⃣ Store in FAISS vector DB
vectorstore = FAISS.from_documents(docs, embeddings)


# 6️⃣ Create retriever
retriever = vectorstore.as_retriever()


# 7️⃣ Create RAG pipeline
qa = RetrievalQA.from_chain_type(
  llm=llm,
  retriever=retriever
)

# 8️⃣ Ask questions
query = "What is the name of the actual president of Spain?"
result = qa.run(query)

print("\n=== ANSWER ===\n")
print(result)