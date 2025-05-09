import os
import httpx

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "BAAI/bge-m3")

async def query_llm(query: str, context: str) -> str:
    payload = {
        "inputs": {
            "question": query,
            "context": context
        }
    }
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://api-inference.huggingface.co/models/{MODEL_NAME}",
            headers=headers,
            json=payload
        )
        
        if response.status_code != 200:
            print("🔴 Hugging Face API error:", response.status_code, response.text)
            return f"API error: {response.status_code}"

        try:
            result = response.json()
            return result.get("answer", "No answer found.")
        except Exception as e:
            print("🔴 JSON decode error:", e)
            return "Error parsing LLM response."