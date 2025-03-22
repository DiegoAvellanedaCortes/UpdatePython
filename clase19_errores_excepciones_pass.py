"""
Errores:
    - SyntaxError: Error de sintaxis
    - NameError: Error de nombre
    - TypeError: Error de tipo
    - ValueError: Error de valor
    - IndexError: Error de indice
"""

#solución de errores
try:
    divisor=int(input("Ingresa un número divisor: "))
    result=100/divisor
    print(f"El resultado es: {result}")
except ZeroDivisionError as e: #Usamos e para nombr
    print(f"División por cero: {e}")
except ValueError as e:
    print(f"Tipo de dato no valido: {e}")


#Tipos de errores -> Clases

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)
