from groq import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    Groq,
    RateLimitError,
)

from .config import load_api_key

MODEL = "openai/gpt-oss-120b"
TIMEOUT_SECONDS = 30.0


SYSTEM_PROMPT = """
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


def _validate_text(text: str) -> None:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("O texto não pode estar vazio.")


def _prepare_request(text: str) -> dict:
    return {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        "temperature": 0.2,
        "max_completion_tokens": 1024,
    }


def _create_client() -> Groq:
    return Groq(api_key=load_api_key(), timeout=TIMEOUT_SECONDS)


def _call_model(client: Groq, request: dict):
    try:
        return client.chat.completions.create(**request)
    except APITimeoutError as error:
        raise RuntimeError(
            "A solicitação excedeu o tempo limite. Tente novamente."
        ) from error
    except AuthenticationError as error:
        raise RuntimeError(
            "A credencial da API é inválida ou não tem autorização."
        ) from error
    except RateLimitError as error:
        raise RuntimeError(
            "O limite de solicitações da API foi atingido. Tente novamente mais tarde."
        ) from error
    except APIConnectionError as error:
        raise RuntimeError(
            "Falha de comunicação com a API da Groq. Verifique sua conexão."
        ) from error
    except APIStatusError as error:
        if error.status_code == 404:
            message = (
                "O modelo de linguagem escolhido está indisponível ou não foi encontrado."
            )
        elif error.status_code >= 500:
            message = "O serviço da Groq está temporariamente indisponível."
        else:
            message = (
                f"A API da Groq rejeitou a solicitação (HTTP {error.status_code})."
            )
        raise RuntimeError(message) from error


def _process_response(response: object) -> str:
    choices = getattr(response, "choices", None)
    if not isinstance(choices, (list, tuple)) or not choices:
        raise RuntimeError(
            "O modelo retornou uma resposta em formato inesperado."
        )

    message = getattr(choices[0], "message", None)
    content = getattr(message, "content", None)
    if not isinstance(content, str):
        raise RuntimeError(
            "O modelo retornou uma resposta em formato inesperado."
        )

    result = content.strip()
    if not result:
        raise RuntimeError("O modelo retornou uma resposta vazia.")
    return result


def correct_text(text: str, client: Groq | None = None) -> str:
    """Valida o texto, solicita a correção ao modelo e processa a resposta."""
    _validate_text(text)

    request = _prepare_request(text)
    active_client = client if client is not None else _create_client()
    response = _call_model(active_client, request)
    return _process_response(response)
