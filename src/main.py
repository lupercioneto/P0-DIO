from corretor import correct_text


def main():

    try:
        text = input("\nDigite o texto que deseja corrigir:\n\n> ")

        print("\nProcessando...")

        result = correct_text(text)

        print("\n" + result)

    except ValueError as error:
        print(f"\nEntrada inválida: {error}")

    except RuntimeError as error:
        print(f"\nErro ao realizar a correção: {error}")

    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")


if __name__ == "__main__":
    main()
