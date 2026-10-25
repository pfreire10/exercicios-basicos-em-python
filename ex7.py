print('Calculadora simples!')


print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')

opcao = input('Digite a opção da operação desejada: ')
opcao = int(opcao)

n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')

n1 = float(n1)
n2 = float(n2)

match opcao:
    case 1:
        resultado = n1 + n2
        print(f'O resultado da soma de {n1} e {n2} é: {resultado}.')
    case 2:
        resultado = n1 - n2
        print(f'O resultado da subtração de {n1} e {n2} é: {resultado}.')
    case 3:
        resultado = n1 * n2
        print(f'O resultado da multiplicação de {n1} e {n2} é: {resultado}.')
    case 4:
        if n2 == 0:
            print('Não é possível dividir por zero.')
        else:
            resultado = n1 / n2
            print(f'O resultado da divisão de {n1} e {n2} é: {resultado}.')
    case _:
        print('Opção inválida.')