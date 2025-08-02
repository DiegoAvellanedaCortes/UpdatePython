# Iteradores -> Itera cada elemento sin usar un indice
#Ocupan menos menoria por lo tanto son más rápidos

my_list = [1, 2, 3, 4]

# Obtener iterador
my_iter = iter(my_list)

# Usar iterador
print(next(my_iter))

print(iter(my_list))


# GENERADOR -> Produce iterables uno a uno con la palabra yield 


def generador():
    yield 1
    yield 2
    yield 3


for a in generador():
    print("Generador->",a)


# Fibonacci
def fibonacci(limit):
    a, b = 0, 1
    """
    a,b=0,1 es igual a:
    a=0
    b=1
    
    """
    while a < limit:
        yield a
        a, b = b, a + b
        """
        a=b
        b=a+b
        """

for num in fibonacci(10):
    print(num)

print("----------------------------")


def num_pares(par,limite):
    a=0
    while a<limite+1:
        if par==True:
            if a % 2==0:
                yield a
        elif par==False:
            if a % 2!=0:
                yield a
        a+=1

print("-----------TRUE------------------")

for par in num_pares(True,15):
    print(par)

print("-----------False------------------")
for par in num_pares(False,15):
    print(par)


