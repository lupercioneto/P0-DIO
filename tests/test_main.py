from unittest.mock import Mock

from src.main import main


def test_main_reports_end_of_input(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", Mock(side_effect=EOFError))

    main()

    assert "Entrada encerrada antes do envio" in capsys.readouterr().out
