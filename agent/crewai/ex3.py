from crewai import Agent, Task, Crew, LLM
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
 
# 🔹 1. Load documents
loader = TextLoader("data.txt")
documents = loader.load()
 
# 🔹 2. Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
docs = text_splitter.split_documents(documents)
 
# 🔹 3. Create embeddings
embeddings = HuggingFaceEmbeddings()
 
# 🔹 4. Store in vector DB (FAISS)
db = FAISS.from_documents(docs, embeddings)
 
# 🔹 5. Retrieval function
def retrieve_context(query):
    results = db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in results])
 
# 🔹 6. LLM (Ollama)
llm = LLM(
    model="ollama/llama3",
    base_url="http://localhost:11434"
)
 
# 🔹 7. Agents
 
retriever_agent = Agent(
    role="Retriever",
    goal="Fetch relevant information from documents",
    backstory="Expert in searching knowledge bases",
    llm=llm,
    verbose=True
)
 
writer_agent = Agent(
    role="Answer Generator",
    goal="Generate accurate answers using retrieved context",
    backstory="Expert in explaining concepts clearly",
    llm=llm,
    verbose=True
)
 
# 🔹 8. User Query
query = "What is Agentic AI?"
 
# 🔹 9. Get context (RAG step)
context_data = retrieve_context(query)
 
# 🔹 10. Tasks
 
task1 = Task(
    description=f"""
    Retrieve and summarize relevant information for:
    {query}
 
    Context:
    {context_data}
    """,
    expected_output="Relevant summarized information from documents",
    agent=retriever_agent
)
 
task2 = Task(
    description="""
    Generate a final answer using retrieved context.
    """,
    expected_output="Clear and accurate answer",
    agent=writer_agent,
    context=[task1]
)
 
# 🔹 11. Crew
 
crew = Crew(
    agents=[retriever_agent, writer_agent],
    tasks=[task1, task2],
    verbose=True
)
 
# 🔹 12. Run
 
if __name__ == "__main__":
    result = crew.kickoff()
    print("\n🔥 FINAL ANSWER:\n")
    print(result)