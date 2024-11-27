"""

descrição:
    - Desafio - Refatorar o projeto da aula anterior para que
        - seja possível cadastrar vários usuários e seus bônus
        - utilizar dicionários,
        - utilizar TypeHints e Funções

autor: 
    - wellington moreira
    - wsantos08@hotmail.com

versão python: 
    - 3.12.4

"""

from typing import Dict

# Desafio
def desafio_04() -> Dict[str, float]:
    def validar_string(string:str) -> str:
        if not string.strip():
            raise ValueError("Nome não pode estar vazio.")
        return string
    
    def validar_valor(valor:float) -> float:
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero.")
        return valor
    
    try:
        cadastrar:bool = True
        usuarios:list[Dict[str, float]] = []

        while cadastrar:
            opcao = input("Deseja cadastrar um novo usuário? (s/n): ")
            
            if opcao.lower() not in ['s', 'n']:
                raise ValueError("Opção inválida, tente novamente.")
                continue
            
            if opcao.lower() == 'n':
                cadastrar = False
                break

            nome_valido:bool = False
            salario_valido:bool = False
            bonus_valido:bool = False

            while not nome_valido:
                try:
                    nome:str = input("Digite seu nome: ")
                    nome = validar_string(nome)
                    print("Nome válido:", nome)
                    nome_valido = True

                except ValueError as e:
                    print(e)

            while not salario_valido:
                try:
                    salario:float = float(input("Digite o valor do seu salário: ").strip().replace(',', '.'))
                    salario = validar_valor(salario)
                    salario_valido = True
                except ValueError as e:
                    print(e)
                    print("Por favor, digite um número válido para o salário.")

            while not bonus_valido:
                try:
                    bonus:float = float(input("Digite o valor do bônus recebido: ").strip().replace(',', '.'))
                    bonus = validar_valor(bonus)
                    bonus_recebido:float = 1000 + salario * bonus
                    bonus_valido = True
                except ValueError as e:
                    print(e)
                    print("Por favor, digite um número válido para o bônus.")
            
            usuarios.append({
                'id': len(usuarios) + 1,
                'nome': nome,
                'salario': salario,
                'bonus_%': bonus,
                'bonus_recebido': bonus_recebido})
            
            print("Usuário cadastrado com sucesso.")

        print('\nResumo de usuários cadastrados:')
        for usuario in usuarios:
            print(f'ID: {usuario["id"]}, Nome: {usuario["nome"]}, Salário: {usuario["salario"]}, Bônus (%): {usuario["bonus_%"]}, Bônus Recebido: {usuario["bonus_recebido"]}')

        return usuarios
    
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    desafio_04()