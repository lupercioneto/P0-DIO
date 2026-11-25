import os

from dotenv import load_dotenv

load_dotenv()


def load_api_key() -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or not api_key.strip():
        raise RuntimeError(
            "Credencial ausente. Configure GROQ_API_KEY no arquivo .env."
        )

    return api_key.strip()
