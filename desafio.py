class Produto:
    def _init_(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade

p1 = Produto("Bolacha", "R$5,00", 227)
p2 = Produto("Monster", "R$9,00", 400) 

print(p1.nome, p1.quantidade)
print(p2.nome, p2.quantidade)