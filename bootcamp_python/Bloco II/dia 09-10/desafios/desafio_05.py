"""
Desafio 5: Logs Personalizados para Testes A/B
Você está conduzindo um teste A/B para comparar duas estratégias de recomendação de produtos. 
Os resultados estão sendo registrados em logs, e você deseja analisar:

Qual estratégia teve melhor performance?
Quais erros ocorreram durante a coleta de dados?

Tarefas:

[X] Simule resultados de duas estratégias (ex: "A" e "B") com métricas como taxa de conversão e número de cliques.
[X] Registre os resultados de cada estratégia em logs.
[X] Capture possíveis erros, como métricas ausentes ou valores fora do intervalo esperado.
- Personalize os logs com formato específico, incluindo:
    - Estratégia testada.
    - Métricas coletadas.
    - Timestamp.

Requisitos:

Use um formato de log personalizado com logger.add().
Adicione logs informativos para cada nova coleta de métricas.

Dicas:
Experimente gerar saídas de log em JSON para facilitar a análise automatizada.

"""
import random
from loguru import logger
from datetime import datetime

logger.add(
    'logs.json',
    format='{time} | {level} | {message}',
    level='INFO',   
    rotation='1 MB', 
    compression='zip',
    serialize=True
)
def gerar_dados(tamanho:int=100) -> dict:
    return {
        "taxa de conversao": [round(random.random(), 2) for _ in range(tamanho)],
        "numero de cliques": [random.randint(0, 999) for _ in range(tamanho)]
    }

def main() -> None:

    testes:list[str] = ['A', 'B']
    metricas:list[str] = ['taxa de conversao', 'numero de cliques']

    resultados:list[dict] = [
        {
            'teste': estrategia,
            **gerar_dados()
        } for estrategia in testes
    ]

    for resultado in resultados:
        try:
            timestamp = datetime.now().isoformat()

            for metrica in metricas:
                if metrica not in resultado:
                    logger.error(
                        f'Métrica ausente na estratégia {resultado["teste"]}',
                        metrica_ausente=metrica,
                        estrategia=resultado["teste"],
                        timestamp=timestamp
                    )
                    raise KeyError(f'Métrica "{metrica}" ausente.')

            if len(resultado['taxa de conversao']) != len(resultado['numero de cliques']):
                logger.error(
                    f'Tamanho de dados inconsistentes na estratégia {resultado["teste"]}',
                    estrategia=resultado["teste"],
                    timestamp=timestamp
                )
                raise ValueError(f'Tamanho de dados inconsistentes na estratégia {resultado["teste"]}')
                
            taxas_invalidas:list = [taxa for taxa in resultado['taxa de conversao'] if not( 0.0 <= taxa <= 1.0)]
            if taxas_invalidas:
                logger.warning(
                    f"Valores inválidos encontrados na 'taxa de conversao' da estratégia {resultado['teste']}",
                    taxas_invalidas=taxas_invalidas,
                    estrategia=resultado["teste"],
                    timestamp=timestamp
                )

            cliques_invalidos:list = [clique for clique in resultado['numero de cliques'] if clique < 0]
            if cliques_invalidos:
                logger.warning(
                    f"Valores inválidos encontrados na 'numero de cliques' da estratégia {resultado['teste']}",
                    cliques_invalidos=cliques_invalidos,
                    estrategia=resultado["teste"],
                    timestamp=timestamp
                )

            logger.info(
                f"Resultados da estratégia {resultado['teste']}",
                estrategia=resultado["teste"],
                timestamp=timestamp,
                metricas_coletadas={
                    "taxa de conversao": resultado['taxa de conversao'],
                    "numero de cliques": resultado['numero de cliques']
                }
            )

        except KeyError as e:
            logger.error(
                f"Erro crítico ao processar os resultados: {e}",
                estrategia=resultado.get("teste", "Desconhecida"),
                timestamp=timestamp
            )
        except Exception as e:
            logger.error(
                f"Erro inesperado ao processar os resultados: {e}",
                estrategia=resultado.get("teste", "Desconhecida"),
                timestamp=timestamp
            )


if __name__ == '__main__':
    main()