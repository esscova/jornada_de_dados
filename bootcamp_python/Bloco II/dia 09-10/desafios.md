# Bootcamp Python

### **Desafio 1: Monitoramento de um Pipeline de ETL**

Você precisa monitorar um pipeline de ETL que processa múltiplos arquivos CSV e os consolida em um único arquivo. Adicione logs para acompanhar o progresso do pipeline, identificar erros e registrar o tempo total de execução.

**Tarefas:**

1. Leia três arquivos CSV fictícios, combine-os em um único DataFrame e salve o resultado.
2. Adicione logs para:
    - Registrar o início e o término de cada etapa.
    - Capturar exceções, como arquivos ausentes ou problemas de leitura.
    - Registrar o tempo total de execução.

**Requisitos:**

- Use rotação de arquivos de log baseada no tamanho (ex: 1 MB).
- Retenha logs apenas por 7 dias.

**Dicas:**

- Use `logger.add()` para configurar a rotação e retenção de logs.
- Utilize `try/except` com `logger.exception` para capturar erros.



### **Desafio 2: Rastreamento de Erros em Transformações de Dados**

Você está processando um DataFrame com transformações complexas (normalização de colunas, preenchimento de valores ausentes, etc.). Às vezes, erros ocorrem em determinadas etapas, mas você não sabe onde exatamente.

**Tarefas:**

1. Crie um DataFrame fictício com valores ausentes e dados inconsistentes.
2. Aplique as seguintes transformações:
    - Preencha valores ausentes com a média da coluna.
    - Normalize os valores entre 0 e 1.
    - Converta uma coluna de strings para números inteiros.
3. Adicione logs para identificar o início e término de cada transformação.
4. Registre erros específicos com rastreamento completo da pilha.

**Requisitos:**

- Use `@logger.catch` para capturar erros em funções específicas.
- Adicione variáveis no log para indicar o número de linhas processadas antes de cada etapa.

**Dicas:**

- Experimente introduzir erros propositais, como valores inválidos, para testar os logs.


### **Desafio 3: Depuração de Modelo de Machine Learning**

Você está treinando um modelo de machine learning e deseja acompanhar:

- O progresso de cada época.
- Métricas de performance (ex: perda e acurácia).
- Possíveis erros durante o treinamento.

**Tarefas:**

1. Simule o treinamento de um modelo (por exemplo, ajuste um modelo simples com um loop `for`).
2. Registre:
    - Início e término de cada época.
    - Valores de perda e acurácia em cada época.
    - Tempo de treinamento total.
3. Introduza um erro em uma época específica (ex: divisão por zero ou índice fora do intervalo) e registre o erro no log.

**Requisitos:**

- Use `logger.info` para progresso e métricas.
- Configure um arquivo de log para salvar todas as mensagens de treinamento.

**Dicas:**

- Utilize bibliotecas como `time` para medir o tempo de execução de cada época.


### **Desafio 4: Integração com `pandas`**

Você está trabalhando em um relatório que carrega, limpa e exporta dados usando a biblioteca `pandas`. O objetivo é monitorar cada etapa e capturar qualquer erro gerado pelo `pandas`.

**Tarefas:**

1. Carregue um arquivo CSV fictício, aplique as seguintes etapas de limpeza:
    - Remova colunas duplicadas.
    - Renomeie colunas.
    - Elimine linhas com valores ausentes.
2. Integre os logs do `pandas` ao Loguru para capturar qualquer erro gerado.
3. Registre o progresso e os resultados da limpeza:
    - Número de linhas e colunas antes e depois da limpeza.
    - Tempo total de execução.

**Requisitos:**

- Implemente um `InterceptHandler` para redirecionar os logs do `pandas`.
- Adicione logs detalhados antes e depois de cada etapa de limpeza.

**Dicas:**

- Use `logger.debug` para registrar informações detalhadas (ex: DataFrame.head()).


### **Desafio 5: Logs Personalizados para Testes A/B**

Você está conduzindo um teste A/B para comparar duas estratégias de recomendação de produtos. Os resultados estão sendo registrados em logs, e você deseja analisar:

- Qual estratégia teve melhor performance.
- Quais erros ocorreram durante a coleta de dados.

**Tarefas:**

1. Simule resultados de duas estratégias (ex: "A" e "B") com métricas como taxa de conversão e número de cliques.
2. Registre os resultados de cada estratégia em logs.
3. Capture possíveis erros, como métricas ausentes ou valores fora do intervalo esperado.
4. Personalize os logs com formato específico, incluindo:
    - Estratégia testada.
    - Métricas coletadas.
    - Timestamp.

**Requisitos:**

- Use um formato de log personalizado com `logger.add()`.
- Adicione logs informativos para cada nova coleta de métricas.

**Dicas:**

- Experimente gerar saídas de log em JSON para facilitar a análise automatizada.


### **Desafio 6: Monitoramento em Real-Time**

Você deseja monitorar o desempenho de um script em tempo real, exibindo os logs no console e salvando-os em um arquivo.

**Tarefas:**

1. Escreva um script que execute uma tarefa longa (ex: loop com cálculos matemáticos).
2. Configure o Loguru para:
    - Exibir logs no console.
    - Salvar logs em um arquivo.
3. Adicione logs para indicar o progresso e o tempo estimado restante.

**Requisitos:**

- Use níveis de log diferentes (`INFO`, `DEBUG`, etc.).
- Adicione logs ricos com o nome do arquivo, linha e função de onde o log foi gerado.

**Dicas:**

- Use variáveis nos logs para indicar progresso (% concluído).
