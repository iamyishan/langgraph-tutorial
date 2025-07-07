from langgraph.prebuilt import create_react_agent

from common.commom_llm import openrouter_model


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# 1.普通代理
# agent = create_react_agent(
#     model=openrouter_model,
#     tools=[get_weather],
# )
# for chunk in agent.stream(
#     {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
#     stream_mode="updates"
# ):
#     print(chunk)
#     print("\n")


# 2.带有token和metadata的代理
# agent = create_react_agent(
#     model=openrouter_model,
#     tools=[get_weather],
# )
# for token, metadata in agent.stream(
#     {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
#     stream_mode="messages"
# ):
#     print("Token", token)
#     print("Metadata", metadata)
#     print("\n")

# 3.要流式传输工具执行时的更新
# from langgraph.config import get_stream_writer
#
# def get_weather(city: str) -> str:
#     """Get weather for a given city."""
#     writer = get_stream_writer()
#     # stream any arbitrary data
#     writer(f"Looking up data for city: {city}")
#     return f"It's always sunny in {city}!"
#
# agent = create_react_agent(
#     model=openrouter_model,
#     tools=[get_weather],
# )
#
# for chunk in agent.stream(
#     {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
#     stream_mode="custom"
# ):
#     print(chunk)
#     print("\n")

#4.流式传输多种模式

agent = create_react_agent(
    model=openrouter_model,
    tools=[get_weather],
)

for stream_mode, chunk in agent.stream(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
    stream_mode=["updates", "messages", "custom"]
):
    print(chunk)
    print("\n")

