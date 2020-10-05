def multiplicar(num, pot):
    if isinstance(num,int) and isinstance(pot,int) and pot >= 0:
        if pot == 0:
            return 0
        else:
            return num + multiplicar(num, pot-1)
    else:
        print("error en las entradas")

def dividir(dividendo,divisor):
    if isinstance (dividendo,int) and isinstance (divisor,int):
        if dividendo == dividendo - divisor:
            return dividendo - divisor
        elif dividendo == 0:
            return divisor + 1
        else:
            dividendo = dividendo
            return dividendo - divisor


