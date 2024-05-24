def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError('Não é possível dividir por zero!')
    return x / y

def exibir_menu():
    print("Selecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

def calcular():
    
    while True:
        exibir_menu()
        escolha = input("Digite o número da operação desejada: ")

        if escolha == '5':
            print('Finalizando calculadora.')
            break
        elif escolha not in {'1', '2', '3', '4'}:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print("Resultado:", adicionar(num1, num2))
            elif escolha == '2':
                print("Resultado:", subtrair(num1, num2))
            elif escolha == '3':
                print("Resultado:", multiplicar(num1, num2))
            elif escolha == '4':
                print("Resultado:", dividir(num1, num2))

        except ValueError as e:
            print(e)
                
if __name__ == "__main__":
    calcular()