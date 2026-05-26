#Plan-and-Execute Agent
from langchain_community.llms import Ollama
import json
 
# =========================
# 🧠 LLM CONFIG
# =========================
MODEL = "llama3"   # make sure you pulled: ollama pull llama3
ollama = Ollama(model=MODEL)
 
# =========================
# 🛠️ TOOLS
# =========================
 
def fetch_logs():
    try:
        with open("pipeline.log", "r") as f:
            return f.read()
    except:
        return """
        ERROR: ModuleNotFoundError: No module named 'pandas'
        """
 
 
def identify_errors(logs):
    prompt = f"""
    Extract all errors from this log and return as JSON list.
 
    LOG:
    {logs}
    """
 
    response = ollama.invoke(prompt)

    try:
        return json.loads(response)
    except:
        return [response]
 
 
def classify_failure(errors):
    prompt = f"""
    Classify the failure type from these errors:
    {errors}
 
    Categories:
    - Dependency Issue
    - Syntax Error
    - Network Issue
    - Configuration Issue
    - Unknown
 
    Return only category.
    """
 
    response = ollama.invoke(prompt)

    return response.strip()
 
 
def suggest_fix(failure_type, errors):
    prompt = f"""
    Suggest fix for:
    Failure Type: {failure_type}
    Errors: {errors}
 
    Keep answer short and actionable.
    """
 
    response = ollama.invoke(prompt)

    return response
 
 
def generate_report(memory):
    prompt = f"""
    Create a clean report from this execution memory:
 
    {memory}
 
    Format:
    - Errors
    - Failure Type
    - Suggested Fix
    """
 
   
    response = ollama.invoke(prompt)

    return response
 
 
# =========================
# 🧠 PLANNER (LLM)
# =========================
 
def create_plan(user_input):
    prompt = f"""
    Break this task into ordered steps.
 
    Task: {user_input}
 
    Only return JSON array of step names.
    Example:
    ["fetch_logs", "identify_errors", "classify_failure", "suggest_fix", "generate_report"]
    """
 
    response = ollama.invoke(prompt)

    try:
        return json.loads(response)
    except:
        # fallback plan
        return [
            "fetch_logs",
            "identify_errors",
            "classify_failure",
            "suggest_fix",
            "generate_report"
        ]
 
 
# =========================
# ⚙️ EXECUTOR
# =========================
 
tools = {
    "fetch_logs": fetch_logs,
    "identify_errors": identify_errors,
    "classify_failure": classify_failure,
    "suggest_fix": suggest_fix,
    "generate_report": generate_report
}
 
 
def execute_plan(plan):
    memory = {}
    context = {}
 
    for step in plan:
        print(f"\n🔹 Executing: {step}")
 
        if step == "fetch_logs":
            result = tools[step]()
            context["logs"] = result
 
        elif step == "identify_errors":
            result = tools[step](context["logs"])
            context["errors"] = result
 
        elif step == "classify_failure":
            result = tools[step](context["errors"])
            context["failure_type"] = result
 
        elif step == "suggest_fix":
            result = tools[step](
                context["failure_type"],
                context["errors"]
            )
            context["fix"] = result
 
        elif step == "generate_report":
            result = tools[step](memory)
 
        else:
            result = f"Unknown step: {step}"
 
        memory[step] = result
 
    return memory["generate_report"]
 
 
# =========================
# 🚀 MAIN
# =========================
 
if __name__ == "__main__":
    user_input = "Analyze failed pipeline logs and suggest fixes"
 
    print("\n🧠 Generating Plan...\n")
    plan = create_plan(user_input)
 
    print("📋 PLAN:", plan)
 
    print("\n⚙️ Executing Plan...\n")
    final_output = execute_plan(plan)
 
    print("\n✅ FINAL REPORT:\n")
    print(final_output)
