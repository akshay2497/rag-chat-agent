# from transformers import pipeline
from sentence_transformers import SentenceTransformer
import requests
import os

# Initialize embedding model
# embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
embedding_model = SentenceTransformer('all-mpnet-base-v2')

def query_chroma(question, collection, top_k=1):
    query_embedding = embedding_model.encode([question])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results['documents'][0], results['metadatas'][0]

GEMINI_API_KEY = 'XXX'  # Or hardcode for testing


def generate_response(question, docs):
    context = "\n".join(docs)
    prompt = f"""Answer the following question using the context below give the answers to the point remove any extra information anything not related to the question context:

Context:
{context}

Question: {question}
Answer:"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "No answer could be generated from Gemini API."
    else:
        return f"Gemini API Error: {response.status_code}, {response.text}"

# Initialize LLM (e.g., DeepSeek)
# qa = pipeline("text-generation", model="deepseek-ai/deepseek-coder-6.7b-base", device_map="auto")

# Below one uses deepseek coder which is a heavy version which is not able to work on
# my laptop
# def generate_response(question, docs):
#     context = "\n".join(docs)
#     prompt = f"Answer the following question using the context:\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
#     response = qa(prompt, max_new_tokens=200)
#     return response[0]["generated_text"]

