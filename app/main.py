from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import query_chroma, generate_response
from generate_response_with_history import generate_response_with_history
from embeddings import collection

from util import create_session_id, save_history, get_history, delete_session

app = FastAPI()

# Request body structure
class QuestionRequest(BaseModel):
    question: str

# Endpoint to handle questions
@app.post("/ask")
def ask_bot(request: QuestionRequest):
    docs, metas = query_chroma(request.question, collection)
    answer = generate_response(request.question, docs)
    return {
        "answer": answer,
        "sources": metas
    }

class QuestionRequest(BaseModel):
    question: str

@app.post("/start")
def start_chat():
    session_id = create_session_id()
    save_history(session_id, [])
    return {"session_id": session_id}

@app.delete("/exit/{session_id}")
def exit_chat(session_id: str):
    delete_session(session_id)
    return {"message": f"Session {session_id} ended and chat history cleared."}

@app.post("/chat/{session_id}")
def chat_bot(session_id: str, request: QuestionRequest):
    question = request.question

    # Load history or start new
    conversation_history = get_history(session_id)

    # Add instruction only for new sessions
    if not conversation_history:
        conversation_history.append({
            "role": "user",
            "parts": [{
                "text": (
                    "Make sure you give the answers in detail. also give the code example if possible. "
                    "If customer greets you instead of any question greet them back and ask how"
                    "can i help you today?"
                    "Answer the following question using the context below. "
                    "Give the answers to the point, remove any extra information, "
                    "and avoid anything not related to the question or context. "
                    "Also if you do not find any relevant information about the "
                    "question do not behave like a chatbot just I do not have this "
                    "information please write to support."
                )
            }]
        })

    # Use RAG to get context
    docs, metas = query_chroma(question, collection)
    context = "\n".join(docs)

    # Append the new question
    prompt = f"Context:\n{context}\n\nQuestion:\n{question}"
    conversation_history.append({"role": "user", "parts": [{"text": prompt}]})

    # Get answer from Gemini
    answer = generate_response_with_history(conversation_history)
    conversation_history.append({"role": "model", "parts": [{"text": answer}]})

    # Save updated history
    save_history(session_id, conversation_history)

    return {"session_id": session_id, "answer": answer, "sources": metas}

# @app.post("/chat")
# def chat_bot(request: QuestionRequest):
#     question = request.question
#
#     # RAG for context
#     docs, metas = query_chroma(question, collection)
#     context = "\n".join(docs)
#
#     # Build prompt
#     prompt = f"""Context:\n{context}\n\nQuestion:\n{question}"""
#
#     # If first turn, add instruction system prompt
#     if not conversation_history:
#         conversation_history.append({
#             "role": "user",
#             "parts": [{
#                 "text": (
#                     "Answer the following question using the context below. "
#                     "Give the answers to the point, remove any extra information, "
#                     "and avoid anything not related to the question or context. "
#                     "Also if you do not find any relevant information about the "
#                     "question do not behave like a chatbot just I do not have this"
#                     "information please write to support."
#                 )
#             }]
#         })
#
#     # Append user's contextualized question
#     conversation_history.append({"role": "user", "parts": [{"text": prompt}]})
#
#     # Gemini call
#     answer = generate_response_with_history(conversation_history)
#
#     # Append model response
#     conversation_history.append({"role": "model", "parts": [{"text": answer}]})
#
#     return {"answer": answer, "sources": metas}
