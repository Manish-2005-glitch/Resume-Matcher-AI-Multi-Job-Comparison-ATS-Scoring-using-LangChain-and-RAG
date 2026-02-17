from langchain_community.vectorstores import Chroma
from rag.embeddings import get_embeddings

def create_vector_store(chunks):
    
    embeddings = get_embeddings()
    
    db = Chroma.from_texts(
        texts=chunks,
        embedding = embeddings,
        persist_directory="chroma_db"
    )
    
    return db

def get_retriever():
    
    embeddings = get_embeddings()
    
    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    
    retriever = db.as_retriever(
        search_kwargs = {"k":5}
    )
    
    return retriever