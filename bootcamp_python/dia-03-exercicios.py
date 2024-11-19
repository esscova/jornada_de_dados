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


if __name__ == '__main__':
    exercicio = Exercicio()
    exercicio.exercicio_05()