from pprint import pprint

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from common.commom_llm import openrouter_model

client = MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            # Replace with absolute path to your math_server.py file
            "args": ["D:\\code\\python\\langgraph\\mcp\\math_mcp.py"],
            "transport": "stdio",
        },
        "weather": {
            # Ensure your start your weather server on port 8000
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }
    }
)

async def main():
    tools = await client.get_tools()
    agent = create_react_agent(
        openrouter_model,
        tools
    )
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    pprint(math_response)

    # weather_response = await agent.ainvoke(
    #     {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    # )
    # pprint(weather_response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
