# Coleta da idade do usuário e informa a faixa etária a qual ele pertence.

age = int(input("Digite a idade: "))

# A estrutura condicional if-elif-else é utilizada para verificar se a idade

if age < 18:
    print("Você é menor de idade.")
elif age >= 18 and age < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")