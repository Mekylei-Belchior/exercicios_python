"""
 Faça um programa que leia um frase pelo teclado e mostre:

 - Quantas vezes aparece a letra "A";
 - Em que posição ela aparece a primeira vez;
 - Em que posição ela aparece a última vez.

"""

frase = input('Digite uma frase: ').strip().lower()

print(f'A letra (A) aparece ({frase.count("a")}) vezes na frase.')
print(f'A letra (A) aparece pela primeira vez na posição: {frase.index("a") + 1}')
print(f'A letra (A) aparece pela última vez na posição: {frase.rindex("a") + 1}')
