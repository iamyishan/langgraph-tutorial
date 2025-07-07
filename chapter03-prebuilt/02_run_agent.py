import asyncio
import time
from pprint import pprint

from langgraph.prebuilt import create_react_agent

from common.commom_llm import openrouter_model


def tool(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_react_agent(
    openrouter_model,
    tools=[tool],
)

# 1.同步调用
# response = agent.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
# pprint(response)


# 2.异步调用
# async def async_call_agent():
#     response = await agent.ainvoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
#     pprint(response)
# if __name__ == "__main__":
#     asyncio.run(async_call_agent())


# 3.同步调用和异步调用的时间对比
# def sync_call_agent():
#     response = agent.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
#     # pprint
# 同步调用两次
# def sync_call_agent_twice():
#     start_time = time.time()
#     for _ in range(2):
#         response = agent.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
#         # pprint
#         print("1111")
#     end_time = time.time()
#     return end_time - start_time
# # 并发调用两次
# async def async_call_agent_once():
#     response = await agent.ainvoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
#     # pprint(response)
#     print("2222")
#
# async def async_call_agent_twice():
#     start_time = time.time()
#     tasks = [async_call_agent_once() for _ in range(2)]
#     await asyncio.gather(*tasks)
#     end_time = time.time()
#     return end_time - start_time
#
# if __name__ == "__main__":
#     sync_time = sync_call_agent_twice()
#     async_time = asyncio.run(async_call_agent_twice())
#     time_diff = sync_time - async_time
#     print(f"同步调用两次耗时: {sync_time} 秒")
#     print(f"并发调用两次耗时: {async_time} 秒")
#     print(f"时间差: {time_diff} 秒")

# 4.同步流式调用
# for chunk in agent.stream(
#         {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
#         stream_mode="updates"
# ):
#     print(chunk)

# 5.异步流式调用
# async def async_stream_agent():
#     async for chunk in agent.astream(
#             {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
#             stream_mode="updates"
#     ):
#         print(chunk)
# if __name__ == '__main__':
#     asyncio.run(async_stream_agent())

# 6.迭代最大步数
from langgraph.errors import GraphRecursionError

max_iterations = 3
recursion_limit = 2 * max_iterations + 1

try:
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "what's the weather in sf"}]},
        {"recursion_limit": recursion_limit},
    )
except GraphRecursionError:
    print("Agent stopped due to max iterations.")