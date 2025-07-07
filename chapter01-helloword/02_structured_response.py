from pydantic import BaseModel
from langgraph.prebuilt import create_react_agent

from common.commom_llm import openrouter_model

"""
结构化输出
"""

class WeatherResponse(BaseModel):
    conditions: str

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"
agent = create_react_agent(
    model=openrouter_model,
    tools=[get_weather],
    response_format=WeatherResponse
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

print(response["structured_response"])