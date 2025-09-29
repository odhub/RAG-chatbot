import gradio as gr
import requests
import os

# Environment variables (override in podman run if needed)
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")
OLLAMA_PORT = int(os.getenv("OLLAMA_PORT", "11434"))
MODEL = os.getenv("MODEL", "mistral-7b-instruct")

OLLAMA_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"

def chat_fn(message, history):
    # history is a list of dicts: {"role": "user"/"assistant", "content": "..."}
    turns = "\n".join(
        f"{msg['role'].capitalize()}: {msg['content']}" for msg in history
    )
    prompt = f"{turns}\nUser: {message}\nAssistant:"

    try:
        resp = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=180
        )
        data = resp.json()
        return data.get("response", "No response from Ollama")
    except Exception as e:
        return f"Error contacting Ollama: {e}"

demo = gr.ChatInterface(
    fn=chat_fn,
    type="messages",  # avoids the deprecation warning
    title="RAG Chatbot (Gradio)",
    description="Chatbot UI connected to Ollama backend",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
