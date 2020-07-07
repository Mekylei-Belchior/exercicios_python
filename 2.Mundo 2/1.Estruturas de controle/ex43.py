"""
  Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
  e mostre seu status, de acordo com a tabela abaixo:

  - IMC abaixo de 18,5: Abaixo do Peso
  - Entre 18,5 e 25: Peso Ideal
  - 25 até 30: Sobrepeso
  - 30 até 40: Obesidade
  - Acima de 40: Obesidade Mórbida

"""

peso = float(input('Informe o seu peso (KG): '))
altura = float(input('Informe sua altura (M): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é de ({imc:.2f}). Você está ABAIXO DO PESO!')

elif imc < 25:
    print(f'Seu IMC é de ({imc:.2f}). Você está no PESO IDEAL!')

elif imc <= 30:
    print(f'Seu IMC é de ({imc:.2f}). Você está com SOBREPESO!')

elif imc <= 40:
    print(f'Seu IMC é de ({imc:.2f}). Você está com OBESIDADE!')

else:
    print(f'Seu IMC é de ({imc:.2f}). Você está com OBSIDADE MÓRBIDA!')
