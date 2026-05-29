from langchain_ollama import OllamaLLM
 
llm = OllamaLLM(model="llama3")

response = llm.invoke("Find temperature in Madrid and convert to Fahrenheit")
print("LLM response:", response)