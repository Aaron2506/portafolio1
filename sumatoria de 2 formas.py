def sumatoria (num):
    if num == 0:
        return 0
    else :
        return num+sumatoria(num-1)

def suma (num):
    if isinstance (num,int)and num>=0:
        return (sumatoria==sumatoria)
    else:
        print("error en la entrada")

#segunda forma de sumatoria
def sumatoria_simple(n):
    return n* (n+1)//2




def cilindro (altura,radio):
    if isinstance(altura,int)and isinstance(radio,int):
        return 2*3.14*radio*(altura+radio)
    else:
        return ('no esta digitando un numero entero')


def calculadora(op1,op2,operador):
    if operador == 'multiplicacion':
        return op1*op2
    elif operador == 'division':
        return op1/op2
    elif operador == 'resta':
        return op1-op2
    elif operador == 'suma':
        return op1+op2
    else:
        return ('Error en las entradas recuerde 2 numeros enteros o flotantes y un str con su operador')







    



