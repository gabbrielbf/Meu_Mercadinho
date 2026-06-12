import os
import time

def pagar_as_compras():
    print('------- Bem vindo ao CAIXA! -------')
    print(f'Sua compra deu: R$[{valor_da_compra}]')
    print(f'Você tem R$[{meu_saldo + valor_da_compra}] na conta.')
    print('Qual é a forma de pagamento?')
    print('-' * 35)
    print('1 - Dinheiro')
    print('2 - Cartão')
    print('-' * 35)

    while True:
        pagamento = int(input('Digite aqui ---> '))
        juros = valor_da_compra * 1.1

        if pagamento == 1:
            print()
            print('Pagamento a vista não tem juros!')
            print(f'Sua compra deu: R$[{valor_da_compra}]')
            time.sleep(0.7)
            print(f'Foi descontado da sua carteira: {valor_da_compra}')
            time.sleep(0.7)
            print(f'Sobrou: R$[{meu_saldo - valor_da_compra}]')
            time.sleep(0.7)
            break
        elif pagamento == 2:
            print()
            print('Pagamento no cartão tem 10% juros!')
            print(f'Sua compra deu: R$[{valor_da_compra:.2f}]')
            time.sleep(0.7)
            print(f'Foi descontado da sua carteira: R$[{juros:.2f}]')
            time.sleep(0.7)
            print(f'Sobrou: R$[{(meu_saldo + valor_da_compra) - juros:.2f}]')
            time.sleep(0.7)
            break
        else:
            print('Não possuímos esta forma de pagamento.')
            print()
            continue
    print()
    return

def continuar_comprando(comprar_mais):
    print(f'Sua decisao foi [{comprar_mais.upper()}]')
    if comprar_mais == 's':
        comprar_mais = True
    else:
        comprar_mais = False
    return comprar_mais

def exibir_mercado():
    """ Função para exibir e selecionar 
    a compra do usuário """

    print()
    print('------ Bem vindo ao MERCADO! ------')
    print('Boa tarde Sr.(a), o que deseja comprar? ')
    print('-' * 35)
    print('1 - Frutas')
    print('2 - Carnes')
    print('3 - Massas')
    print('-' * 35)
    comprar = int(input('---> '))

    return comprar

def exibir_frutas():
    """ Função para exibir as 
    frutas disponíveis """

    print('Estas são as FRUTAS disponíveis: ')
    print('-' * 35)
    frutas = estoque_do_mercado[0][1]

    for fruta, preco in frutas.items():
        preco_formatato = f'{preco:.2f}'
        print(f'Produto - {fruta} | Preço: {preco_formatato.replace('.',',')}')
    print('-' * 35)
    print()

    return 

def exibir_carnes():
    """ Função para exibir as 
    carnes disponíveis """

    
    print('Estas são as CARNES disponíveis: ')
    print('-' * 35)
    carnes = estoque_do_mercado[0][2]

    for carne, preco in carnes.items():
        preco_formatato = f'{preco:.2f}'
        print(f'Produto - {carne} | Preço: {preco_formatato.replace('.',',')}')
    print('-' * 35)
    print()

    return 

def exibir_massas():
    """ Função para exibir as 
    massas disponíveis """

    print('Estas são as MASSAS disponíveis: ')
    print('-' * 35)
    massas = estoque_do_mercado[0][3]

    for massa, preco in massas.items():
        preco_formatato = f'{preco:.2f}'
        print(f'Produto - {massa} | Preço: {preco_formatato.replace('.',',')}')
    print('-' * 35)
    print()

    return 

def qual_fruta_comprar(Oque_comprar):
    """ Função para definir, subtrair e adicionar
     o produto comprado pelo usuário """

    global valor_da_compra, meu_saldo
    frutas = estoque_do_mercado[0][1]
    
    match Oque_comprar:
        case 'Maçã':
            print(f'o produto ({Oque_comprar}) foi adicionado ao carrinho com sucesso')
            print('-' * 35)
            for fruta, preco in frutas.items():
                if Oque_comprar == fruta:
                    carrinho.append(fruta) 
                    valor_da_compra += preco
                    meu_saldo -= preco
                    preco_formatato = f'{preco:.2f}'
            print(f'Essa compra custou: {preco_formatato.replace('.',',')}')
            preco_formatato = f'{meu_saldo:.2f}'
            print(f'Seu saldo atual é de: {preco_formatato.replace('.',',')}')
            print('-' * 35)
        case 'Banana':
            print(f'o produto ({Oque_comprar}) foi adicionado ao carrinho com sucesso')
            print('-' * 35)
            for fruta, preco in frutas.items():
                if Oque_comprar == fruta:
                    carrinho.append(fruta)
                    valor_da_compra += preco
                    meu_saldo -= preco
                    preco_formatato = f'{preco:.2f}'
            print(f'Sua compra atual custa: {preco_formatato.replace('.',',')}')
            preco_formatato = f'{meu_saldo:.2f}'
            print(f'Seu saldo atual é de: {preco_formatato.replace('.',',')}')
            print('-' * 35)
        case 'Melancia':
            print(f'o produto ({Oque_comprar}) foi adicionado ao carrinho com sucesso')
            print('-' * 35)
            for fruta, preco in frutas.items():
                if Oque_comprar == fruta:
                    carrinho.append(fruta)
                    valor_da_compra += preco
                    meu_saldo -= preco
                    preco_formatato = f'{preco:.2f}'
            print(f'Sua compra atual custa: {preco_formatato.replace('.',',')}')
            preco_formatato = f'{meu_saldo:.2f}'
            print(f'Seu saldo atual é de: {preco_formatato.replace('.',',')}')
            print('-' * 35)
        case _:
            print(f'Não temos ({Oque_comprar}) em nosso estoque.')
            print()
    return

def qual_carne_comprar(Oque_comprar):
    """ Função para definir, subtrair e adicionar
     o produto comprado pelo usuário """

    global valor_da_compra, meu_saldo
    carnes = estoque_do_mercado[0][2]
    
    match Oque_comprar:
        case 'Alcatra':
            print(f'o produto ({Oque_comprar}) foi adicionado ao carrinho com sucesso')
            print('-' * 35)
            for carne, preco in carnes.items():
                if Oque_comprar == carne:
                    carrinho.append(carne)
                    valor_da_compra += preco
                    meu_saldo -= preco
                    preco_formatato = f'{preco:.2f}'
            print(f'Essa compra custou: {preco_formatato.replace('.',',')}')
            preco_formatato = f'{meu_saldo:.2f}'
            print(f'Seu saldo atual é de: {preco_formatato.replace('.',',')}')
            print('-' * 35)
        case 'Picanha':
            print(f'o produto ({Oque_comprar}) foi adicionado ao carrinho com sucesso')
            print('-' * 35)
            for carne, preco in carnes.items():
                if Oque_comprar == carne:
                    carrinho.append(carne)
                    valor_da_compra += preco
                    meu_saldo -= preco
                    preco_formatato = f'{preco:.2f}'
            print(f'Sua compra atual custa: {preco_formatato.replace('.',',')}')
            preco_formatato = f'{meu_saldo:.2f}'
            print(f'Seu saldo atual é de: {preco_formatato.replace('.',',')}')
            print('-' * 35)
        case 'Acem':
            print(f'o produto ({Oque_comprar}) foi adicionado ao carrinho com sucesso')
            print('-' * 35)
            for carne, preco in carnes.items():
                if Oque_comprar == carne:
                    carrinho.append(carne)
                    valor_da_compra += preco
                    meu_saldo -= preco
                    preco_formatato = f'{preco:.2f}'
            print(f'Sua compra atual custa: {preco_formatato.replace('.',',')}')
            preco_formatato = f'{meu_saldo:.2f}'
            print(f'Seu saldo atual é de: {preco_formatato.replace('.',',')}')
            print('-' * 35)
        case _:
            print(f'Não temos ({Oque_comprar}) em nosso estoque.')
            print()
    return

def qual_massa_comprar(Oque_comprar):
    """ Função para definir, subtrair e adicionar
     o produto comprado pelo usuário """

    global valor_da_compra, meu_saldo
    massas = estoque_do_mercado[0][3]
    
    match Oque_comprar:
        case 'Arroz':
            print(f'o produto ({Oque_comprar}) foi adicionado ao carrinho com sucesso')
            print('-' * 35)
            for massa, preco in massas.items():
                if Oque_comprar == massa:
                    carrinho.append(massa)
                    valor_da_compra += preco
                    meu_saldo -= preco
                    preco_formatato = f'{preco:.2f}'
            print(f'Essa compra custou: {preco_formatato.replace('.',',')}')
            preco_formatato = f'{meu_saldo:.2f}'
            print(f'Seu saldo atual é de: {preco_formatato.replace('.',',')}')
            print('-' * 35)
        case 'Macarrão':
            print(f'o produto ({Oque_comprar}) foi adicionado ao carrinho com sucesso')
            print('-' * 35)
            for massa, preco in massas.items():
                if Oque_comprar == massa:
                    carrinho.append(massa)
                    valor_da_compra += preco
                    meu_saldo -= preco
                    preco_formatato = f'{preco:.2f}'
            print(f'Sua compra atual custa: {preco_formatato.replace('.',',')}')
            preco_formatato = f'{meu_saldo:.2f}'
            print(f'Seu saldo atual é de: {preco_formatato.replace('.',',')}')
            print('-' * 35)
        case 'Feijão':
            print(f'o produto ({Oque_comprar}) foi adicionado ao carrinho com sucesso')
            print('-' * 35)
            for massa, preco in massas.items():
                if Oque_comprar == massa:
                    carrinho.append(massa)
                    valor_da_compra += preco
                    meu_saldo -= preco
                    preco_formatato = f'{preco:.2f}'
            print(f'Sua compra atual custa: {preco_formatato.replace('.',',')}')
            preco_formatato = f'{meu_saldo:.2f}'
            print(f'Seu saldo atual é de: {preco_formatato.replace('.',',')}')
            print('-' * 35)
        case _:
            print(f'Não temos ({Oque_comprar}) em nosso estoque.')
            print()
    return

estoque_do_mercado = [{1:{'Maçã': 2.30, 'Banana': 2.00, 'Melancia': 14.00}, 
                       2:{'Alcatra': 33.50, 'Picanha': 65.00, 'Acem': 24.75}, 
                       3:{'Arroz': 6.50, 'Macarrão': 4.35, 'Feijão': 12.60}}]

meu_saldo = 150
carrinho = []
valor_da_compra = 0

while True:
    #os.system('cls')
    match exibir_mercado():
        case 1:
            exibir_frutas()
            oque_comprar = input('O que deseja comprar deste setor: ').title()
            qual_fruta_comprar(oque_comprar)
        case 2:
            exibir_carnes()
            oque_comprar = input('O que deseja comprar deste setor: ').title()
            qual_carne_comprar(oque_comprar)
        case 3:
            exibir_massas()
            oque_comprar = input('O que deseja comprar deste setor: ').title()
            qual_massa_comprar(oque_comprar)
        case _:
            print('Infelizmente não temos este item.')
            continue
    comprar_mais = str(input('Deseja comprar algo mais?[S/N]: ')).lower()
    if continuar_comprando(comprar_mais) == True and meu_saldo > 0:
        continue
    else:
        break
print()
pagar_as_compras()
