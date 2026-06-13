import os
import time

# Funções suporte
def limpar_tela():
    """Limpa o terminal para manter a interface organizada."""

    os.system('cls' if os.name == 'nt' else 'clear')

def ler_opcao_numerica(mensagem):
    """Solicita um número ao usuário e trata erros caso ele digite algo inválido."""

    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("[ERRO]: Por favor, digite apenas números válidos.")

# Estoque mercado
estoque_do_mercado = {
    1: {'Maçã': 2.30, 'Banana': 2.00, 'Melancia': 14.00}, 
    2: {'Alcatra': 33.50, 'Picanha': 65.00, 'Acem': 24.75}, 
    3: {'Arroz': 6.50, 'Macarrão': 4.35, 'Feijão': 12.60}
}

saldo_inicial = 150.0  # Saldo fixo até o momento do pagamento
carrinho = []
valor_da_compra = 0.0

# Cerebro do programa, funções lógicas
def exibir_produtos(setor):
    """Exibe os produtos disponíveis no setor escolhido com formatação em vírgula."""

    produtos = estoque_do_mercado[setor]
    print('Estas são as opções disponíveis:')
    print('-' * 35)
    for nome, preco in produtos.items():
        preco_formatado = f'{preco:.2f}'.replace('.', ',')
        print(f'Produto - {nome:<10} | Preço: R$ {preco_formatado}')
    print('-' * 35)

def processar_pagamento(total):
    """Gerencia a escolha da forma de pagamento e aplica juros se necessário."""

    global saldo_inicial
    print('\nQual é a forma de pagamento?')
    print('-' * 35)
    print('1 - Dinheiro (Sem juros)')
    print('2 - Cartão (10% de juros)')
    print('-' * 35)
    
    forma_pagamento = ler_opcao_numerica('Digite aqui ---> ')
    
    total_a_pagar = 0

    if forma_pagamento == 1:
        total_a_pagar = total
        print(f'\nPagamento à vista.')
    elif forma_pagamento == 2:
        total_a_pagar = total * 1.1
        print(f'\nPagamento no cartão (10% juros).')
    else:
        print("Opção inválida.")
        return None

    if saldo_inicial >= total_a_pagar:
        saldo_inicial -= total_a_pagar
        return total_a_pagar
    else:
        print('-' * 35)
        print('Saldo insuficiente!\nTrabalhe mais ou tire algo do carrinho.')
        print('-' * 35)
        time.sleep(3)
        return None

def pagar_as_compras():
    """Gerencia a visualização do carrinho (agrupado), remoção e finalização."""

    global valor_da_compra
    while True:
        limpar_tela()
        print('------- CAIXA -------')
        print('Seu carrinho:')
        
        # Agrupamento dos itens para exibição
        contagem = {}
        for item in carrinho:
            nome = item["nome"]
            contagem[nome] = contagem.get(nome, 0) + 1
            
        for nome, quantidade in contagem.items():
            # Busca o preço original de qualquer instância desse item no carrinho
            preco = next(i['preco'] for i in carrinho if i['nome'] == nome)
            print(f'{quantidade}x {nome} | Preço unitário: R$ {f"{preco:.2f}".replace(".", ",")}')
        
        total_formatado = f'{valor_da_compra:.2f}'.replace('.', ',')
        saldo_formatado = f'{saldo_inicial:.2f}'.replace('.', ',')
        print(f'\nTotal da compra: R$ {total_formatado} | Meu saldo: R$ {saldo_formatado}')
        
        if valor_da_compra == 0:
            print("Carrinho vazio. Saindo...")
            return

        print('\n1 - Finalizar Pagamento\n2 - Remover item')
        opcao = ler_opcao_numerica('Escolha uma opção: ')
        
        if opcao == 2:
            item_nome = input("Digite o nome do produto para remover: ").title()
            for i in range(len(carrinho) - 1, -1, -1):
                if carrinho[i]['nome'] == item_nome:
                    removido = carrinho.pop(i)
                    valor_da_compra -= removido['preco']
                    break
        elif opcao == 1:
            total_final = processar_pagamento(valor_da_compra)
            if total_final:
                print(f"\nCompra finalizada! Valor debitado: R$ {f'{total_final:.2f}'.replace('.', ',')}")
                break
    print()
    return

# Corpo do programa
while True:
    limpar_tela()
    print('------ Bem vindo ao MERCADO! ------')
    print(f'Saldo disponível: R$ {f"{saldo_inicial:.2f}".replace(".", ",")}')
    
    # Exibição em tempo real do valor no carrinho
    valor_carrinho_fmt = f'{valor_da_compra:.2f}'.replace(".", ",")
    print(f'Valor atual no carrinho: R$ {valor_carrinho_fmt}')
    
    print('1 - Frutas | 2 - Carnes | 3 - Massas')
    print('-' * 35)
    
    setor_escolhido = ler_opcao_numerica('---> ')
    
    if setor_escolhido in estoque_do_mercado:
        exibir_produtos(setor_escolhido)
        item_escolhido = input('O que deseja comprar deste setor: ').title()
        
        if item_escolhido in estoque_do_mercado[setor_escolhido]:
            preco = estoque_do_mercado[setor_escolhido][item_escolhido]
            carrinho.append({'nome': item_escolhido, 'preco': preco})
            valor_da_compra += preco
            print(f'\n{item_escolhido} adicionado ao carrinho!')
        else:
            print("\nProduto não encontrado.")
        time.sleep(1)
    
    if input('\nDeseja comprar algo mais? [S/N]: ').lower() != 's':
        break

pagar_as_compras()