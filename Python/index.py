################################ DIA 1 ####################################
######################
#print("teste")
#funcionou

######################
#num1 = 2
#num2 = 2
#print(num1 + num2)

###################### CALCULADORA DE MÉDIA
# num1 = 1
# num2 = 10
# media = (num1 + num2)/2

# if num1 < 0 or num2 < 0:
#     print('valores menor que o permitido')

# elif num1 > 10 or num2 > 10:
#     print('valores superior ao limite')

# elif media >= 6:
#     print(media , "passou")

# else:
#     print(media , "nao passou")

###################### VARIFICAR SE O NÚMERO É PAR OU ÍMAPAR
# num1 = 3

# if num1 % 2 == 0:
#     print('par')

# else:
#     print('impar')

###################### MULTIPLICADOR
# pedir pro usuário falar se quer que o número retorne o dobro ou o triplo, pedir o número
# mult aceita apenas DOBRO ou TRIPLO

# mult = 'TRIPLO'
# num = 2
# x= num * 2
# y= num * 3

# if mult == 'DOBRO':
#     print(x)

# elif mult == 'TRIPLO':
#     print(y)

# else:
#     print('campo mult aceita apenas DOBRO ou TRIPLO')

###################### FOR (comum)
# for i in range(100):
#     if i % 2 == 0: #resta 0 para PAR e resta 1 para IMPAR
#         print(i)

###################### FOR (tabuada)
# tabuada = 4

# for i in range(0,11):
#     result = i * tabuada
#     print(tabuada, "x", i, "=", result)

###################### LISTA (ordenar por ordem alfabetica)
# mercado = ['pao', 'arroz', 'queijo', 'macarrao']
# mercado.sort()
# print(mercado)

###################### LISTA (ordenar por tamanho)
# mercado = ['paozinho', 'arroz', 'queijo provolone', 'macarrao']
# tamanho = sorted(mercado, key=len)
# print(tamanho)

###################### LISTA (ordenar maior para menor)
# num = [9,5,8,3,4]
# num.sort(reverse = True) #se for do menor para o maior, basta apenas remover o reversr deixando apenas o sort() 
# print(num)

###################### COVERSÃO DE TEMPERATURA
# para = 'C'
# temperatura = 77

# if para == 'F':
#     i = (temperatura * 1.8) + 32
#     print(i, "Fahrenheit")

# elif para == 'C':
#     i = (temperatura - 32) / 1.8
#     print(i)

#~############################### DIA 2 ####################################

###################### INTERAÇÃO COM INPUT
# nome = input('Digite seu nome: ')
# print('Olá,', nome)

###################### While (adivinhação)
# import random  
# acerto = False

# while acerto != True:
#     num = random.randint(1,10)
#     guess = int(input('Adivinhe o número: '))

#     if guess != num:
#         print('errou, numero sorteado era: ', num)
#     if guess == num:
#         acerto = True
#         print('acertou, o numero era: ', num)
        
###################### While (operações)
# op = str
# num1 = int
# num2 = int

# while op != "!":
#     num1 = int(input('digite um numero: '))

#     op = input('qual operação? ')
    
#     if op not in ['+', '-', '*', '/', '!']:
#         print('Operação desconhecida, opeação aceita somente + ! - * / ')
#         continue
#     elif op == '!':
#         print("SAIR")
#         break

#     num2 = int(input('digite um numero: '))

#     if op == '+':
#         result = num1 + num2
#     if op == '*':
#         result = num1 * num2
#     if op == '-':
#         result = num1 - num2
#     if op == '/':
#         result = num1 / num2

#     print(num1, op, num2, '=', result)    

###################### FUNÇÕES e MANITULAÇÃO DE ARRAY
def func():
 contador = 0
 lista = []
 lista1 = []
 lista2 = []

 while contador < 5:
    n = int(input('digite um número: '))

    lista.append(n)

    if n % 2 == 1:
        lista1.append(n)
    else:
        lista2.append(n)

    contador += 1

 print(lista)
 print('Lista ímpar: ', lista1)
 print('Lista par: ', lista2)

#func()

###################### CONTADOR VOGAIS
def vogais():
    text = input('insira o texto para verificar: ')
    contador = 0

    for vogais in 'aeiou':
        contador += text.count(vogais)
    
    print(contador)

#vogais()

###################### VERIFICA SE É PALINDROMO
def palindromo():
    texto = input('digite: ')
    textoSemEspaco = texto.replace(' ', '')
    textoLower = textoSemEspaco.lower()
    textoInvertido = textoLower[::-1]
    
    if textoInvertido == textoLower:
        print('É palíndromo: ', textoInvertido, textoLower)
    else:
        print('Não é palíndromo: ', textoInvertido, textoLower)

#palindromo()

###################### DATA E HORA
def datahora():
    from datetime import date
    import datetime
    import time

    hoje = date.today()
    hojeF= hoje.strftime('%d/%m/%y')

    print(hojeF)

    while True:    
        agora = datetime.datetime.now()

        formatacao = agora.strftime("%H:%M:%S")

        print(formatacao)

        time.sleep(1)

#datahora()