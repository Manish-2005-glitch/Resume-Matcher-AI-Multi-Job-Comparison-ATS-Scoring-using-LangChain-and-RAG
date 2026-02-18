import os
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

from dotenv import load_dotenv 

load_dotenv()

def get_embeddings():
    return HuggingFaceInferenceAPIEmbeddings(
        api_key=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
