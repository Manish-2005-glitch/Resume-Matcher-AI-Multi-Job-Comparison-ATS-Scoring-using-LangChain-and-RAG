import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


def get_llm():

    return ChatHuggingFace(
        llm=HuggingFaceEndpoint(
            repo_id="HuggingFaceH4/zephyr-7b-beta",
            huggingfacehub_api_token=os.getenv("HF_TOKEN"),
            task="text-generation",
            temperature=0.3,
            max_new_tokens=512,
        )
    )
