## Loguru
**Lista de exercícios progressivos** para você praticar e desenvolver suas habilidades com a biblioteca **Loguru** e a prática de **Decoradores**. Esses exercícios vão desde o básico até cenários avançados, cobrindo casos reais de uso para profissionais de dados e desenvolvedores.


### **Loguru**
---
#### **1. Primeiro Log**
Crie um script que registre mensagens de log nos níveis `INFO`, `WARNING` e `ERROR` diretamente no console.

**Objetivo:**
- Compreender os diferentes níveis de log.
- Experimentar os métodos `logger.info`, `logger.warning` e `logger.error`.


#### **2. Log em Arquivo**
Configure o Loguru para salvar os logs em um arquivo chamado `aplicacao.log`. Registre três mensagens com diferentes níveis de log.

**Objetivo:**
- Aprender a usar o método `logger.add` para salvar logs em arquivos.
- Familiarizar-se com a criação de arquivos de log.

#### **3. Formatação de Mensagens**
Personalize o formato do log para incluir a hora, o nível e a mensagem, com o seguinte modelo:  
`"{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"`.

**Objetivo:**
- Explorar o parâmetro `format` no método `logger.add`.
- Criar mensagens de log claras e legíveis.


#### **4. Rotação de Arquivos**
Configure o Loguru para rotacionar os arquivos de log quando eles atingirem 1 MB. Teste gerando mensagens de log até que a rotação ocorra.

**Objetivo:**
- Praticar o uso do parâmetro `rotation` para gerenciar tamanhos de arquivos.
- Compreender a rotação automática de arquivos.


#### **5. Capturando Exceções**
Use o decorador `@logger.catch` para registrar automaticamente qualquer exceção gerada por uma função que simula um erro (exemplo: divisão por zero).

**Objetivo:**
- Aprender a capturar e registrar rastreamentos completos de erros.
- Familiarizar-se com o decorador `@logger.catch`.

#### **6. Medindo Tempo de Execução**
Implemente um decorador personalizado para medir o tempo de execução de uma função e registre o tempo no log.

**Objetivo:**
- Criar decoradores personalizados.
- Usar o Loguru para registrar informações dinâmicas, como tempos de execução.


#### **7. Entrada e Saída de Funções**
Implemente um decorador que registre:
- Os argumentos de entrada de uma função.
- O resultado de saída.

Teste com uma função que soma dois números.

**Objetivo:**
- Criar logs úteis para depuração de funções.
- Registrar dados dinâmicos nos logs.


#### **8. Integração com `pandas`**
Crie um pipeline simples com `pandas` que:
1. Leia um arquivo CSV fictício.
2. Limpe os dados (ex: remova valores ausentes).
3. Renomeie colunas.
Registre cada etapa do pipeline com mensagens de log, incluindo o número de linhas e colunas antes e depois de cada transformação.

**Objetivo:**
- Usar logs para monitorar o progresso de pipelines de dados.
- Integrar Loguru em fluxos de trabalho de análise.


### **Decoradores**
---
#### **9. Criando um decorador**
Crie um decorador chamado minha_mensagem que imprime "Iniciando função..." antes de executar uma função e "Função concluída!" depois. Aplique este decorador a uma função chamada saudar, que recebe um nome como argumento e imprime "Olá, [nome]!".

Objetivo:
- Entender a estrutura básica de um decorador.
- Familiarizar-se com o conceito de wrapper.


#### **10. Decorador com Argumentos Dinâmicos**
Crie um decorador chamado log_entrada_saida que registra os argumentos de entrada e o valor de retorno de uma função. Aplique este decorador a uma função chamada soma, que recebe dois números e retorna sua soma.

Objetivo:
- Aprender a manipular *args e **kwargs no wrapper.
- Entender como registrar informações antes e depois da execução da função.


#### 11. Controle de Acesso
Crie um decorador chamado verificar_permissao que aceita como argumento um nome de usuário permitido. O decorador deve permitir a execução da função apenas se o usuário passado como argumento for o mesmo do permitido; caso contrário, deve levantar uma exceção PermissionError. Aplique o decorador a uma função chamada acessar_dados, que imprime "Acesso concedido".

Objetivo:
- Trabalhar com decoradores parametrizados.
- Implementar lógica condicional dentro do wrapper.

