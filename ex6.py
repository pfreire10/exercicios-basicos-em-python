valor_compra = input('Digite o valor da compra: ')

valor_compra = float(valor_compra)

if valor_compra < 0:
    print('Valor inválido')

elif valor_compra < 100:
    porc_desconto = 0
    desconto = 0
    valor_final = valor_compra - desconto
    print(f'Valor original: {valor_compra}. Porcentagem de desconto: {porc_desconto}. Valor descontado: {desconto}. Valor final: {valor_final}.')

elif valor_compra >= 100 and valor_compra <=  299.99:
    porc_desconto = 5
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print(f'Valor original: {valor_compra}. Porcentagem de desconto: {porc_desconto}. Valor descontado: {desconto}. Valor final: {valor_final}.')

elif valor_compra >= 300 and valor_compra <= 499.99:
    porc_desconto = 10
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f'Valor original: {valor_compra}. Porcentagem de desconto: {porc_desconto}. Valor descontado: {desconto}. Valor final: {valor_final}.')

else: 
    porc_desconto = 15
    desconto = valor_compra * 0.15
    valor_final = valor_compra - desconto
    print(f'Valor original: {valor_compra}. Porcentagem de desconto: {porc_desconto}. Valor descontado: {desconto}. Valor final: {valor_final}.')
    