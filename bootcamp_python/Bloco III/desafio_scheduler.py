"""
Implementar um sistema de agendamento de tarefas utilizando a biblioteca schedule, 
onde as tarefas são lidas de um arquivo de texto e agendadas automaticamente, 

o fluxo do processo pode ser descrito em algumas etapas principais:

- Leitura do arquivo de texto: 
    O arquivo de texto conterá a lista de tarefas, seus horários e outros parâmetros de agendamento (como a periodicidade).

- Análise e interpretação do conteúdo do arquivo: 
    O formato do arquivo de texto deve ser consistente, de modo que o sistema consiga interpretá-lo corretamente e mapear as informações de cada tarefa.

- Agendamento com a biblioteca schedule: 
    Usar a biblioteca schedule para agendar as tarefas, de acordo com os parâmetros extraídos do arquivo de texto.

- Execução periódica das tarefas: 
    Configurar a execução periódica das tarefas de acordo com o agendamento.

"""

import schedule
import time
from loguru import logger

class SistemaTarefas:
    def __init__(self):
        self.tarefas:list = []
        logger.add('data/sistema_tarefas_agendadas.log', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

    def exemplo_tarefa(self, tarefa: str) -> None:
        logger.info(f"Executando tarefa: {tarefa}")

    def adicionar_tarefas_do_arquivo(self, tarefas_path: str='data/tarefas.txt') -> None:
        try:
            with open(tarefas_path, 'r') as file:
                for linha in file.readlines():
                    dados:list = linha.strip().split(',')
                    
                    logger.debug(f'dados: {dados}')

                    if len(dados) != 3:
                        logger.warning(f"Quantidade de parâmetros inválida: {len(dados)}")
                        continue

                    tarefa, horario, intervalo  = [item.strip() for item in dados]
                    logger.info(f"Tarefa: {tarefa}, Horário: {horario}, Intervalo: {intervalo}")
                    
                    self.agendar_tarefa(tarefa, horario, intervalo)
                    self.tarefas.append(tarefa)

        except FileNotFoundError:
            logger.error(f"Arquivo de tarefas nao encontrado: {tarefas_path}")
        except Exception as e:
            logger.error(f"Erro ao ler o arquivo de tarefas: {e}")

    def agendar_tarefa(self, tarefa: str, horario: str, intervalo: str) -> None:
            logger.info(f"Agendando tarefa: {tarefa}, Horário: {horario}, Intervalo: {intervalo}")

            if intervalo.lower() == 'diário':
                schedule.every().day.at(horario).do(self.exemplo_tarefa, tarefa)
            elif intervalo.lower() == 'semanal':
                schedule.every(7).days.at(horario).do(self.exemplo_tarefa, tarefa)
            elif intervalo.lower() == 'mensal':
                schedule.every(30).days.at(horario).do(self.exemplo_tarefa, tarefa)

            else:
                logger.warning(f"Intervalo de agendamento desconhecido: {intervalo}")


    def rodar_agendador(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    sistema = SistemaTarefas()
    sistema.adicionar_tarefas_do_arquivo()
    sistema.agendar_tarefa('Tarefa 1', '10:00', 'diário')
    try:
        sistema.rodar_agendador()
        logger.info("Agendador de tarefas iniciado.")
        logger.info("Pressione Ctrl+C para encerrar o agendador.")
        logger.info(f"Tarefas agendadas: {', '.join(sistema.tarefas)}")
    except KeyboardInterrupt:
        logger.warning("Agendador de tarefas encerrado.")