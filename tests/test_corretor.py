import pytest

from unittest.mock import Mock
from src.corretor import correct_text


def test_empty_text():
    with pytest.raises(ValueError):
        correct_text("")


def test_only_spaces():
    with pytest.raises(ValueError):
        correct_text("   ")


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


def test_empty_api_key(monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="GROQ_API_KEY"):
        correct_text("Texto para correção.")


def test_connection_error():
    from groq import APIConnectionError

    client = Mock()
    client.chat.completions.create.side_effect = APIConnectionError(
        request=Mock()
    )

    with pytest.raises(RuntimeError, match="conectar à API"):
        correct_text("Texto para correção.", client=client)
