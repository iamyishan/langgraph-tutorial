from pprint import pprint
from langgraph.checkpoint.memory import InMemorySaver
from common.commom_llm import openrouter_model
model = openrouter_model
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

tools = [get_weather]
# 1.历史记忆
# from langgraph.prebuilt import create_react_agent
# from langgraph.checkpoint.memory import InMemorySaver
#

#
# checkpointer = InMemorySaver()
#
# agent = create_react_agent(
#     model=openrouter_model,
#     tools=[get_weather],
#     checkpointer=checkpointer
# )
#
# # Run the agent
# config = {
#     "configurable": {
#         "thread_id": "1"
#     }
# }
#
# sf_response = agent.invoke(
#     {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
#     config
# )
#
# # Continue the conversation using the same thread_id
# ny_response = agent.invoke(
#     {"messages": [{"role": "user", "content": "what about new york?"}]},
#     config
# )
# print(ny_response)


# 2.总结记忆
from common.commom_llm import openrouter_model
from langchain_core.messages.utils import count_tokens_approximately
# from common.commom_llm import openrouter_model
#

# from langmem.short_term import SummarizationNode
# from langchain_core.messages.utils import count_tokens_approximately
# from langgraph.prebuilt import create_react_agent
# from langgraph.prebuilt.chat_agent_executor import AgentState

# from typing import Any
#
# summarization_node = SummarizationNode(
#     token_counter=count_tokens_approximately,
#     model=model,
#     max_tokens=384,
#     max_summary_tokens=128,
#     output_messages_key="llm_input_messages",
# )
#
#
# class State(AgentState):
#     # NOTE: we're adding this key to keep track of previous summary information
#     # to make sure we're not summarizing on every LLM call
#     context: dict[str, Any]
#
#
# checkpointer = InMemorySaver()
# tools = [get_weather]
# agent = create_react_agent(
#     model=model,
#     tools=tools,
#     pre_model_hook=summarization_node,
#     state_schema=State,
#     checkpointer=checkpointer,
# )
#
# config = {
#     "configurable": {
#         "thread_id": "1"
#     }
# }
#
# res = agent.invoke(
#     {
#         "messages": "look up user information",
#         "context": {"user": "Alice"}
#     },
#     config
#
# )
# pprint(res)

# 3.裁剪消息
from langchain_core.messages.utils import (
    trim_messages,
    count_tokens_approximately
)
from langgraph.prebuilt import create_react_agent

# This function will be called every time before the node that calls LLM
def pre_model_hook(state):
    trimmed_messages = trim_messages(
        state["messages"],
        strategy="last",
        token_counter=count_tokens_approximately,
        max_tokens=384,
        start_on="human",
        end_on=("human", "tool"),
    )
    return {"llm_input_messages": trimmed_messages}

checkpointer = InMemorySaver()
agent = create_react_agent(
    model,
    tools,
    pre_model_hook=pre_model_hook,
    checkpointer=checkpointer,
)