"""

descricao: Desafio - Refatorar o projeto da aula anterior evitando Bugs!
autor: wellington moreira

"""
# Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante e prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente. Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que os valores sejam positivos.
def verifica_string(string:str) -> str:
    if len(string) == 0:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in string):
        raise ValueError("O nome não deve conter números.")
    else:
        return string

def verifica_valor(valor:float, tipo:str) -> float:
    if valor < 0:
        raise ValueError(f"O {tipo} deve ser um valor positivo.")
    else:
        return valor

def desafio_02():

    try:
        nome = input("Digite seu nome: ")
        verifica_string(nome)

    except ValueError as e:
        print(e)
        exit()

    try:
        salario = float(input("Digite o valor do seu salário: ").strip().replace(',', '.'))
        verifica_valor(salario, 'salário')

    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")
        exit()

    try:
        bonus = float(input("Digite o valor do bônus recebido: ").strip().replace(',', '.'))
        verifica_valor(bonus, 'bônus')

    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
        exit()

    bonus_recebido = 1000 + salario * bonus  

    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")


if __name__ == "__main__":
    desafio_02()