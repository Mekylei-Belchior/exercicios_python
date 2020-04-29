"""
 Faça um programa que leia a velocidade de um carro.
 Se ele utrapassar 80km/h, mostre a mensagem dizendo que ele foi multado.

 A multa vai custar R$ 7,00 por cada km acima do limite.

"""

vel = int(input('Informe a velocidade do veículo: '))

if vel > 80:
    multa = float((vel - 80) * 7)

    print(f'Você foi multado em (R$ {multa:.2f}), por excesso de velocidade.')
else:
    print('Você esta dentro do limite de vecidade permitido!')