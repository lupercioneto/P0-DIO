from .corretor import correct_text


def capture_input() -> str:
    return input("\nDigite o texto que deseja corrigir:\n\n> ")


def present_result(result: str) -> None:
    print("\n" + result)


def main() -> None:
    try:
        text = capture_input()
        print("\nProcessando...")
        result = correct_text(text)
        present_result(result)

    except ValueError as error:
        print(f"\nEntrada inválida: {error}")

    except RuntimeError as error:
        print(f"\nErro ao realizar a correção: {error}")

    except EOFError:
        print("\nEntrada encerrada antes do envio do texto.")

    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")


if __name__ == "__main__":
    main()
