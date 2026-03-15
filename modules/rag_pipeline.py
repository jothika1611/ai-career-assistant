from modules.generator import generate

def chat_with_pdf(question: str, vectorstore, chat_history: list) -> str:
    """
    RAG-based question answering with conversation memory
    """

    # 1. Retrieve relevant chunks from the vector store
    docs = vectorstore.similarity_search(question, k=3)

    # 2. Build document context
    context_text = "\n\n".join(
        doc.page_content.strip()
        for doc in docs
        if hasattr(doc, "page_content")
    )

    # 3. Format conversation history (limit last 3 turns)
    history_str = ""
    for q, a in chat_history[-3:]:
        history_str += f"User asked: {q}\nAssistant replied: {a}\n\n"

    # 4. Build prompt
    prompt = f"""
You are a helpful AI assistant that answers questions based on a document.

Use the document context and conversation history only for understanding.

IMPORTANT RULES:
- Do NOT repeat the conversation history.
- Do NOT return answers in Q/A format.
- Do NOT show previous questions.
- Only return the final answer to the current question.



Document Context:
{context_text}

Current Question:
{question}

Final Answer:
"""

    # 5. Generate answer
    answer = generate(prompt)


    return answer