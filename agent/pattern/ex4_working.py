import requests


# -----------------------------
# LLM (Ollama)
# -----------------------------
def call_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False,
        },
    )
    return response.json()["response"]



# -----------------------------
# TOOL: Search
# -----------------------------
def search_tool(query):
    print(f"[TOOL] Searching: {query}")
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    data = requests.get(url).json()
    return data.get("AbstractText", "No result found")


# -----------------------------
# AGENT LOOP
# -----------------------------
def agent(goal):
    memory = []

    for step in range(4):
        print(f"\n--- Step {step+1} ---")
        context = "\n".join(memory)
        prompt = f"""
You are an AI agent.
Goal: {goal}
Memory:
{context}

You can:
1. PLAN what to do
2. EXECUTE by either:
    - SEARCH <query>
    - ANSWER directly

Respond strictly:
PLAN: ...
ACTION: SEARCH or ANSWER
INPUT: ...

"""
        output = call_llm(prompt)
        print(output)

        memory.append(output)

        # --- TOOL USE ---
        if "ACTION: SEARCH" in output:
            query = output.split("INPUT:")[-1].strip()
            result = search_tool(query)

            print("Observation:", result)
            memory.append(f"Search result: {result}")

        elif "ACTION: ANSWER" in output:
            answer = output.split("INPUT:")[-1].strip()
            print("\n✅ Final Answer:", answer)
            break


# -----------------------------
# RUN
# -----------------------------

if __name__ == "__main__":
    agent("What is Agentic AI and give 2 real-world examples")