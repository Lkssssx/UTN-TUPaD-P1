# Utils
def valid_input(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))

    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n


# Ejercicio 1)
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
    
num = valid_input("Ingrese un número entero positivo", 1)

for i in range(num, 0, -1):
    print(f"El factorial de {i} es: {factorial(i)}")


# Ejercicio 2)
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

num = valid_input("Ingrese un número entero positivo", 1)

for i in range(num, 0, -1):
    print(f"En la posicion {i} obtenemos el valor de fibonacci: {fibonacci(i)}")


# Ejercicio 3)
def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)
    
n = valid_input("Ingrese un número entero para la base")
m = valid_input("Ingrese otro número entero para el exponente")

print(f"{n} ^ {m} = {potencia(n, m)}")


# Ejercicio 4)
def binario(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
       return f"{binario(x//2)}{x % 2}"

num = valid_input("Ingrese un número entero positivo", 1)

print(f"{num} en binario es: {binario(num)}")


# Ejercicio 5)
def es_palindromo(palabra):
    if palabra == "":
        return ""
    else:
        return f"{"".join(list(palabra).pop(len(palabra) - 1))}{es_palindromo((palabra)[:len(palabra) - 1])}"
    
palabra = input("Ingrese una palabra: ")

print(es_palindromo(palabra))


# Ejercicio 6)
def suma_digitos(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n % 10 + suma_digitos(n//10)

n = valid_input("Ingrese un número entero positivo", 1)

print(suma_digitos(n))


# Ejercicio 7)
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

n = valid_input("Ingrese un número entero positivo", 1)

print(contar_bloques(n))


# Ejercicio 8)
def contar_digito(numero, digito):
    numero_lista = list(str(numero))

    if str(digito) not in numero_lista:
        return 0
    else:
        numero_lista.remove(str(digito))
        if numero_lista == []:
            return 1
        return 1 + contar_digito(int("".join(numero_lista)), digito)

numero = valid_input("Ingrese un número entero positivo", 1)
digito = valid_input("Ingrese un digito de ese número", 0, 9)

print(contar_digito(numero, digito))
