from IPython.core.display_functions import display
from PIL.Image import Image
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

from common.commom_llm import openrouter_model


def tool() -> None:
    """Testing tool."""
    ...

agent = create_react_agent(
    openrouter_model,
    tools=[tool],
)

# agent.get_graph().draw_mermaid_png()

try:
    mermaid_code = agent.get_graph().draw_mermaid_png( )
    with open("graph.jpg", "wb") as f:
        f.write(mermaid_code)
except Exception as err:
    # This requires some extra dependencies and is optional
    print(err)
