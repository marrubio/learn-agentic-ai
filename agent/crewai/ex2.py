from crewai import Agent, Task, Crew, LLM

# 🔹 1. LLM (Ollama via LiteLLM)
llm = LLM(
  model="ollama/llama3",
  base_url="http://localhost:11434"
)

# 🔹 2. Agents
researcher = Agent(
  role="Senior Research Analyst",
  goal="Find accurate and useful information about topics",
  backstory="Expert in AI and technology research",
  llm=llm,
  verbose=True
)

writer = Agent(
  role="Content Writer",
  goal="Write clear and engaging articles",
  backstory="Expert in technical writing",
  llm=llm,
  verbose=True
)


reviewer = Agent(
  role="Editor",
  goal="Improve quality, clarity, and correctness",
  backstory="Strict editor with attention to detail",
  llm=llm,
  verbose=True
)


# 🔹 3. Tasks (IMPORTANT: expected_output required)
task1 = Task(
  description="Research and summarize Agentic AI with real-world examples",
  expected_output="A clear summary of Agentic AI with at least 3 real-world use cases",
  agent=researcher
)


task2 = Task(
  description="Write a detailed article based on the research",
  expected_output="A well-structured article explaining Agentic AI",
  agent=writer,
  context=[task1]   # 🔥 uses output of task1
)


task3 = Task(
    description="Review and improve the article for clarity and accuracy",
    expected_output="A refined and polished version of the article",
    agent=reviewer,
    context=[task2]   # 🔥 uses output of task2
)

# 🔹 4. Crew (multi-agent system)

crew = Crew(
  agents=[researcher, writer, reviewer],
  tasks=[task1, task2, task3],
  verbose=True
)

# 🔹 5. Run

if __name__ == "__main__":
  result = crew.kickoff()
  print("\n\n🔥 FINAL OUTPUT:\n")
  print(result)