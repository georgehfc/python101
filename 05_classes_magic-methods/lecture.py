class Pessoa:
    def __init__(self, nome, documento = None):
        self.nome = nome
        self.documento = documento

    def __str__(self):
        return f'{self.nome} #{self.documento}'

    def mostrar_nome(self):
        return f'O nome da pessoa é {self.nome}'

    def mostrar_nome_tres_vezes(self):
        frase = f'O nome da pessoa é {self.nome}\n'
        frase = frase + f'Eu disse {self.nome}!\n'
        frase = frase + f'{self.nome}!'.upper()
        return frase

class Estudante(Pessoa):
    def __init__(self, nome, documento, matricula):
        super().__init__(nome = nome, documento = documento)
        self.matricula = matricula

    def mostrar_nome(self):
        return f'O nome da pessoa estudante é: {self.nome}'

class DisciplinaEscolar:
    def __init__(self, nome, pessoa_responsavel):
        self.nome = nome
        self.pessoa_responsavel = pessoa_responsavel
        self.estudantes = []

    def cadastro_estudante(self, estudante):
        print(f'Cadastrando estudante {estudante}...')
        if estudante in self.estudantes:
            print(f'Estudante {estudante} já foi cadastrado.')
        else:
            self.estudantes.append(estudante)
            print(f'Estudante {estudante} cadastrado.')

# CLASS 'DOCENTE'

# pessoa = Pessoa(nome = 'George', documento = '1234')
# print(pessoa.mostrar_nome())

# estudante = Estudante(nome = 'Chaves', documento = '1212', matricula = '2525245334')
# print(estudante.mostrar_nome())

# anonimo = Pessoa(nome = 'Mistério', documento = '666')
# print(anonimo.mostrar_nome_tres_vezes())
