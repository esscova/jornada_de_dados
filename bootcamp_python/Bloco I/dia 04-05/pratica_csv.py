"""
descrição
    - Exemplo de como ler arquivos csv com API csv do python
    - Documentação: https://docs.python.org/3/library/csv.html

autor
    - wellington moreira   
    - wsantos08@hotmail.com

versão python
    - 3.12.4
    
"""
def main() -> None:
    import csv

    try:
        caminho_arquivo:str = 'data/exemplo.csv'
        dados:list = []

        # metodo .reader() para leitura de linha por linha
        # metodo .DictReader() para leitura de linha por linha e transformar em dicionario
        # with gera um contexto para o arquivo assegurando que ele seja fechado

        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            
            for linha in leitor_csv:
                dados.append(linha)

        for registro in dados:    
            print(registro)

    except Exception as e:
        print(f'Erro: {e}')

    except FileNotFoundError:
        print(f'Arquivo {caminho_arquivo} nao encontrado')

if __name__ == '__main__':
    main()