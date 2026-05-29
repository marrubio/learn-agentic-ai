from langsmith import Client
from langchain_community.llms import Ollama


# LangSmith client
 
client = Client(
  api_key="************************",
  api_url="https://eu.api.smith.langchain.com"
)


# Local Ollama model
ollama = Ollama(model="llama3", temperature=0.7)

# Prompt
prompt = "List 3 interesting facts about Neptune."

# Call model
result = ollama.invoke(prompt)

# Print LLM output
print("LLM Response:\n", result)

# Log run manually to LangSmith
client.create_run(
  name="Ollama Llama3 Run",
  run_type="llm",
  inputs={"prompt": prompt},
  outputs={"output": result},
  project_name="test"
)

print("Logged to LangSmith successfully!")