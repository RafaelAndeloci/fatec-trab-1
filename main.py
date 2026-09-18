from pathlib import Path
import runpy

diretorio_projeto = Path(__file__).resolve().parent


def executar_exercicios_1():
    """Executa os exercícios de inspeção e tratamento dos dados."""
    print("===========================ETAPA 1===========================")
    runpy.run_path(diretorio_projeto / "exercicio-1.py", run_name="__main__")


def executar_exercicios_2():
    print("===========================ETAPA 2===========================")
    runpy.run_path(diretorio_projeto / "exercicio-2.py", run_name="__main__")


def executar_exercicios_3():
    print("===========================ETAPA 3===========================")
    runpy.run_path(diretorio_projeto / "exercicio-3.py", run_name="__main__")


def executar_exercicios_4():
    print("===========================ETAPA 4===========================")
    print("(Exibido na janela aberta)")
    runpy.run_path(diretorio_projeto / "exercicio-4.py", run_name="__main__")


def main():
    executar_exercicios_1()
    executar_exercicios_2()
    executar_exercicios_3()
    executar_exercicios_4()


if __name__ == "__main__":
    main()
