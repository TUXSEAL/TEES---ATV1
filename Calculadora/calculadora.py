def calculadora():
    # Menu de operações
    operacao = input('''
    Qual operação matemática você quer:
    + para adição
    - para subtração
    * para multiplicação
    / para divisão
    ''')

    if operacao in ['+', '-', '*', '/']:
        numero_1 = float(input('Digite o primeiro número: '))
        numero_2 = float(input('Digite o segundo número: '))

        if operacao == '+':
            resultado = numero_1 + numero_2
            operacao_str = ' + '
        elif operacao == '-':
            resultado = numero_1 - numero_2
            operacao_str = ' - '
        elif operacao == '*':
            resultado = numero_1 * numero_2
            operacao_str = ' * '
        elif operacao == '/':
            if numero_2 != 0:
                resultado = numero_1 / numero_2
                operacao_str = ' / '
            else:
                print('Erro: Divisão por zero não é permitida.')
                repetir()
                return

        print(f'{numero_1}{operacao_str}{numero_2} = {resultado}')
    else:
        print('Insira uma opção válida.')

    repetir()

def repetir():
    repetir_calc = input('''
    Você deseja calcular novamente? 
    Se sim, digite (S) ou (N) para sair.
    ''').upper()

    if repetir_calc == 'S':
        calculadora()
    elif repetir_calc == 'N':
        print("\tSaindo... Obrigado!")
    else:
        repetir()

def bem_vindo():
    print('''
    Começar a calcular
    ''')

bem_vindo()
calculadora()
