"""

descrição: exercicios de fixação, dia 03 bootcamp python
autor: wellington moreira

"""

class Exercicio:
    def __init__(self):
        self.title = 'Exercicios de fixação'
    
    titulo_01:str = """
Exercício 1: Verificação de Qualidade de Dados

Você está analisando um conjunto de dados de vendas e precisa garantir 
que todos os registros tenham valores positivos para `quantidade` e `preço`. 
Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
forem positivos ou "Dados inválidos" caso contrário.
    """

    titulo_02:str = """
Exercício 2: Classificação de Dados de Sensor

Imagine que você está trabalhando com dados de sensores IoT. 
Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
de temperatura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'

    """

    titulo_03:str = """"
Exercício 3: Filtragem de Logs por Severidade

Você está analisando logs de uma aplicação e precisa filtrar mensagens 
com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
escreva um programa que imprima a mensagem se a severidade for 'ERROR'.    
    """

    titulo_04:str = """
Exercício 4: Validação de Dados de Entrada

Antes de processar os dados de usuários em um sistema de recomendação, 
você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
fornecido um email válido. Escreva um programa que valide essas condições 
e imprima "Dados de usuário válidos" ou o erro específico encontrado.
    """

    titulo_05:str = """
Exercício 5: Detecção de Anomalias em Dados de Transações

Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.    
    """

    titulo_06:str = """
Exercício 6. Contagem de Palavras em Textos
Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
    """

    titulo_07:str = """
Exercício 7. Normalização de Dados
Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
    """

    titulo_08:str = """
Exercício 8. Filtragem de Dados Faltantes
Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
    """

    titulo_09:str = """
Exercício 9. Extração de Subconjuntos de Dados
Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.
    """

    titulo_10:str = """
 Exercício 10. Agregação de Dados por Categoria
 Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
    """

    def exercicio_01(self:str) -> None:
        print(self.titulo01)
        try:
            
            quantidade:float = float(input('Digite a quantidade: ').strip().replace(',', '.'))
            preco:float = float(input('Digite o preco: R$ ').strip().replace(',', '.'))

            if not isinstance(quantidade, float) and not isinstance(preco, float):
                raise TypeError('Entrada inválida')

            if quantidade > 0 and preco > 0:
                print('Dados validos')
            else:
                print('Dados invalidos')

        except ValueError:
            print('Tem que ser um numero')

    def exercicio_02(self:str) -> None:
        print(self.titulo_02)
        try:
            temperatura:float = float(input('Digite a temperatura: ').strip().replace(',', '.'))

            if not isinstance(temperatura, float):
                raise TypeError('Entrada inválida')

            if temperatura < 18:
                print('Baixa')
            elif temperatura >= 18 and temperatura <= 26:
                print('Normal')
            else:
                print('Alta')
        except ValueError:
            print('Tem que ser um numero')

    def exercicio_03(self:str) -> None:
        print(self.titulo_03)
        try:
            log:dict = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
        
            if log['level'] == 'ERROR':
                print(f'Erro tipo: {log["message"]} em {log["timestamp"]}')

        except ValueError:
            print('Erro na obtencao do log')

    def exercicio_04(self:str) -> None:
        print(self.titulo_04)
        try:
            email:str = input('Digite o email: ').strip()

            while True:
                try:
                    idade:int = int(input('Digite a idade: '))
                    break
                except ValueError:
                    print('Tem que ser um numero')
            

            if not isinstance(email, str):
                raise TypeError('Entrada inválida')
            
            if idade == '' or email == '':
                raise ValueError('Digite uma idade e um email')
            
            if not isinstance(idade, int):
                raise TypeError('Entrada inválida')

            email_split:list = email.split('@')

            if len(email_split) != 2:
                raise ValueError('Email inválido, campo email com mais de um @')
            
            if email_split[0] == '' or email_split[1] == '':
                raise ValueError('Email inválido, campo email vazio')
            
            if '.' not in email_split[1]:
                raise ValueError('Email inválido, campo email sem domínio')
            
            if '@' not in email:
                raise ValueError('Email inválido, campo domínio sem @')
            
            if len(email_split[0]) > 100 or len(email_split[1]) > 100:
                raise ValueError('Email inválido, campo email ou domínio muito longo')
            
            if len(email_split[0]) < 3 or len(email_split[1]) < 3:
                raise ValueError('Email inválido, campo email ou domínio muito curto')
            
            if idade < 18 or idade > 65:
                raise ValueError('Idade inválida')

            print(f'Dados de usuário validos - idade: {idade}, email: {email}')

        except ValueError as e:
            print(e)

    def exercicio_05(self:str) -> None:
        print(self.titulo_05)
        try:
            transacao:dict = {'valor': 12000, 'hora': 20}

            if not isinstance(transacao, dict):
                raise TypeError('Entrada inválida')
                      
            if transacao['hora'] < 9 or transacao['hora'] > 18 or transacao['valor'] > 10000:
                print('Transação suspeita')

        except ValueError:
            print('Erro na obtencao da transação')

    def exercicio_06(self:str) -> None:
        print(self.titulo_06)
        try:
            texto:str = input('Digite o texto: ').strip().lower().replace(',''', '').replace('.', '')

            if not isinstance(texto, str):
                raise TypeError('Entrada inválida, digite um texto')

            palavras:list = texto.split()

            resultado:dict = {
                palavra: palavras.count(palavra) for palavra in set(palavras)
            }
            
            for palavra, quantidade in resultado.items():
                print(f'{palavra}: {quantidade}')

        except ValueError:
            print('Erro na obtencao do texto')

    def exercicio_07(self:str) -> None:
        print(self.titulo_07)
        try:
            while True:
                try:
                    lista_numeros = [ 
                        int(num) for num in input('Digite uma lista de números separados por espaços: ').split(' ') if len(num)>0 
                        ]
                    break
                except ValueError:
                    print('Entrada inválida, digite uma lista de números')

            menor_valor = min(lista_numeros)
            maior_valor = max(lista_numeros)

            normalizados = [
                (x - menor_valor) / (maior_valor - menor_valor) for x in lista_numeros
            ]

            print(f'Valores normalizados: \n{normalizados}')

            
        except ValueError:
            print('Erro na obtencao dos números')

    def exercicio_08(self:str) -> None:
        print(self.titulo_08)
        try:
            usuarios:list = [
                {'nome': 'João', 'idade': 25, 'cidade': ''},
                {'nome': 'Maria', 'idade': 10, 'cidade': 'Rio de Janeiro'},
                {'nome': 'Pedro', 'idade': 35, 'cidade': 'Belo Horizonte'},
                {'nome': 'Ana', 'idade': 40, 'cidade': ''},
                {'nome': 'Lucas', 'idade': 45, 'cidade': 'Curitiba'},
                {'nome': 'Julia', 'idade': 50, 'cidade': 'Recife'},
                {'nome': 'Carlos', 'idade': 15, 'cidade': 'Salvador'},
                {'nome': 'Mariana', 'idade': 60, 'cidade': ''},
                {'nome': 'Gabriel', 'idade': 15, 'cidade': 'Porto Alegre'}
            ]

            print('Usuários cadastrados:')
            for usuario in usuarios:
                print(f'Nome: {usuario["nome"]}, Idade: {usuario["idade"]}, Cidade: {usuario["cidade"]}')

            usuarios_validos:list = [usuario for usuario in usuarios if usuario['cidade'] != '']

            print('\nUsuários válidos com cidade cadastrada:')
            for usuario in usuarios_validos:
                print(f'Nome: {usuario["nome"]}, Idade: {usuario["idade"]}, Cidade: {usuario["cidade"]}')

        except ValueError:
            print('Erro na execução, tente novamente.')

    def exercicio_09(self:str) -> None:
        print(self.titulo_09)
        try:
            while True:
                try:
                    lista_numeros:list = [ 
                        int(num) for num in input('Digite uma lista de números separados por espaços: ').split(' ') if len(num)>0 
                        ]
                    break
                except ValueError:
                    print('Entrada inválida, digite uma lista de números')

            pares:list = [num for num in lista_numeros if num % 2 == 0]
            print(f'Números pares: {pares}')

        except ValueError:
            print('Erro na obtencao dos números')

    def exercicio_10(self:str) -> None:
        print(self.titulo_10)
        try:
            vendas:list = [
                {'produto': 'Produto A', 'categoria': 'Categoria 1', 'preco': 10.99},
                {'produto': 'Produto B', 'categoria': 'Categoria 2', 'preco': 19.99},
                {'produto': 'Produto C', 'categoria': 'Categoria 1', 'preco': 5.99},
                {'produto': 'Produto D', 'categoria': 'Categoria 2', 'preco': 29.99},
                {'produto': 'Produto E', 'categoria': 'Categoria 1', 'preco': 15.99},
                {'produto': 'Produto F', 'categoria': 'Categoria 2', 'preco': 9.99},
                {'produto': 'Produto G', 'categoria': 'Categoria 1', 'preco': 12.99},
                {'produto': 'Produto H', 'categoria': 'Categoria 2', 'preco': 24.99},
                {'produto': 'Produto I', 'categoria': 'Categoria 1', 'preco': 8.99},
                {'produto': 'Produto J', 'categoria': 'Categoria 2', 'preco': 16.99}
            ]

            print('Produtos vendidos:')
            for venda in vendas:
                print(f'Produto: {venda["produto"]}, Categoria: {venda["categoria"]}, Preço: {venda["preco"]}')            

            vendas_categoria_1:list = [venda for venda in vendas if venda['categoria'] == 'Categoria 1']
            total_categoria_1 = sum([venda['preco'] for venda in vendas_categoria_1])

            vendas_categoria_2:list = [venda for venda in vendas if venda['categoria'] == 'Categoria 2']
            total_categoria_2 = sum([venda['preco'] for venda in vendas_categoria_2])

            print('\nTotal vendido por categoria:')
            print(f'Total vendido na categoria 1: R$ {total_categoria_1:.2f}')
            print(f'Total vendido na categoria 2: R$ {total_categoria_2:.2f}')

        except ValueError:
            print('Erro na obtencao dos números')

if __name__ == '__main__':
    exercicio = Exercicio()
    exercicio.exercicio_10()