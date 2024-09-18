#criando uma função para calcular

def calculadora():

#Menu de operações

    operacao = input('''
    Qual operação matemática você quer:
    + para adição
    - para subtração
    * para multiplicação
    / para divisão
    ''')

    if operacao == '+':
        # adição
        numero_1 = float(input('Digite o primeiro numero: '))
        numero_2 = float(input('Digite o segundo numero: '))
        
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operacao == '-':
        # subtração
        numero_1 = float(input('Digite o primeiro numero: '))
        numero_2 = float(input('Digite o segundo numero: '))
        
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operacao == '*':
        # multiplicação
        numero_1 = float(input('Digite o primeiro numero: '))
        numero_2 = float(input('Digite o segundo numero: '))
        
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operacao == '/':
        # divisão
        numero_1 = float(input('Digite o primeiro numero: '))
        numero_2 = float(input('Digite o segundo numero: '))
        
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)
                
    else:
        print('Insira uma opção válida.')
        
    
        
calculadora()