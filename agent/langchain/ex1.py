from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
 
# LLM
llm = ChatOllama(model="llama3")
 
# Tool
@tool
def calculator(input: str) -> str:
    """Use this tool to perform mathematical calculations."""
    return str(eval(input))
 
tools = [calculator]
 
# Correct Prompt
prompt = PromptTemplate.from_template("""
You are an intelligent agent.
 
You have access to the following tools:
{tools}
 
Use this format:
 
Question: {input}
Thought: think step by step
Action: one of [{tool_names}]
Action Input: input to the tool
Observation: result
Final Answer: the final answer
 
Begin!
 
Question: {input}
Thought:
{agent_scratchpad}
""")
 
# Agent
agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
 
# Run
result = executor.invoke({"input": "What is 15 * 6?"})
print(result["output"])