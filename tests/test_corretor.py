from unittest.mock import Mock

import httpx
import pytest
from groq import APIConnectionError, APITimeoutError, AuthenticationError
from groq import NotFoundError, APIStatusError

from src.corretor import correct_text


@pytest.mark.parametrize("text", ["", "   ", "\t\n"])
def test_empty_text_is_rejected(text):
    with pytest.raises(ValueError, match="não pode estar vazio"):
        correct_text(text)


def test_success_correction():
    client = Mock()

    client.chat.completions.create.return_value.choices = [
        Mock(
            message=Mock(
                content="Os alunos foram para a escola ontem."
            )
        )
    ]

    resultado = correct_text(
        "Os alunos foi para escola ontem.",
        client=client
    )

    assert resultado == "Os alunos foram para a escola ontem."

    # Verifica se a API foi chamada
    client.chat.completions.create.assert_called_once()


def test_missing_api_key_is_reported_without_calling_model(monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="Credencial ausente"):
        correct_text("Texto para correção.")


def test_blank_api_key_is_reported(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "   ")
    with pytest.raises(RuntimeError, match="Credencial ausente"):
        correct_text("Texto para correção.")


def test_invalid_api_key_is_reported_without_exposing_credential(monkeypatch):
    secret = "fake-secret-that-must-not-be-shown"
    monkeypatch.setenv("GROQ_API_KEY", secret)
    client = Mock()
    response = httpx.Response(
        401, request=httpx.Request("POST", "https://api.groq.com")
    )
    client.chat.completions.create.side_effect = AuthenticationError(
        "Unauthorized", response=response, body=None
    )

    with pytest.raises(RuntimeError, match="credencial da API é inválida") as error:
        correct_text("Texto para correção.", client=client)

    assert secret not in str(error.value)


def test_connection_error_is_reported():
    client = Mock()
    client.chat.completions.create.side_effect = APIConnectionError(
        request=httpx.Request("POST", "https://api.groq.com")
    )

    with pytest.raises(RuntimeError, match="Falha de comunicação"):
        correct_text("Texto para correção.", client=client)


def test_timeout_is_reported():
    client = Mock()
    client.chat.completions.create.side_effect = APITimeoutError(
        request=httpx.Request("POST", "https://api.groq.com")
    )

    with pytest.raises(RuntimeError, match="tempo limite"):
        correct_text("Texto para correção.", client=client)


def test_unavailable_model_is_reported():
    client = Mock()
    response = httpx.Response(
        404, request=httpx.Request("POST", "https://api.groq.com")
    )
    client.chat.completions.create.side_effect = NotFoundError(
        "Model not found", response=response, body=None
    )

    with pytest.raises(RuntimeError, match="modelo de linguagem escolhido"):
        correct_text("Texto para correção.", client=client)


def test_service_unavailable_is_reported():
    client = Mock()
    response = httpx.Response(
        503, request=httpx.Request("POST", "https://api.groq.com")
    )
    client.chat.completions.create.side_effect = APIStatusError(
        "Service unavailable", response=response, body=None
    )

    with pytest.raises(RuntimeError, match="temporariamente indisponível"):
        correct_text("Texto para correção.", client=client)


@pytest.mark.parametrize(
    "response",
    [
        Mock(choices=[]),
        Mock(choices=[Mock(message=Mock(content=None))]),
        Mock(choices=[Mock(message=Mock(content="   "))]),
        Mock(),
    ],
)
def test_invalid_or_empty_model_response_is_reported(response):
    client = Mock()
    client.chat.completions.create.return_value = response

    with pytest.raises(RuntimeError, match="resposta"):
        correct_text("Texto para correção.", client=client)
