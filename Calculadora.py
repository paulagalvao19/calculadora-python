print('----------------Calculadora------------')

def adicao(num1,num2):
   return num1 + num2


def sub(num1,num2):
   return num1 - num2

def mult(num1,num2):
   return num1 * num2

def div(num1,num2):
    if num2 != 0:
      return num1 / num2
    else:
        return 'Não é possivel fazer divisões por 0'

def calculadora():
    print("Escolha a operação:")
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')

    op = input("Qual operação você deseja? ")

    if op in ['1','2','3','4']:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        if op == '1':
            print(f'Resultado: {adicao(num1, num2)}')
        elif op == '2':
            print(f'Resultado: {sub(num1, num2)}')
        elif op == '3':
            print(f'Resultado: {mult(num1, num2)}')
        elif op == '4':
            print(f'Resultados {div(num1, num2)}')
        else:
            print("Opção inválida! Tente novamente.")

calculadora()