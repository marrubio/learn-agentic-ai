from crewai import Agent, Task, Crew, LLM

llm = LLM(
  model="ollama/llama3",
  base_url="http://localhost:11434"
)


agent = Agent(
  role="Assistant",
  goal="Help user",
  backstory="AI agent",
  llm=llm,
  verbose=True
)

task = Task(
  description="What is 25 * 4 + 10?",
  expected_output="The final numerical answer", # ✅ FIX
  agent=agent
)


crew = Crew(
  agents=[agent],
  tasks=[task]
)

print(crew.kickoff())