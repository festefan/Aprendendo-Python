# divisão por dois números
try:
    numero1 = float(input('Entre com o primeiro número: '))
    numero2 = float(input('Entre com o segundo número: '))
    numero1 = numero1 / numero2
    print("O resultado é: ",numero1)
except ValueError:
    print("Valor inválido!")
except ZeroDivisionError:
    print("Não é possível divisão por zero")
input('Pressione ENTER para sair...')
