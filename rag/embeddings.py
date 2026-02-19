import os
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv 

load_dotenv()

def get_embeddings():

    return HuggingFaceEndpointEmbeddings(
        repo_id="sentence-transformers/all-MiniLM-L6-v2",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
    )
