from pprint import pprint

from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from common.commom_llm import openrouter_model

"""
工具定义
"""


# 1.普通工具
# def multiply(a: int, b: int) -> int:
#     """Multiply two numbers."""
#     return a * b


# 2.使用langchain的tool装饰器
# @tool("multiply_tool", parse_docstring=True)
# def multiply(a: int, b: int) -> int:
#     """Multiply two numbers.
#
#     Args:
#         a: First operand
#         b: Second operand
#     """
#     return a * b

# 3.使用pydantic进行类型验证
# from pydantic import BaseModel, Field
#
# class MultiplyInputSchema(BaseModel):
#     """Multiply two numbers"""
#     a: int = Field(description="First operand")
#     b: int = Field(description="Second operand")
#
# @tool("multiply_tool", args_schema=MultiplyInputSchema)
# def multiply(a: int, b: int) -> int:
#     return a * b

# 4.并行多个工具
# def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b
#
#
# def multiply(a: int, b: int) -> int:
#     """Multiply two numbers."""
#     return a * b
#
#
# tools = [add, multiply]

# 5.t工具直接返回结果
# @tool(return_direct=True)
# def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b
#
# tools = [add]
# agent = create_react_agent(
#     model=openrouter_model,
#     tools=tools,
# )
# res = agent.invoke(
#
#     {"messages": [{"role": "user", "content": "what's 3 + 5 ?"}]}
# )
# pprint(res)

# 6.错误处理

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    if a == 42:
        raise ValueError("The ultimate error")
    return a * b

# Run with error handling (default)
agent = create_react_agent(
    model=openrouter_model,
    tools=[multiply]
)
res=agent.invoke(
    {"messages": [{"role": "user", "content": "what's 42 x 7?"}]}
)
pprint(res)