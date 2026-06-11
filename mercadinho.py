import os

def exibir_mercado():
    """ Função para exibir e selecionar 
    a compra do usuário """

    print(f'Seu saldo atual é: {meu_saldo}')
    print()
    print('Boa tarde Sr.(a), o que deseja comprar? ')
    print('1 - Frutas')
    print('2 - Carnes')
    print('3 - Massas')
    comprar = int(input('-> '))

    return comprar

def exibir_frutas():
    pass


estoque_do_mercado = [{1:{'Maçã': 2.30, 'Banana': 2.00, 'Melancia': 14.00}, 
                       2:{'Alcatra': 33.50, 'Picanha': 65.00, 'Acem': 24.75}, 
                       3:{'Arroz': 6.50, 'Macarrão': 4.35, 'Feijão': 12.60}}]

meu_saldo = 150
carrinho = 0.0
valor_da_compra = 0.0

while True:
    os.system('cls')
    match exibir_mercado():
        case 1:
            exibir_frutas()
            pass
        case 2:
            pass
        case 3:
            pass
        case _:
            pass

