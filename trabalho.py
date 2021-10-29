import numpy as np
from decimal import Decimal
import os





#Métodos para os Exercicios

#método para limpar a consola ao voltar ao menu
def clearConsole():
    #utilizamos o metodo system da libraria OS para correr o comando Clear.
    os.system("clear")

#método de converção de um numero inteiro ou decimal para binário.
def binary(num):
    try:
        # começo por transformar o float numa string onde irei usar a funçao split para fazer a divisão do numero inteiro e o numero decimal (parto o numero no pointer (.)).
        num = str(num).split(".")
        # escrevo uma condição para quando o numero introduzido para conversao se trata de inteiro ou decimal (um numero sem casas decimais não necessita de ser partido
        # durante a conversão)
        if(len(num) > 1):
            # se o tamanho da lista num for maior que 1, significa que o numero tem casas decimais
            # de seguida converto de volta o numero da metade inteira em int utilizo a função bin() para obter o binário da metade inteira
            metade_inteira_binario = bin(int(num[0]))
            # como a função bin() não aceita numeros não inteiros e como, numa representação binaria de um numero não inteiro, utilizar a função bin() na metade decimal não funciona.
            # (Porque na representação correta o lado decimal depende do lado inteiro)
            # Para resolver isso, irei calcular o lado decimal à mão para obter a representação correta.
            # Para tal começo para transformar a parte decimal num float com 0 como inteiro, ou seja num numero 2.534, eu divido os dois numeros e fico com 2 e 534. De seguida,
            # transformo a string 534 num float 0.534 para efetuar os calculos da conversão
            metade_decimal = float("0.%s" % num[1])
            metade_decimal_binario = ""
            # crio um ciclo que irá manter-se até que o float (0.534 por exemplo fique com o valor de 0)
            while metade_decimal != 0:
                # começo por multiplicar o numero por 2 ou somar o numero por si proprio
                metade_decimal = metade_decimal + metade_decimal
                # e verifico se a sua casa antes do floating point é maior que 0, para tal subtraio o numero por 1 e verifico se o resultado da subtração é menor que 0
                if(metade_decimal - 1 < 0):
                    # se for menor, significa que não tenho onde tirar 1 valor por isso adiciono 0 à string do binário
                    metade_decimal_binario += "0"
                else:
                    # se for maior, significa que tenho onde tirar 1 valor por isso adiciono 1 à string do binário e subtraio a metade_decimal por 1
                    metade_decimal = metade_decimal - 1
                    metade_decimal_binario += "1"
            #depois de um certo operações onde o metade_decimal fica com o valor de 0, entao a conversão esta completa e retorno uma string com a metade inteira e decimal convertidas
            return "%s.%s" % (metade_inteira_binario, metade_decimal_binario)
        else:
            # como sei que de outra forma, o numero é inteiro. Returno o resultado da conversao com o metodo Bin() do numero.
            return bin(int(num[0]))
    except ValueError:
        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
        print("\n Foi encontrado um erro durante a conversão! Por Favor tente mais tarde.\n".encode('utf8').decode('iso-8859-1'))

def exercicio1():
    #indico ao python que quero utilizar uma variavel global ao programa que se encontra fora do método
    #esta variavel menu_active servirá para que possa navegar de volta para o menu sempre que desejar, dentro do exercicio 1
    global menu_active 
    active = True
    while active:
        try:
            print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")
            #Inicialização e Requesito do valor X
            print("\u001b[30m\u001b[47m\u001b[1m_________________Exercicio 1__________________\u001b[0m\u001b[0m\u001b[0m\n")
            # 1 - Dou grab do input do user que necessitará de ser um float senão a exception será chamada
            # 2 - A razão pelo qual eu guardo o input como float() em vez de Decimal() é porque desta forma
            #  posso validar qualquer tipo de input errado numa so linha e de seguida converter esse input para Decimal.  
            x = float(input("Introduza o valor de X (inteiro ou decimal) - "))
            x = Decimal('%s' % x)
            # 3 - De seguida calculo o valor de Y utilizando o input do utilizador.
            # NOTA - Note que utilizo a função de calculo da SquareRoot da libraria Decimal porque não é possivel calcular
            # variaveis Decimal utilizando a função sqrt() do python (que aceita apenas floats ou inteiros). 
            y = x**2 + Decimal.sqrt(x) + 2
            # 4 - Por fim arredondo o resulta de Y em 2 casas decimais
            y = round(y, 2)
            print("---------\u001b[32mResultado\u001b[0m----------\n")
            print(" Y = %s" % y)
            print("\n----------------------------")

            #crio um ciclo para perguntar ao utilizar se deseja ou não fazer a conversão e se quer manter-se no exercicio 1 com uma nova entrada ou voltar ao menu 
            perg1_respondida = False
            while perg1_respondida == False:
                try:
                    # Se o user desejar converter:
                    # Pergunto ao utilizador se deseja converter o resultado para Binário ou Hexadecimal e guardo a resposta na variavel per1_resposta.
                    print("______________________________________________________________________________________________\n")
                    perg1_resposta = int(input("Deseja converter o resultado para Binário ou Hexadecimal (1 = sim |2 = não)? ".encode('utf8').decode('iso-8859-1')))
                    if perg1_resposta == 1:
                        #se a resposta for 1 então dou a primeira pergunta como respondida perg1_respondida = true
                        perg1_respondida = True
                        #seguindo a mesma lógica, pergunto de seguida ao utilizador se deseja binário ao decimal.
                        perg2_respondida = False
                        while perg2_respondida == False:
                            try:
                                print("______________________________________________________________________________________________\n")
                                print("      Binário[1]          Hexadecimal[2] \n".encode('utf8').decode('iso-8859-1'))
                                perg2_resposta = int(input("Seleciona uma das opções: ".encode('utf8').decode('iso-8859-1')))
                                #quando o utilizador seleciona uma das duas opções permitidas, a conversão é executada e devolvida ao utilizador
                                if perg2_resposta == 1:
                                    perg2_respondida = True
                                    print("__________________\u001b[32mConversão para Binário\u001b[0m__________________\n".encode('utf8').decode('iso-8859-1'))
                                    print("O número %s em binário é representado por %s.\n".encode('utf8').decode('iso-8859-1') % (y, binary(y)))
                                    #depois de devolver o resultado ao utilizador, pergunta-mos se o mesmo quer continuar no exercicio 1 ou retornar ao menu
                                    perg3_respondida = False 
                                    while perg3_respondida == False:
                                        try:
                                            print("\n______________________________________________________________________________________________\n")
                                            perg3_resposta = int(input("Deseja continuar no Exercicio 1 ou voltar ao Menu? (1 = Continuar |2 = Voltar ao Menu)? "))
                                            #se a resposta do utilizador for 1:
                                            #           1- declaramos a pergunta como respondida, para sair do ciclo da pergunta. perg3_respondida = true
                                            #           2- mantemos a variavel active a true para que o utilizador volte ao inicio do ciclo do exercicio
                                            if perg3_resposta == 1:
                                                perg3_respondida = True
                                                active = True
                                            #se a resposta do utilizador for 2:
                                            #           1- declaramos a pergunta como respondida, para sair do ciclo da pergunta. perg3_respondida = true
                                            #           2- passamos a variavel active a falso para que o user saia do ciclo da pergunta e retorne ao menu
                                            #           3- passamos a variavel global do menu a true para que quando o utilizador sair do metodo do exercicio
                                            # dentro do ciclo do menu, volte a ser imprimido o mesmo.
                                            #           4- damos clear á consola através do metodo escrito anteriorment clearConsole()
                                            elif perg3_resposta == 2:
                                                perg3_respondida = True
                                                active = False
                                                menu_active = True
                                                clearConsole()
                                            #erro da validação da resposta á perg3
                                            else:
                                                print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                                                print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                                        #erro da validação da resposta á perg3
                                        except ValueError:
                                            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                                            print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                                elif perg2_resposta == 2:
                                    perg2_respondida = True
                                    print("__________________\u001b[32mConversão para Hexadecimal\u001b[0m__________________\n".encode('utf8').decode('iso-8859-1'))
                                    print("O número %s em hexadecimal é representado por %s.\n".encode('utf8').decode('iso-8859-1') % (y, float.hex(float(y))))
                                    #depois de devolver o resultado ao utilizador, pergunta-mos se o mesmo quer continuar no exercicio 1 ou retornar ao menu
                                    perg3_respondida = False 
                                    while perg3_respondida == False:
                                        try:
                                            print("\n______________________________________________________________________________________________\n")
                                            perg3_resposta = int(input("Deseja continuar no Exercicio 1 ou voltar ao Menu? (1 = Continuar |2 = Voltar ao Menu)? "))
                                            #se a resposta do utilizador for 1:
                                            #           1- declaramos a pergunta como respondida, para sair do ciclo da pergunta. perg3_respondida = true
                                            #           2- mantemos a variavel active a true para que o utilizador volte ao inicio do ciclo do exercicio
                                            if perg3_resposta == 1:
                                                perg3_respondida = True
                                                active = True
                                            #se a resposta do utilizador for 2:
                                            #           1- declaramos a pergunta como respondida, para sair do ciclo da pergunta. perg3_respondida = true
                                            #           2- passamos a variavel active a falso para que o user saia do ciclo da pergunta e retorne ao menu
                                            #           3- passamos a variavel global do menu a true para que quando o utilizador sair do metodo do exercicio
                                            # dentro do ciclo do menu, volte a ser imprimido o mesmo.
                                            #           4- damos clear á consola através do metodo escrito anteriorment clearConsole()
                                            elif perg3_resposta == 2:
                                                perg3_respondida = True
                                                active = False
                                                menu_active = True
                                                clearConsole()
                                            #erro da validação da resposta á perg3
                                            else:
                                                print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                                                print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                                        #erro da validação da resposta á perg3
                                        except ValueError:
                                            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                                            print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                                #erro da validação da resposta á perg2
                                else:
                                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                                    print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                            #erro da validação da resposta á perg2
                            except ValueError:
                                print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                                print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                    elif perg1_resposta == 2:
                        #Mesma logica utilizada anteriormente para voltar ao menu
                        perg1_respondida = True
                        perg3_respondida = False 
                        while perg3_respondida == False:
                            try:
                                print("\n______________________________________________________________________________________________\n")
                                perg3_resposta = int(input("Deseja continuar no Exercicio 1 ou voltar ao Menu? (1 = Continuar |2 = Voltar ao Menu)? "))
                                if perg3_resposta == 1:
                                    perg3_respondida = True
                                    active = True
                                elif perg3_resposta == 2:
                                    perg3_respondida = True
                                    active = False
                                    menu_active = True
                                    clearConsole()
                                else:
                                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                                    print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                            except ValueError:
                                print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                                print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                    else:
                        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                        print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                except ValueError:
                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                    print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
        except ValueError:
            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
            print("\nFoi atribuido um valor não permito, por favor introduza novamente um valor inteiro ou decimal! (Exemplo: 2.4)\n".encode('utf8').decode('iso-8859-1'))

def exercicio2():
    global menu_active
    active = True
    while active:
        try:
            print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")
            print("\u001b[30m\u001b[47m\u001b[1m_________________Exercicio 2__________________\u001b[0m\u001b[0m\u001b[0m\n")
            #crio as matrizes com as mesmas dimensões que o enunciado
            matriz1 = np.array([[1, 0 ,2],[-1,3,1]])
            matriz2 = np.array([[3,1], [2,1], [1,0]])

            print("""
    \u001b[34;1mMatriz1                     Matriz2\u001b[34;0m
...............                .........
| 1    0    2 |       X        | 3   1 |
|-1    3    1 |                | 2   1 |
                               | 1   0 |
                    
                  \u001b[32;1mResultado\u001b[32;0m
                      |
                      V""")
            #multiplico as matrizes com o operador @
            resultado_multi = matriz1@matriz2
            print("""   
                  .........
                  | %s    %s|
                  | %s    %s| 
            """ % (resultado_multi[0][0], resultado_multi[0][1], resultado_multi[1][0], resultado_multi[1][1]))
            #transformo o resultado na sua transposta
            transposta = resultado_multi.transpose()
            print("""
                 \u001b[33;1m*Transposta*\u001b[33;0m  
                  .........
                  | %s    %s|
                  | %s    %s| 
            """ % (transposta[0][0], transposta[0][1], transposta[1][0], transposta[1][1]))
            
            #imprimo os endereços de memoria dos objetos resultado_multi e transposta através do metódo id()
            print("O endereço do objeto do resultado da multiplicação em memóra é %s.".encode('utf8').decode('iso-8859-1') % id(resultado_multi))
            print("O endereço do objeto da transposta do resultado da multiplicação em memória é %s.\n".encode('utf8').decode('iso-8859-1') % id(transposta))
            print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")

            #volto ao menu com a mesma forma logica explicada no exercicio 1
            respondido = False
            while respondido == False:
                try:
                    perg1_resposta = int(input("Introduza [1] para voltar ao menu de navegação! ".encode('utf8').decode('iso-8859-1')))
                    respondido = True
                    if perg1_resposta == 1:
                        menu_active = True
                        active = False
                        clearConsole()
                    else:
                        respondido = False
                        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                        print("\nNão foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                except ValueError:
                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                    print("\nNão foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
        except ValueError:
            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
            print("\nAlgo correu mal do código do exercicio. Volte a tentar mais tarde!\n".encode('utf8').decode('iso-8859-1'))

def exercicio3():
    global menu_active
    active = True
    while active:
        try:
            print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")
            print("\u001b[30m\u001b[47m\u001b[1m_________________Exercicio 3__________________\u001b[0m\u001b[0m\u001b[0m\n")
            #começo por criar uma lista vazia e declarar um variavel boleana para saber quando é que as entradas terminaram
            listar = True
            lista = []
            count = 0
            #crio um ciclo que irá ser executado constantemente enquanto a boleana listar continuar a verdadeiro
            while listar:
                # em cada entrada é validado o input do user, aceitando apenas numeros inteiros(inicialmente)
                nova_entrada = int(input("Introduza um valor inteiro positivo á lista([-1] encerra as entradas e devolve o output):  ".encode('utf8').decode('iso-8859-1')))
                # se o valor introduzido for maior que 0, adiciono o valor á lista e imprimo o nº da entrada com o seu respetivo valor
                if nova_entrada > 0:
                    count = count + 1
                    lista.append(nova_entrada)
                    print("\u001b[32;1mEntrada nº %s = %s\u001b[32;0m".encode('utf8').decode('iso-8859-1') % (count, nova_entrada))
                # se o valor for -1 então altero a boleana listar para falso e inicio as operaçoes sobre a lista introduzida
                elif nova_entrada == -1:
                    listar = False
                    if len(lista) == 0:
                        print(".............................................................................................")
                        print("\n\u001b[31;1mNão é possivel efetuar operações devido a lista se encontrar vazia!\u001b[31;0m\n".encode('utf8').decode('iso-8859-1'))
                    else:
                        print(".............................................................................................")
                        #primeiro imprimo a lista no seu estado originalmente introduzido
                        print("\nLista ---> %s\n" % lista)
                        #segundo imprimo o resultado da soma de todos os valores na lista com recurso ao metodo sum()
                        print("\nSoma de todos os valores na lista ---> %s\n" % sum(lista))
                        #terceiro imprimo o valor mais alto na lista com recurso ao metodo max()
                        print("\nValor Máximo na lista ---> %s\n".encode('utf8').decode('iso-8859-1') % max(lista))
                        #quarto imprimo o valor mais baixo na lista com recurso ao metodo min()
                        print("\nValor Minimo na lista ---> %s\n" % min(lista))
                        #quinto imprimo a lista com ordem ascendente com recurso ao metodo sorted()
                        print("\nLista ordenada ascendente ---> %s\n" % sorted(lista))
                        print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")
                    
                    #por fim volto a utilizar um ciclo while para perguntar ao usar se quer dar nova entrada ao exercicio 3 ou voltar ao menu (como no resto dos exercicios)
                    perg_respondida = False
                    while perg_respondida == False:
                        try:
                            perg_resposta = int(input("Deseja continuar no Exercicio 3 ou voltar ao Menu? (1 = Continuar |2 = Voltar ao Menu)? "))
                            if perg_resposta == 1:
                                perg_respondida = True
                                active = True
                            elif perg_resposta == 2:
                                perg_respondida = True
                                active = False
                                menu_active = True
                                clearConsole()
                            else:
                                print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                                print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                        except ValueError:
                            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                            print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                # qualquer valor inteiro negativo (sem contar com o -1) sera descartado como entrada não permitida
                else:
                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                    print("\n Valor de entrada deve ser positivo ou (-1) para encerrar as entradas.\n".encode('utf8').decode('iso-8859-1'))

        except ValueError:
            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
            print("\nFoi atribuido um valor não permito, por favor volte novamente a introduzir todos valores para a lista (os valores devem ser inteiros e positivos).\n".encode('utf8').decode('iso-8859-1'))

def exercicio4():
    global menu_active
    active = True
    ex = True
    while active:
        while ex:
            try:
                print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")
                print("\u001b[30m\u001b[47m\u001b[1m_________________Exercicio 4__________________\u001b[0m\u001b[0m\u001b[0m\n")
                #valido entrada de A e converto o int para bool
                try:
                    a = int(input("Introduza o valor de A (1 = true | 0 = false): "))
                    if a == 1:
                        a = True
                    elif a == 0:
                        a = False
                    else:
                        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                        print("\n Não foi introduzida uma opção permitida para o valor de A.\n".encode('utf8').decode('iso-8859-1'))
                        break
                except ValueError:
                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                    print("\nFoi atribuido um valor não permitido, por favor volte novamente.\n".encode('utf8').decode('iso-8859-1'))
                    break
                #valido entrada de B e converto o int para bool
                try:
                    b = int(input("\nIntroduza o valor de B (1 = true | 0 = false): "))
                    if b == 1:
                        b = True
                    elif b == 0:
                        b = False
                    else:
                        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                        print("\nNão foi introduzida uma opção permitida para o valor de B.\n".encode('utf8').decode('iso-8859-1'))
                        break
                except ValueError:
                    print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                    print("\nFoi atribuido um valor não permitido, por favor volte novamente.\n".encode('utf8').decode('iso-8859-1'))
                    break
            
                #utilizo o operador logico "and" para obter o resultado esperado
                resultado = a and b
                #imprimo o resultado com alguma formatação
                print("\n---------\u001b[32mResultado\u001b[0m----------\n")
                print("\n A (%s) ^ B (%s) = %s\n" % (a,b,resultado))
                print("\u001b[34;1m---------------------------------------------------------------------------\u001b[34;0m")
                #por fim volto a utilizar um ciclo while para perguntar ao usar se quer dar nova entrada ao exercicio 4 ou voltar ao menu (como no resto dos exercicios)
                perg_respondida = False
                while perg_respondida == False:
                    try:
                        perg_resposta = int(input("Deseja continuar no Exercicio 4 ou voltar ao Menu? (1 = Continuar |2 = Voltar ao Menu)? "))
                        if perg_resposta == 1:
                            perg_respondida = True
                            active = True
                        elif perg_resposta == 2:
                            perg_respondida = True
                            active = False
                            menu_active = True
                            ex = False
                            clearConsole()
                        else:
                            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                            print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
                    except ValueError:
                        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                        print("\n Não foi introduzida uma opção permitida.\n".encode('utf8').decode('iso-8859-1'))
            except ValueError:
                print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
                print("\nAlgo correu mal com programa no exercicio 4. Por favor tente mais tarde.\n".encode('utf8').decode('iso-8859-1'))

#Opener com informação relevante á aplicação
print("""\u001b[34m
 _______  _______ _________ _______  _______  _______ __________________ _______  _______    ______  _________ _______  _______  _______  _______ _________ _______ 
(       )(  ___  )\__   __/(  ____ \(       )(  ___  )\__   __/\__   __/(  ____ \(  ___  )  (  __  \ \__   __/(  ____ \(  ____ \(  ____ )(  ____ \\__   __/(  ___  )
| () () || (   ) |   ) (   | (    \/| () () || (   ) |   ) (      ) (   | (    \/| (   ) |  | (  \  )   ) (   | (    \/| (    \/| (    )|| (    \/   ) (   | (   ) |
| || || || (___) |   | |   | (__    | || || || (___) |   | |      | |   | |      | (___) |  | |   ) |   | |   | (_____ | |      | (____)|| (__       | |   | (___) |
| |(_)| ||  ___  |   | |   |  __)   | |(_)| ||  ___  |   | |      | |   | |      |  ___  |  | |   | |   | |   (_____  )| |      |     __)|  __)      | |   |  ___  |
| |   | || (   ) |   | |   | (      | |   | || (   ) |   | |      | |   | |      | (   ) |  | |   ) |   | |         ) || |      | (\ (   | (         | |   | (   ) |
| )   ( || )   ( |   | |   | (____/\| )   ( || )   ( |   | |   ___) (___| (____/\| )   ( |  | (__/  )___) (___/\____) || (____/\| ) \ \__| (____/\   | |   | )   ( |
|/     \||/     \|   )_(   (_______/|/     \||/     \|   )_(   \_______/(_______/|/     \|  (______/ \_______/\_______)(_______/|/   \__/(_______/   )_(   |/     \|
                                                                                                                                                                    
                                                                                                                                                                    \u001b[0m""")
print("\u001b[1m\u001b[4m   *** Bem Vindo ao trabalho desenvolvido no intuito da cadeira \n de Matemática Discreta do TIWM - Bruno Monteiro e João Almeida ***\n Por favor utilize o menu de selecção para navegar pela aplicação!\n\u001b[0m".encode('utf8').decode('iso-8859-1'))
print("\u001b[33m!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?\u001b[0m")
print("      Continuar[1]                  Sair[2]")
print("\u001b[33m!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?\n\u001b[0m")
resp = 0
while resp != 1 and resp != 2:
    #Fortalecer contra input que não se trate de um int (strings, especial characters, etc..)
    try:
        resp = int(input("Deseja continuar?   "))
        #Check if int as the value 1 or 2, otherwise same error message.
        if resp == 1:
            menu_active = True
        elif resp == 2:
            menu_active = False
            break
        else:
            print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
            print("\nNão foi introduzida uma opção disponivel, por favor tente novamente!\n".encode('utf8').decode('iso-8859-1'))
    except ValueError:
        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
        print("\nNão foi introduzida uma opção disponivel, por favor tente novamente!\n".encode('utf8').decode('iso-8859-1'))
    

#Menu da Aplicação

#criamos um dicionario com as opções do menu
menu = {}
menu['1']="Exercicio 1"
menu['2']="Exercicio 2"
menu['3']="Exercicio 3"
menu['4']="Exercicio 4"
menu['5']="Exit"

#criamos um ciclo onde o menu corre infinitamente ate que o valor de menu_active seja falso
while menu_active:
    print("\n\u001b[36m///////////////// Menu de Navegação ///////////////////\n\u001b[0m".encode('utf8').decode('iso-8859-1'))
    options=menu.keys()
    #imprimo o dicionario com um ciclo for onde junto as keys com os seus respetivos valores numa so string impressa
    for entry in options:
        print("Opção[%s] - %s\n".encode('utf8').decode('iso-8859-1') % (entry,menu[entry]))
    #requer uma opção das listadas ao utilizador
    selection=input("Seleciona uma das opções: ".encode('utf8').decode('iso-8859-1'))
    #se for uma opção valida para os respetivos exercicios:
    #      1- Menu_active passa a false (para que o menu não seja constatemente aberto dentro dos exercicios)
    #      2- E executo um metodo do exercicio escolhido pelo utilizador 
    if selection =='1':
        menu_active = False
        exercicio1() 
    elif selection == '2':
        menu_active = False
        exercicio2()
    elif selection == '3':
        menu_active = False
        exercicio3()
    elif selection == '4':
        menu_active = False
        exercicio4()
    elif selection == '5':
        #se a opção for sair, então partimos o ciclo do menu, que terminara o programa 
        break
    #se for inserida uma opção que não seja permitida, será devolvido uma mensagem de erro que, como o menu_active continua a verdadeiro, retorna o utilizador ao menu 
    else:
        print("\n\u001b[31;1m********************ERROR***********************\n\u001b[31;0m")
        print("\nNão foi introduzida uma opção disponivel, por favor tente novamente!\n".encode('utf8').decode('iso-8859-1'))




    