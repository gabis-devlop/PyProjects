#CRIANDO UM PROGRAMA QUE CALCULA A MÉDIA DE UM ALUNO E INFORMA SE ELE FOI APROVADO OU REPROVADO

nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a terceira nota: "))
nota_4 = int(input("Digite a quarta nota: "))

#CONDIÇÕES PARA APROVAÇÃO DO ALUNO

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

#IMPRIMINDO A MÉDIA E SITUAÇÃO DO ALUNO

print(f"A média do aluno foi {media:.2f} e ele foi {situacao}")