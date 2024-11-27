"""
Exercícios: entendendo sobre Classes

Exercício 1:
Crie uma classe Carro com os atributos marca, modelo e ano. Adicione um método mostrar_info() que imprime as informações do carro.

Exercício 2:
Modifique a classe Carro para incluir um método que atualiza o ano do carro. Crie um objeto dessa classe e atualize o ano.

Exercício 3:
Implemente uma classe Produto com os atributos nome, preço e quantidade. Adicione um método calcular_valor_total() que retorna o valor total (preço * quantidade).

Exercício 4:
Crie uma classe Pessoa com os atributos nome e idade. Adicione um método aniversario() que aumenta a idade em 1 a cada vez que é chamado. 
Crie um objeto e simule o aniversário da pessoa.

Exercício 5:
Crie uma classe Aluno com os atributos nome, nota1, nota2 e nota3. Adicione um método calcular_media() que retorna a média das notas. 
Teste a classe com alguns objetos.
"""
# Exercício 1
class Carro:
    def __init__ (self):
        self.marca = 'Fiat'
        self.modelo = 'Uno com escada'
        self.ano = 2001

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

# Exercício 2
class Carro:
    def __init__ (self):
        self.marca = 'Fiat'
        self.modelo = 'Uno com escada'
        self.ano = 2001

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

    def atualizar_ano(self, novo_ano):
        self.ano = novo_ano

# Exercício 3
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.preco * self.quantidade

# Exercício 4
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez aniversário e agora tem {self.idade} anos.")

# Exercício 5
class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

if __name__ == "__main__":
    carro1 = Carro()
    carro1.mostrar_info()

    carro1.atualizar_ano(2023)
    carro1.mostrar_info()

    produto1 = Produto("Produto 1", 10.99, 5)
    print(produto1.calcular_valor_total())

    pessoa1 = Pessoa("Matusalém", 999)
    pessoa1.aniversario()

    aluno1 = Aluno("Akita", 10, 10, 10)
    aluno2 = Aluno("escova", 5, 5, 5)

    alunos = [aluno1, aluno2]
    for aluno in alunos:
        if aluno.calcular_media() >= 7:
            print(f"Nome: {aluno.nome}, Média: {aluno.calcular_media()}, O miserável é um gênio!")
        else:
            print(f"Nome: {aluno.nome}, Média: {aluno.calcular_media()}, Só vim pela merenda mermo!")