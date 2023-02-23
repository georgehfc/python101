# ficha_pessoa = {
#     "nome": "Jose Luiz",
#     "sobrenome": "Oliveira",
#     "cep": "123",
#     "data_nascimento": "34/13"
# }

class FichaPessoa():   # class "FichaPessoa"
    # campos - variaveis
    # metodos - funcoes

    # sempre roda ao criar o objeto, magicamente
    def __init__(self, p_nome, p_sobrenome, p_cep, p_data_nascimento):
        self.nome = p_nome   # campo "nome"
        self.sobrenome = p_sobrenome
        self.cep = p_cep
        self.data_nascimento = p_data_nascimento

    def alterar_sobrenome(self, p_novo_sobrenome):
        self.sobrenome = p_novo_sobrenome

    def mostrar_nome_completo(self):    # metodo - mostrar_nome_completo
        return f"{self.nome} {self.sobrenome}"


ficha_erick = FichaPessoa(p_nome="Erick", p_sobrenome="Muller",
                          p_cep="010101", p_data_nascimento="27/12")
print(ficha_erick)
print(f'Nome: {ficha_erick.nome}')
print(f"Nome completo: {ficha_erick.mostrar_nome_completo()}")


ficha_samuel = FichaPessoa(p_nome="Samuel", p_sobrenome="Costa",
                           p_cep="010110", p_data_nascimento="22/05")
print(ficha_samuel)
print(f'Nome: {ficha_samuel.nome}')
print(f"Nome completo: {ficha_samuel.mostrar_nome_completo()}")
ficha_samuel.alterar_sobrenome("Abobrinhas")
print(f"Nome completo: {ficha_samuel.mostrar_nome_completo()}")

ficha_alexandre = FichaPessoa(p_nome="Alexandre", p_sobrenome="Calixto",
                              p_cep="0555541", p_data_nascimento="07/06")
print(ficha_alexandre)
print(f'Nome: {ficha_alexandre.nome}')
print(f"Nome completo: {ficha_alexandre.mostrar_nome_completo()}")