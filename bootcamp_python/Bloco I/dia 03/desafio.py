"""
descricao: dia 03 bootcamp python - refatorar o projeto da aula anterior com tratamento de erros e prevenção de bugs
autor: Wellington Moreira

"""

def verifica_string(string: str) -> str:
    if len(string) == 0:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in string):
        raise ValueError("O nome não deve conter números.")
    else:
        return string


def verifica_valor(valor: float, tipo: str) -> float:
    if valor < 0:
        raise ValueError(f"O {tipo} deve ser um valor positivo.")
    else:
        return valor


def desafio_03() -> None:

    nome_valido:bool = False
    salario_valido:bool = False
    bonus_valido:bool = False

    while not nome_valido:
        try:
            nome:str = input("Digite seu nome: ")
            nome = verifica_string(nome)
            print("Nome válido:", nome)
            nome_valido = True

        except ValueError as e:
            print(e)

    while not salario_valido:
        try:
            salario:float = float(input("Digite o valor do seu salário: ").strip().replace(',', '.'))
            salario = verifica_valor(salario, 'salário')
            salario_valido = True
        except ValueError as e:
            print(e)
            print("Por favor, digite um número válido para o salário.")

    while not bonus_valido:
        try:
            bonus:float = float(input("Digite o valor do bônus recebido: ").strip().replace(',', '.'))
            bonus = verifica_valor(bonus, 'bônus')
            bonus_valido = True
        except ValueError as e:
            print(e)
            print("Por favor, digite um número válido para o bônus.")

    bonus_recebido:float = 1000 + salario * bonus

    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")


if __name__ == "__main__":
    desafio_03()
