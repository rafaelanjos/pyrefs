class Dog:

    # Atributo de classe
    species = 'mammal'

    # Inicializador - Atributos de instância
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Método de instância
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # Método de instância
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Instancias da classe DOG()
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Acessa os atributos da instância
print("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age))

# Philo é mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))

# Acessa atributo da classe
print(Dog.species)

# Invoca métodos da instância
print(mikey.description())
print(mikey.speak("Gruff Gruff"))

# Herança
# Classe filha - herda da classe DOG
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Classe filha - herda da classe DOG
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


#A classe filha herda os atributos e comportamentos da classe pai
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))

#A função isinstance() é usada para determinar se a instância pertencia a uma classe

# jim  é uma instância de Dog()?
print(isinstance(jim, Dog))

# julie é uma instância de Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# johnny walker é uma instância de Bulldog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

# julie é uma instância de  jim?
# A linha abaixo lança a exceção
# print(isinstance(julie, jim))
# TypeError: isinstance() arg 2 must be a type or tuple of types
# Segundo argumento deve ser um typo ou uma tupla de tipos

# Herança # Sobrescrita de atributos
class SomeOtherBreed(Dog):
    species = 'reptile'

beans = SomeOtherBreed('Sussi', 3)
print(beans.species)