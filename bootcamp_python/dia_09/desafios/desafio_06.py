"""
Desafio 6: Monitoramento em Real-Time

Você deseja monitorar o desempenho de um script em tempo real, exibindo os logs no console e salvando-os em um arquivo.

Tarefas:

1. Escreva um script que execute uma tarefa longa (ex: loop com cálculos matemáticos).
2. Configure o Loguru para:
    - Exibir logs no console.
    - Salvar logs em um arquivo.
3. Adicione logs para indicar o progresso e o tempo estimado restante.

Requisitos:

- Use níveis de log diferentes (INFO, DEBUG, etc.).
- Adicione logs ricos com o nome do arquivo, linha e função de onde o log foi gerado.

Dicas:

- Use variáveis nos logs para indicar progresso (% concluído).

"""

import time
import random
from datetime import datetime
from loguru import logger

logger.add('desafio_06.log',
           format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
           rotation='1 MB')

def tarefa_longa(iteracoes:int=1000) -> None:
    inicio = time.time()

    for i in range(1, iteracoes + 1):
        _ = random.random() * i * 2.5
        progresso = (i / iteracoes) * 100

        tempo_passado = time.time() - inicio
        tempo_estimado = (tempo_passado / i) * (iteracoes - i) if i> 0 else 0

        if i % (iteracoes // 20) == 0:
            logger.info(f"Progresso: {progresso:.2f}%, Tempo estimado restante: {tempo_estimado:.2f} segundos")

        logger.debug(f'Iteração {i}/{iteracoes} - tempo decorrido: {tempo_passado:.2f}s')
        time.sleep(0.01)
    
    tempo_total = time.time() - inicio
    logger.info(f'Tarefa concluida em {tempo_total:.2f} segundos')

def main() -> None:
    logger.info('Iniciando tarefa longa...')
    tarefa_longa(1000)
    logger.info('Tarefa longa concluida.')


if __name__ == '__main__':
    main()