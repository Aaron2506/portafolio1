def toma_de_pares(num):
    if isinstance (num,int)and num>0:
        return tpAUX(num,0)
    else:
        return -1

def tpAUX(num,lol):
    if num==0:
        return 0
    else:
        if (num%10)%2==0:
            return (num%10)*10**lol+tpAUX(num//10,lol+1)
        else:
            return tpAUX(num//10,lol)



def multiplicar(num,multiplicador):
    if multiplicador == 0:
        return 0
    else:
        return num+multiplicar(num,multiplicador-1)
def elevar(numero,potencia):

    if potencia == 0:
        return 1
    elif potencia == 1:
        return numero
    else:
        return multiplicar(numero,elevar(numero,potencia-1))

