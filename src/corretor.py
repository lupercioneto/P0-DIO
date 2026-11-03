import os

from dotenv import load_dotenv
from groq import (
    Groq,
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    RateLimitError,
)

load_dotenv()

MODEL = "openai/gpt-oss-120b"


def correct_text(text: str, client: Groq | None = None) -> str:
    """
    Recebe um texto e retorna sua versão corrigida pelo LLM.

    Args:
        text: Texto que será revisado.
        client: Cliente Groq opcional, utilizado também nos testes.

    Returns:
        Texto corrigido pelo modelo.

    Raises:
        ValueError: Se o texto estiver vazio ou for inválido.
        RuntimeError: Se ocorrer algum erro na comunicação com a API.
    """

    # Validações
    if not isinstance(text, str) or not text.strip():
        raise ValueError("O texto não pode estar vazio.")

    if client is None:
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise RuntimeError("GROQ_API_KEY não encontrada.")

        client = Groq(api_key=api_key, timeout=30.0)


    # Instruções ao modelo
    system_prompt = """
    Você é um corretor gramatical especializado na língua portuguesa.

    Sua tarefa é revisar textos enviados pelo usuário.

    Siga estas instruções:
    1. Corrija erros ortográficos, gramaticais e de pontuação.
    2. Preserve o significado original do texto.
    3. Não altere desnecessariamente o estilo de escrita.
    4. Não acrescente informações.
    5. Apresente o texto corrigido.
    6. Explique brevemente as principais correções realizadas.

    Organize sua resposta em três seções:

    TEXTO ORIGINAL: 
    [Texto Original]

    TEXTO CORRIGIDO:
    [Texto revisado]

    CORREÇÕES REALIZADAS:
    [Lista das principais correções e suas explicações]

    Se não houver erros, informe que o texto já está correto.
    """

    # Request com a API 
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=0.2,
            max_completion_tokens=1024
        )

        result = response.choices[0].message.content

        if not result or not result.strip():
            raise RuntimeError("O modelo retornou uma resposta vazia.")

        return result.strip()

    except AuthenticationError as error:
        raise RuntimeError("Chave da API inválida ou sem autorização.") from error

    except RateLimitError as error:
        raise RuntimeError("Limite de requisições da API atingido.") from error

    except APIConnectionError as error:
        raise RuntimeError("Não foi possível conectar à API da Groq.") from error

    except APIStatusError as error:
        raise RuntimeError(
            f"A API da Groq retornou um erro HTTP: {error.status_code}."
        ) from error
