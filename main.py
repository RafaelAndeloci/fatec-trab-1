from pathlib import Path
import runpy

diretorio_projeto = Path(__file__).resolve().parent


def executar_exercicios_1_e_2():
    """Executa os exercícios de inspeção e tratamento dos dados."""
    runpy.run_path(diretorio_projeto / "exercicio-2.py", run_name="__main__")


def executar_exercicios_3_e_4():
    """Executa os exercícios de agrupamento, agregação e visualização."""
    runpy.run_path(diretorio_projeto / "exercicio-3.py", run_name="__main__")


def main():
    executar_exercicios_1_e_2()
    executar_exercicios_3_e_4()


if __name__ == "__main__":
    main()
