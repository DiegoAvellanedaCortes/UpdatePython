"""
def factorial recibe como parametro un número del cual queremos conocer su factorial

1. Realiza la validación si es Cero y si es así arroja como resultado 1
2. Realiza el proceso, suponiento de n=3 

    n=3
    3*factorial(3-1)
    3*factorial(2)

    n=2
    2*factorial(2-1)
    2*factorial(1)
    
    n=1
    1*factorial(1-1)
    1*factorial(0)

    En este caso se detiene la ejecución porque tenemos como resultado 0, pero n nunca llega a ser 1
"""


def factorial(n):
    if n==0:
        return 1 
    else:
        return n*factorial(n-1)


print(factorial(5))


"""
Serie Fibonacci

El atributo n corresponde a la posición, no a al valor

Formula: fibonacci(n-1)+fibonacci(n-2)

    Para obtener el valor de Fibonacci necesitamos conocer la posición anterior fibonacci(n-1) y conocer el valor de dos posiciones anteriores tambien fibonacci(n-2)

    Como la serie comienza desde la segunda posición es factible hacerlo. 
    Posición 0 = 0
    Posición 1 = 1

    En este caso para conocer la posición 2 hacemos n=2 
    --> fibonacci(n-1) 
       -Reemplazamos -> fibonacci(2-1) 
       -Resultado -> fibonacci(1) -> El valor para fibonacci en la posición 1 es 1
    --> fibonacci(n-2)
       -Reemplazamos -> fibonacci(2-2) 
       -Resultado -> fibonacci(0) -> El valor para fibonacci en la posición 0 es 0

       fibonacci(n-1)+fibonacci(n-2)=Valor fibonacci para nueva posición ej fibonacci(2)
              1      +        0     = 1         
"""
def fibonacci(n):
    if n==0 or n==1 :
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(f"Fibonacci->",fibonacci(6))

def sumatoria(n):
    if n==0 or n==1:
        return n
    else:
        return n+sumatoria(n-1)

print(f"Sumatoria->",sumatoria(5))