import os
from langchain_huggingface import ChatHuggingFace
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()


def get_llm():

    token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

    client = InferenceClient(
        model="HuggingFaceH4/zephyr-7b-beta",
        token=token
    )

    return ChatHuggingFace(llm=client)