from sentence_transformers import SentenceTransformer
import chromadb
import os
from chromadb.config import Settings

# Initialize Chroma

chroma_client = chromadb.PersistentClient(path="../chroma_db")

# collection = chroma_client.get_or_create_collection(name="support_docs_all-mpnet-base-v2")
# model = SentenceTransformer('all-MiniLM-L6-v2')  # light & fast
collection = chroma_client.get_or_create_collection(name="react_docs")
model = SentenceTransformer('all-mpnet-base-v2')

def ingest_to_chroma(data):
    x = 15000;
    for idx, (url, text) in enumerate(data):
        embeddings = model.encode([text])
        collection.add(
            documents=[text],
            embeddings=embeddings.tolist(),
            ids=[f"doc_{x}"],
            metadatas=[{"source": url}]
        )
        x = x + 1
