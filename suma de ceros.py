def suma_de_ceros(num):
    if isinstance (num,int):
        if num<0:
            return suma_de_ceros(num*-1)
        elif num>=0 and num < 10:
            return 0
        else:
            if num%10==0:
                return 1+suma_de_ceros(num//10)
            else:
                return suma_de_ceros(num//10)
        
                                                        



def suma_de_ceros2(num):
    if isinstance (num,int)and num>=0:
        if num==0:
            return 1
        elif num>0 and num < 10:
            return ("false")
        else:
            if num%10==0:
                print ('true')
            else:
                return suma_de_ceros2(num//10)

def suma_de_ceros3(num):
    if isinstance(num,int) and num>=0:
        if num == 0:
            return ('true')
        elif num>=1 and num<=9:
            return ('false')
        else:
            if num%10==0:
                return true
            else :
                return suma_de_ceros3
