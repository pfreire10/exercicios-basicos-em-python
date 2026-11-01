mes = int(input('Digite o número do mês (1 a 12): '))

match mes:
    case 1:
        print('Janeiro')
    case 2:
        print('Fevereiro')
    case 3:
        print('Março')
    case 4:
        print('Abril')
    case 5:
        print('Maio')
    case 6:
        print('Junho')
    case 7:
        print('Julho')
    case 8:
        print('Agosto')
    case 9:
        print('Setembro')
    case 10:
        print('Outubro')
    case 11:
        print('Novembro')
    case 12:
        print('Dezembro')
    case _:
        print('Mês inválido. Por favor, digite um número entre 1 e 12.')

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print('Este mês tem 31 dias.')
    case 4 | 6 | 9 | 11:
        print('Este mês tem 30 dias.')
    case 2:
        print('Este mês tem 28 dias normalmente, ou 29 , se for um ano bissexto.')
    case _:
        print('Mês inválido. Por favor, digite um número entre 1 e 12.')