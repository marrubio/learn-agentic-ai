# Iterative loop
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


# Call Llama
def ask_llama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
    )
    return response.json()["response"].strip()


# Generate initial text
def generate():
    return "AI is good"


# Evaluate (simple rule)
def evaluate(text):
    return len(text) > 40  # want longer sentence


# Improve using Llama
def improve(text):
    prompt = f"""
Improve this sentence to make it more detailed and meaningful:

{text}

Return only improved sentence.
"""
    return ask_llama(prompt)


# Iterative loop
def iterative_loop(max_iterations=5):
    result = generate()

    for i in range(max_iterations):
        print(f"\nIteration {i + 1}: {result}")

        if evaluate(result):
            print("✅ Good enough!")
            break

        result = improve(result)

    return result


# Run
if __name__ == "__main__":
    final = iterative_loop()
    print("\n🏁 Final Output:\n", final)
