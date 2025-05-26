class Aluno:
    def __init__(self, nome, turma, nota):
        self.nome = nome
        self.turma = turma
        self.nota = nota


# Criando objetos
a1 = Aluno("Miguel", "3A", 90)
a2 = Aluno("Eliza","2B", 80)


print(a1.nome, a1.turma, a1.nota)  
print(a2.nome, a2.turma, a2.nota)  
