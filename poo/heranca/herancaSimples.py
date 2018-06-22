class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class PessoaFisica(Pessoa):

    def __init__(self, nome, idade, cpf):
        Pessoa.__init__(self,nome,idade)
        self.cpf = cpf

    def __repr__(self):
        return f'{self.nome} tem {self.idade} ano(s), está registrado no cpf {self.cpf}'

renatinho = PessoaFisica('Renato', 41, '364.158.364-74')
print(renatinho)