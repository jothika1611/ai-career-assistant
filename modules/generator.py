from config import MODEL_PROVIDER

if MODEL_PROVIDER == "openai":
    from models.openai_model import generate_response as generate
else:
    from models.ollama_model import generate_response as generate