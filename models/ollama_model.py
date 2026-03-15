import subprocess
from config import OLLAMA_MODEL

def generate_response(prompt: str) -> str:
    try:
        process = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=True
        )
        output = process.stdout.strip()
        return output if output else f"No output from Ollama. Stderr:\n{process.stderr}"
    except subprocess.CalledProcessError as e:
        err_msg = e.stderr or "Unknown error"
        return f"Error: Could not get response from Ollama.\n{err_msg}"