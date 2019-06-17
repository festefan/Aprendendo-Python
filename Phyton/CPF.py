#Validador de cpf
import re
print('\n Validador de CPF \n')

cpf = str(input('Entre com os números do CPF com ponto e hífen: \n'))
          
if re.search('\d{3}.\d{3}.\d{3}-\d{2}' ,cpf) :
    print("CPF Validado")
else:
    print("Numero de CPF fora do Padrão")
