
from corretor import correct_text

texto = "Os alunos foram para a escola ontem."

try:
    resultado = correct_text(texto)
    print(resultado)

except (ValueError, RuntimeError) as error:
    print(f"\nErro: {error}")
