from datetime import datetime
from langsmith import Client
from langchain_community.llms import Ollama
 
# 1️⃣ LangSmith client
 
client = Client(
  api_key="************************",
  api_url="https://eu.api.smith.langchain.com"
)

 
 
# 2️⃣ Ollama Llama3 model
ollama = Ollama(model="llama3", temperature=0.7)
 
# 3️⃣ List of prompts to test
prompts = [
    "Explain 3 facts about Neptune in simple words.",
    "Explain 3 facts about Uranus in simple words.",
    "Explain 3 facts about Saturn in simple words."
]
 
# 4️⃣ Loop through prompts
for prompt in prompts:
    # Call the model
    result = ollama.invoke(prompt)
   
    # Print locally
    print(f"\nPrompt: {prompt}")
    print("LLM Response:")
    print(result)
   
    # Log each run with extra metadata
    client.create_run(
        name="Planet Facts Experiment",
        run_type="llm",
        inputs={"prompt": prompt, "model": "llama3", "temperature": 0.7},
        outputs={"output": result},
        project_name="test",
        metadata={
            "timestamp": datetime.now().isoformat(),
            "experiment": "planet_facts_test"
        }
    )
 
print("\nAll prompts logged to LangSmith successfully!")