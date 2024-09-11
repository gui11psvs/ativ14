# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado
nota1 = float(input("digete a primeira nota: "))
nota2 = float(input("digete a segunda nota: "))
nota3 = float(input("digete a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"média: {media:.2f}")
 
if media >= 7:
    print("aluno aprovado!")
elif 5 <= media < 7:
    print("aluno em recuperação.")
else:
    print("aluno reprovado.")
    
