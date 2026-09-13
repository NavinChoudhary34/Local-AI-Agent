import asyncio

from src.agent import Agent
from src.tools import tools, tool_descriptions

def main():
    instructions= (
        "You are a tool calling agent that may use the following tools by rsponding according to their instructions.\n"
        "Available tools.\n"
        f"{tool_descriptions}\n"
        "If no tool is needed, respond with the final answer."
    )

    agent = Agent(
        tools = tools,
        instructions = instructions
    )

    #run loop
    print("Hello u r chating with the agent.\n type 'exit' or 'bye' or 'quit' to end the chat")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {'exit','bye','quit'}:
            print("goodbye")
            break
        result = asyncio.run(agent.run(user_input))
        print(f"Agent: {result.strip()}")

if __name__ == "__main__":
    main()