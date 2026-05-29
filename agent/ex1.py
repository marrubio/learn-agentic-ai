from langchain_community.llms import Ollama
 
llm = Ollama(model="llama3")

while True:
    user_input = input("Me: ")
 
    if user_input.lower() in ["exit", "quit"]:
        print("Llama3: Goodbye!")
        break
 
    response = llm.invoke(user_input)
    print("Llama3:", response)



