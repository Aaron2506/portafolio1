#funcion para calcular el area de un rombo
#entrada: dos numeros enteros
#salida: el resultado del area
#restricciones:deben ser solo 2 numeros enteros

def area_de_un_rombo(DM,dm):
    if isinstance(DM,int) and isinstance(dm,int):
        return (DM*dm)/2

#funcion para calcular el area de un trapecio
#entrada:3 numeros enteros
#salida:resultado del area de un trapecio
#restricciones: debe ser numero entero

def area_de_un_trapecio(B,b,h):
    if isinstance(B,int)and isinstance(b,int)and isinstance(h,int):
        return (B+b)*h/2

# funcion que indica a cual provinvia pertenece
# entradas:un numero de cedula
# salidas: indicar la provincia
# restricciones: debe ser un numero entero positivo

def mi_provincia(num):
    if isinstance(num,int):
        if num//100000000 == 1:
            return ("san jose")
        elif num//100000000 == 2:
            return ('alajuela')
        elif num//100000000 == 3:
            return ('cartago')
        elif num//100000000 == 4:
            return ('heredia')
        elif num//100000000 == 5:
            return ('guanacaste')
        elif num//100000000 == 6:
            return ('puntarenas')
        elif num//100000000 == 7:
            return ('limon')
        elif num//100000000 == 8:
            return ('nacionalizado extranjero')
        elif num//100000000 == 9:
            return ('partida especial de nacimientos(casos especiales)')


#funcion que determina si existen pares o no mediante true o false
#entrada:un numero
#salida:false si hay un impar y true solo hay pares
#restricciones:numero entero positivo

def pares(num):
    if isinstance(num,int):
        if(num%10)%2 == 0:
            return ('true')
        elif (num%10)%2==1:
            return('false')




        
