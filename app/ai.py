import os
from typing import Optional

def generate_suggestion(prompt: str) -> str:
    """Generate a short todo suggestion based on a user prompt.
    If an OpenAI API key is set in the environment variable ``OPENAI_API_KEY``,
    the function calls the OpenAI ChatCompletion endpoint (gpt-3.5‑turbo).
    Otherwise it falls back to a deterministic simple suggestion.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            import openai
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Suggest a concise todo item based on: {prompt}"}],
                max_tokens=30,
                n=1,
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"AI suggestion failed: {e}. Try a simpler prompt."
    # Simple deterministic fallback
    return f"Review {prompt}" if prompt else "New Todo"
