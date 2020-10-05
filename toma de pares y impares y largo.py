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

#***************************************************************************


def largoN(num):
    if isinstance(num,int)and num>0:
        if num<10:
            return 1
        else:
            return 1+largoN(num//10)
def invertir(num):
    if isinstance(num,int)and num>=0:
        pot=largoN(num)-1
        return invaux(num,pot)
    else:
        return-1

def invaux(num,pot):
    if pot==0:
        return num
    else:
        return ((num%10)*10**pot)+invaux(num//10,pot-1)


######################################################################

def toma_de_impares2(num):
    if isinstance (num,int)and num>0:
        return tpAU(num,0)
    else:
        return -1

def tpAU(num,lol):
    if num==0:
        return 0
    else:
        if (num%10)%2==1:
            return (num%10)*10**lol+tpAU(num//10,lol+1)
        else:
            return tpAU(num//10,lol)




def fibo(num):
    if isinstance(num,int)and num >= 0:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        elif num<0:
            return fibo(num*-1)
        elif num > 1:
            return toma_de_impares2(num)


def fibo2(num):
    if isinstance(num,int)and num >= 0:
        if num == 0:
            return 0
        elif num == 1:
            return 1
        elif num<0:
            return fibo(num*-1)
        elif fibo(num):
            return fibo(num -1)+fibo(num-2)
    else:
        return -1



    
        
        



















################################################################


def pares(num):
    if isinstance(num,int):
        if(num%10)%2 == 0:
            return ('true')
        elif (num%10)%2==1:
            return('false')


        


        













                   
