from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.calculator import Calculator


# Create AI Agent
agent = Agent(
  model=Ollama(id="llama3.1"),
  # Tools (this makes it powerful 🔥)
  tools=[
        DuckDuckGo(),   # for internet search
        Calculator()    # for math
        ],
  # Instructions (very important)
  instructions=[
    "Always use calculator for math",
    "Use search tool for latest information",
    "Give clear and structured answers"
    ],
  # Memory
  add_history_to_messages=True,
  # Debugging
  show_tool_calls=True,
  markdown=True

)

# Run multiple queries
agent.print_response("What is 25% of 200?")
agent.print_response("Latest news about AI agents")
agent.print_response("My name is Rakesh")
agent.print_response("What is my name?")