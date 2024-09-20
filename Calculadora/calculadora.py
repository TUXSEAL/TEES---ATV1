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
        
    
    #adicionando estruta para reprtir
    repetir()
        
    
#adicionado uma estrututra para calcular novamente ou não

def repetir():
    
    repetir_calc = input('''
    Você deseja calcular novamente? 
    Se sim, digite (S) ou (N) para sair.
    ''')
    
    if repetir_calc.upper() == 'S':
        calculadora()
        
    elif repetir_calc.upper() == 'N':
        print("\t Saindo... Obrigado!")

    else:
        repetir()


def bem_vindo():
        print('''
        Começar a calcular
        ''')


bem_vindo()
calculadora()
