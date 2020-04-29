"""
 Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
 Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

"""

check = []

exp = str(input('Digite uma expressão: '))

for simb in exp:

    if simb == '(':
        check.append(simb)

    elif simb == ')':

        if len(check) > 0:
            check.pop()

        else:
            check.append(simb)
            break

print()
if len(check) == 0:

    print('Sua expressão está CORRETA!')

else:

    print('Sua expressão está ERRADA!')
