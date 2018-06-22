class Funcionario:

    def __init__(self, nome, salario, cpf):
        self.nome = nome
        self.salario = salario
        self.cpf = cpf
    

    def bonificacao(self):
        return self.salario * 0.10

class Gerente(Funcionario):

    def __init__(self, nome, salario, cpf, bonus):
        #Funcionario.__init__(nome, salario, cpf) # ou
        super().__init__(nome, salario, cpf)
        self.__bonus = bonus  #Atributo exclusivo e privado da classe gerente
    
    # Especialização do comportamento
    def bonificacao(self):
        # Mantem encapsulado a regra de bonificação do funcionário e adiciona o bonus do gestor
        return super().bonificacao() + self.__bonus

    def set_bonus(self, bonus):
        self.__bonus = bonus


gervasio = Gerente('Gervasio', 5000, '132.145.654-47', 1500)
print('bonus', gervasio.bonificacao()