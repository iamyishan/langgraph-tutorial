from langchain_community.chat_models import ChatZhipuAI
from dotenv import load_dotenv
import os

load_dotenv()
from langchain_openai import ChatOpenAI

# zhipuai 模型需要安装 pip install --upgrade httpx httpx-sse PyJWT
zhipuai_api_key = os.getenv('ZHIPUAI_API_KEY')

deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')

zhipu_model = ChatZhipuAI(
    temperature=0.8,
    api_key=zhipuai_api_key,
    model="GLM-4-Flash"
)

deepseek_model = ChatOpenAI(
    model='deepseek-chat',
    openai_api_key=deepseek_api_key,
    openai_api_base='https://api.deepseek.com',
    max_tokens=1024
)

openrouter_model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv('OPENROUTER_API_KEY'),
    model="deepseek/deepseek-chat-v3-0324:free"
)
