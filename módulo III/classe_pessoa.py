class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def infos(self, nome, idade): 
        return f'Nome: {nome}, Idade: {idade}' 
    
    

nome = input()
idade = int(input())

p = Pessoa()
resultado = p.infos(nome, idade)

print(resultado)