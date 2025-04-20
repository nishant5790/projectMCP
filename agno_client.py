import asyncio
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters


async def run_agent(message: str) -> None:
    """Run the filesystem agent with the given message."""

    file_path = str(Path(__file__).parent.parent.parent.parent)

    # Create server parameters for stdio connection
    # server_params = StdioServerParameters(
    #     command="python",
    #     # Make sure to update to the full absolute path to your math_server.py file
    #     args=[f"{file_path}/projectMCP/server.py"],
    # )
    async with MCPTools(f"python /home/knish/projectMCP/server.py") as mcp_tools:
        agent = Agent(
            model=OpenAIChat(id="gpt-4o"),
            tools=[mcp_tools],
            instructions=dedent("""\
                You are a math expert. You can use the tools to perform calculations.
                
            """),
            markdown=True,
            show_tool_calls=True,
        )

        # Run the agent
        await agent.aprint_response(message, stream=True)


# Example usage
if __name__ == "__main__":
    # Basic example - exploring project license
    asyncio.run(run_agent("What is the value of (5+10)*10-5?"))