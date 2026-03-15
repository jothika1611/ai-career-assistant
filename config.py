import os

# Choose the model provider for chat
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "ollama")  # "ollama" or "openai"

# OpenAI API key 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Ollama local model
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:4b")