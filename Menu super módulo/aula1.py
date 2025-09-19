# nome = str(input("Digite seu nome"))
# print(f"Bem vindo ao modulo de python {nome}.")


# num1 = int(input("Digite um numero: "))
# num2 = int(input("Digite o segundo número: "))

# print(f'''
#       {num1} + {num2} = {num1 + num2}
#       {num1} - {num2} = {num1 - num2}
#       {num1} / {num2} = {num1 / num2} 
#       ''')

# idade = int(input("Digite a sua idade: "))

# if idade >= 18:
#     print("O usuario é maior de idade")
# else:
#     print("O usuario é menor de idade")


# nota = int(input("Digite a sua nota: "))

# if nota >= 9:
#     print("Excelente!")
# elif nota >= 7:
#     print("Bom!")
# elif nota >= 6:
#     print("Regular!")
# if nota < 6:
#     print("Reprovado!")


## menu interativo

while True:
    print('''
          Bem vindo ao menu interativo!
          Digite a opção desejada:
          1 - Calculadora
          1 - Calculador de média
          3 - Contador de números 
          4 - Verificador de par ou inpar
          0 - Encerrar programa
          ''')
    
    opicao = int(input("Digite a opição desejada:"))
    if opicao == 1:
        print("\nBem vindo a CALCULADORA\n")
        num1 = int(input("Digite um número:"))
        num2 = int(input("Digite outro número:"))
        operacao_mat = str(input("Digite a operação mateática desejada. +, -, *, /:"))
        print("")
        if operacao_mat == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        if operacao_mat == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        if operacao_mat == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        if operacao_mat == "/":
            print(f"{num1} / {num2} = {num1 / num2}")
    elif opicao == 2:
        print("\nBem vindo ao CALCULADOR DE MÉDIA")
        numeros = int(input("Digite quantos números irá inserir para fazer a média:"))
        soma = 0
        for i in range(1, numeros+1):
            n_usuario = int(input(f"Digite o {i}° numero:"))
            soma += n_usuario
        media = soma/numeros
        print("")
        print(f"Amédia dos números é {media}")
    elif opicao == 3:
        print("\nBem vindo ao CONTADOR DE NÚMEROS")
        num = int(input("Digite até qual número deseja contar:"))
        for i in range(1, num+1):
            print(i)
    elif opcao == 0:
        print("Programa encerrado")
        break        
            

                  
            
    
    
    


