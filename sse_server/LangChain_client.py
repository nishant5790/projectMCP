from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import asyncio
import json

from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o-mini")

async def main():

    async with MultiServerMCPClient(
        {
            "math": {
                "url": "http://localhost:8082/sse",
                "transport": "sse",
            },
            "terminal": {
                #  terminal_server_sse.py
                "url": "http://localhost:8081/sse",
                "transport": "sse",
            }
        }
    ) as client:
        agent = create_react_agent(model, client.get_tools())
        math_response = await agent.ainvoke({"messages": "what's ((12*3)-(10/2))?"})
        terminal_response = await agent.ainvoke({"messages": "what the list of file in directry ?"})
        print(f"----------------------------------Math response: --------------------------------\n")
        for cnt in range(len(math_response['messages'])):
            if math_response['messages'][cnt].additional_kwargs:
                print(math_response['messages'][cnt].additional_kwargs)
            print(math_response['messages'][cnt].content)
            print('\n')
        print(f"\n -------------------------------Terminal response: --------------------\n")
        for cnt in range(len(terminal_response['messages'])):
            if terminal_response['messages'][cnt].additional_kwargs:
                print(terminal_response['messages'][cnt].additional_kwargs)
            print(terminal_response['messages'][cnt].content)
            print('\n')


        # print(f"Terminal response: {terminal_response}")
        
if __name__ == "__main__":
    asyncio.run(main())