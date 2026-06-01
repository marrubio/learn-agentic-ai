from phi.agent import Agent
from phi.model.ollama import Ollama

# Research Agent (no tool for stability)

research_agent = Agent(
  name="Researcher",
  model=Ollama(id="mistral"),
  instructions=["Give a factual overview of the topic"],
  markdown=True
)
writer_agent = Agent(
  name="Writer",
  model=Ollama(id="mistral"),
  instructions=["Write clearly and structured"],
  markdown=True
)


reviewer_agent = Agent(
  name="Reviewer",
  model=Ollama(id="mistral"),
  instructions=["Improve clarity and grammar"],
  markdown=True
)

topic = "AI agents in 2026"

print("🔍 Researching...")
research = research_agent.run(topic).content

print("✍️ Writing...")
draft = writer_agent.run(f"Write article:\n{research}").content

print("🧪 Reviewing...")
final = reviewer_agent.run(f"Improve:\n{draft}").content

print("\n===== FINAL OUTPUT =====\n")
print(final)