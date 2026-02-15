import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

def get_llm():
    endpoint = HuggingFaceEndpoint(
        repo_id = "deepseek-ai/DeepSeek-V3.2",
        task="text-generation",

        max_new_tokens=512,

        temperature=0.2,

        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
    )
    
    llm = ChatHuggingFace(llm = endpoint)
    
    return llm