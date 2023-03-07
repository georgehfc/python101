class Pessoa:
    def __init__(self, nome, documento=None):
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

# "Estudante estende de Pessoa"
class Estudante(Pessoa):
    def __init__(self, nome, documento, matricula):
        # 'SUPER()' CHAMA A CLASSE MÃE
        super().__init__(nome=nome, documento=documento)
        self.matricula = matricula

    def mostrar_nome(self):
        return f'O nome da pessoa estudante é: {self.nome}'

# "Docente é uma especialização de Pessoa"
class Docente(Pessoa):
    def __init__(self, nome, documento=None):
        super().__init__(nome, documento)
        self.turmas = []

class DisciplinaEscolar:
    def __init__(self, nome, pessoa_responsavel):
        self.nome = nome
        self.pessoa_responsavel = pessoa_responsavel
        self.estudantes = []

    def __str__(self):
        return f'{self.nome} ({self.pessoa_responsavel})'

    def cadastro_estudante(self, estudante):
        print(f'Cadastrando estudante {estudante}...')
        if estudante in self.estudantes:
            print(f'Estudante {estudante} já foi cadastrado.')
        else:
            self.estudantes.append(estudante)
            print(f'Estudante {estudante} cadastrado.')

#
estudante = Estudante(nome='George', documento='1234', matricula='83748934')
print(estudante.mostrar_nome())
responsavel = Pessoa(nome='Danny Sanchez')
disciplina = DisciplinaEscolar(nome='LP I', pessoa_responsavel=responsavel.nome)
disciplina.cadastro_estudante(estudante)
print(disciplina)
