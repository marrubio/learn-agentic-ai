from 4phi.agent import Agent
from phi.model.ollama import Ollama
from phi.storage.agent.sqlite import SqlAgentStorage
 
# 💾 Memory + Storage (SQLite file)
storage = SqlAgentStorage(
    db_file="agent_memory.db",   # creates local DB file
    table_name="agent_sessions"
)
 
# 🤖 Agent with memory + caching
agent = Agent(
    model=Ollama(id="mistral"),
 
    # ✅ MEMORY
    storage=storage,
    add_history_to_messages=True,   # remembers conversation
 
    # ✅ CACHING (same query → faster response)
    cache=True,
 
    markdown=True,
    debug=True
)
 
# 👇 SESSION ID (important for memory)
session_id = "user_1"
 
# =========================
# INTERACTION 1
# =========================
print("\n--- FIRST MESSAGE ---\n")
agent.print_response(
    "My name is Rakesh",
    session_id=session_id
)
 
# =========================
# INTERACTION 2
# =========================
print("\n--- SECOND MESSAGE ---\n")
agent.print_response(
    "What is my name?",
    session_id=session_id
)
 
# =========================
# CACHING TEST
# =========================
print("\n--- CACHING TEST ---\n")
agent.print_response(
    "Explain AI agents",
    session_id=session_id
)
 
print("\n--- SAME QUESTION AGAIN (FAST) ---\n")
agent.print_response(
    "Explain AI agents",
    session_id=session_id
)