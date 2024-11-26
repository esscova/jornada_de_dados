"""

Desafio 3: Depuração de Modelo de Machine Learning
Você está treinando um modelo de machine learning e deseja acompanhar:

O progresso de cada época.
Métricas de performance (ex: perda e acurácia).
Possíveis erros durante o treinamento.
Tarefas:

[X] Simule o treinamento de um modelo (por exemplo, ajuste um modelo simples com um loop for).
Registre:
[X] Início e término de cada época.
[X] Valores de perda e acurácia em cada época.
[X] Tempo de treinamento total.
Introduza um erro em uma época específica (ex: divisão por zero ou índice fora do intervalo) e registre o erro no log.
Requisitos:

Use logger.info para progresso e métricas.
Configure um arquivo de log para salvar todas as mensagens de treinamento.
Dicas:

Utilize bibliotecas como time para medir o tempo de execução de cada época.

"""

import time
from loguru import logger

def simular_metricas(epoch):
    perda=max(0.1,1.0/(1+epoch))
    acuracia=min(100, epoch*10 + 50)
    return perda, acuracia


def treinar_modelo():
    logger.add('treinamento.log', format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")
    logger.info("Iniciando treinamento...")
    start_time = time.time()

    try:
        for epoch in range(10):
            logger.info(f"Epoca {epoch + 1} iniciada.")

            try:
                if epoch == 5:
                    raise ValueError("Erro ao treinar o modelo - índice fora do intervalo.")

                percas, acuracias = simular_metricas(epoch)
                time.sleep(1)

                logger.info(f"Perda: {percas}")
                logger.info(f"Acuracia: {acuracias} %")
            except Exception as e:
                logger.error(f'Erro na epoca {epoch + 1}: {e}') 
                continue

            logger.info(f"Epoca {epoch + 1} concluida.")

    except Exception as e:
        logger.critical(f'Erro crítico durante o treinamento: {e}')

    end_time = time.time()
    total_time = end_time - start_time
    logger.info(f"Treinamento concluido em {total_time:.2f} segundos.")

    logger.info("Fim do treinamento.")

def main():
    treinar_modelo()

if __name__ == "__main__":
    main()