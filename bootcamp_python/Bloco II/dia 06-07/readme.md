# Bootcamp Python
## Funções
As **funções** em programação são blocos de código que realizam uma tarefa específica e podem ser reutilizados em diferentes partes de um programa. Elas permitem que o programador encapsule um conjunto de instruções, facilitando a organização e a manutenção do código. Em Python, as funções são definidas usando a palavra-chave `def`, seguidas pelo nome da função e parênteses que podem conter parâmetros.

### Para que servem as funções?

1. **Reutilização de Código**: As funções permitem que um bloco de código seja escrito uma vez e reutilizado várias vezes, evitando a repetição desnecessária.
   
2. **Modularidade**: Dividir um programa em funções torna-o mais fácil de entender e depurar, pois cada função pode ser testada independentemente.

3. **Organização**: As funções ajudam a estruturar o código, agrupando operações relacionadas, o que melhora a legibilidade.

4. **Parâmetros e Retornos**: As funções podem receber dados de entrada (argumentos) e retornar resultados, permitindo uma interação dinâmica com o código.

### Exemplo em Python

Aqui está um exemplo simples de uma função que soma dois números:

```python
def soma(a, b):
    resultado = a + b
    return resultado

# chamando a função
print(soma(3, 7))  # saída: 10
```

Neste exemplo, a função `soma` recebe dois parâmetros (`a` e `b`), calcula a soma deles e retorna o resultado. A chamada da função é feita passando os valores desejados, demonstrando como as funções podem ser usadas para realizar operações específicas de forma eficiente.

**Referências**:
- https://www.inf.pucrs.br/~pinho/LaproI/Funcoes/AulaDeFuncoes.htm
- https://ebaconline.com.br/blog/funcoes-python
- https://dicasdeprogramacao.com.br/o-que-sao-funcoes-e-procedimentos/
