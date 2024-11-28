"""

Classes com a Biblioteca Schedule
Exercício 1:
Crie uma classe Tarefa que imprime uma mensagem na tela a cada 10 segundos usando a biblioteca schedule.

Exercício 2:
Modifique a classe Tarefa para que ela aceite uma função como parâmetro, permitindo que você agende diferentes tipos de tarefas.

Exercício 3:
Implemente uma classe Agendador que receba várias tarefas e execute-as de acordo com um intervalo específico. 
Use a biblioteca schedule para agendar as tarefas.

Exercício 4:
Crie uma classe TarefaComHoraEspecifica que execute uma tarefa em um horário fixo. Por exemplo, execute uma tarefa às 14:00 horas todos os dias.

Desafio:
Implemente um sistema de agendamento que leia tarefas de um arquivo de texto e as agende automaticamente. 
Use a biblioteca schedule para executar essas tarefas periodicamente.


"""
import schedule
import time
from loguru import logger
import threading
import re

class Tarefa:
    """
    Classe base para agendar tarefas simples que exibem uma mensagem.
    """
    def __init__(self, mensagem: str = "Executando a tarefa...", intervalo: int = 10):
        """
        Inicializa a tarefa.

        Args:
            mensagem (str): Mensagem a ser exibida durante a execução da tarefa.
            intervalo (int): Intervalo de tempo, em segundos, para repetir a tarefa.
        """
        self.mensagem = mensagem
        self.intervalo = intervalo
        logger.add('data/tarefa_agendada.log', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

        schedule.every(self.intervalo).seconds.do(self.imprimir_mensagem)

    def imprimir_mensagem(self):
        """Executa a tarefa agendada."""
        logger.info(self.mensagem)
        logger.info(f"Início da tarefa agendada para executar a cada {self.intervalo} segundos.")
        logger.info('Tarefa agendada concluída.')

    @staticmethod
    def start_scheduler():
        """Executa o agendador em um loop contínuo."""
        logger.info("Iniciando o agendador...")
        while True:
            schedule.run_pending()
            time.sleep(0.1)


class TarefaComFuncao:
    """
    Classe que permite agendar uma função personalizada.
    """
    def __init__(self, funcao, intervalo: int = 10, *args, **kwargs):
        """
        Inicializa a tarefa personalizada.

        Args:
            funcao (callable): Função a ser executada periodicamente.
            intervalo (int): Intervalo de tempo, em segundos, para repetir a tarefa.
            *args: Argumentos posicionais para a função.
            **kwargs: Argumentos nomeados para a função.
        """
        if not callable(funcao):
            raise ValueError("O parâmetro 'funcao' deve ser uma função ou callable.")

        self.funcao = funcao
        self.intervalo = intervalo
        self.args = args
        self.kwargs = kwargs

        schedule.every(self.intervalo).seconds.do(self.executar_funcao)

    def executar_funcao(self):
        """Executa a função personalizada."""
        logger.info(f"Executando a função: {self.funcao.__name__}")
        self.funcao(*self.args, **self.kwargs)
        logger.info(f"Função {self.funcao.__name__} concluída.")


# Exercicio 3
class Agendador:
    """
    Classe que permite agendar diversas tarefas.
    """
    def __init__(self):
        self.tarefas = []
        logger.add('data/agendador.log', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

    def adicionar_tarefa(self, tarefa, intervalo, *args, **kwargs):
        """
        Adiciona uma nova tarefa ao agendador.

        Args:
            funcao (callable): Função que será executada periodicamente.
            intervalo (int): Intervalo em segundos para executar a função.
            *args: Argumentos posicionais para a função.
            **kwargs: Argumentos nomeados para a função.
        """
        if not callable(tarefa):
            raise ValueError("O parâmetro 'tarefa' deve ser uma função ou callable.")

        logger.info(f'Agendando a tarefa: {tarefa.__name__} para executar a cada {intervalo} segundos.')
        schedule.every(intervalo).seconds.do(tarefa, *args, **kwargs)
        self.tarefas.append(tarefa)

    def iniciar(self):
        """
        Inicia o loop do agendador em threading.
        """
        logger.info("Iniciando o agendador...")
        threading.Thread(target=self._run_scheduler, daemon=True).start()

    @staticmethod
    def _run_scheduler():
        """
        Inicia o loop do agendador.
        """
        while True: 
            schedule.run_pending()
            time.sleep(0.1)


# Exercicio 4
class TarefaComHoraEspecifica:
    """
    Classe que permite agendar uma função para executar em um horário específico.
    """
    def __init__(self, funcao, horario, *args, **kwargs):
        """
        Inicializa a tarefa com o horário e função especificados.

        Args:
            funcao (callable): Função a ser executada.
            horario (str): Horário no formato "HH:MM" para executar a função.
            *args: Argumentos posicionais para a função.
            **kwargs: Argumentos nomeados para a função.
        """       
        logger.add('data/tarefa_hora_especifica_agendada.log', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
        
        if not callable(funcao):
            raise ValueError("O parâmetro 'funcao' deve ser uma função ou callable.")
        
        if not self._validar_horario(horario):
            raise ValueError("O parâmetro 'horario' deve ser uma string no formato 'HH:MM'.")

        self.funcao = funcao
        self.horario = horario
        self.args = args
        self.kwargs = kwargs

        schedule.every().day.at(self.horario).do(self.executar_funcao)
        logger.info(f"Agendando a tarefa {self.funcao.__name__} para executar na hora especificada: {self.horario}")

    def _validar_horario(self, horario) -> bool:
        return bool(re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', horario))

    def executar_funcao(self):
        """
        Executa a função agendada.
        """
        logger.info(f"Executando a função: {self.funcao.__name__}")
        self.funcao(*self.args, **self.kwargs)
        logger.info(f"Função {self.funcao.__name__} concluída.")


if __name__ == "__main__":

    # tarefa_simples = Tarefa(mensagem="Minha tarefa padrão está rodando!", intervalo=5)

    # def tarefa_personalizada(nome):
    #     logger.debug(f"Olá, {nome}! Esta é uma tarefa personalizada.")
    #     return nome

    # tarefa_funcao = TarefaComFuncao(funcao=tarefa_personalizada, intervalo=10, nome="Mundo")

    # scheduler_thread = threading.Thread(target=Tarefa.start_scheduler, daemon=True)
    # scheduler_thread.start()

    # logger.info("Agendador iniciado.")

    # try:
    #     while True:
    #         time.sleep(1)

    # except KeyboardInterrupt:
    #     logger.warning("Encerrando o programa...")

    # def tarefa1():
    #     logger.info("Executando a primeira tarefa...")

    # def tarefa2(nome):
    #     logger.info(f"Executando a segunda tarefa...{nome}")

    # agendador = Agendador()
    # agendador.adicionar_tarefa(tarefa1, 5)
    # agendador.adicionar_tarefa(tarefa2, 10, 'seu bobo')
    # agendador.iniciar()

    # try:
    #     while True:
    #         time.sleep(1)

    # except KeyboardInterrupt:
    #     logger.warning("Encerrando o programa...")

    from datetime import datetime

    def minha_tarefa():
        logger.info(f"Executando a primeira tarefa... horario atual: {datetime.now()}") 
    
    try:
        tarefa = TarefaComHoraEspecifica(minha_tarefa, '23:40')
        logger.info('Iniciando o agendador...')

        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        logger.warning("Encerrando o programa...")