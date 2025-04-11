# Ejercicio 1
for i in range(101):
    print(i);


# Ejercicio 2
num = input("Ingrese un número entero: ");
count = 0;

for digit in num:
    count += 1;

print("El número", num, "tiene", count, "dígitos.");

# Ejercicio 3
num1 = int(input("Ingrese un número: "));
num2 = int(input("Ingrese otro número: "));
max = num1;
min = num2;

if max < min: 
    max = num2;
    min = num1;

for i in range(min + 1, max):
    print(i);


# Ejercicio 4
num = int(input("Ingrese un número a sumar: "));
count = 0;

while num != 0:
        count += num;
        num = int(input("Ingrese otro número a sumar: "));

print("La suma de todos los números da:", count);


# Ejercicio 5
from random import randint;

num = int(input("Adivina el número del 0 al 9: "));
random_num = randint(0, 9);
count = 0;

while num != random_num:
    count += 1;
    num = int(input("Incorrecto. Vuelva a intentarlo: "));
count += 1;
print("Correcto! El número era", random_num, ". Fueron necesarios", count, "intentos");


# Ejercicio 6
for i in range(100, 0, -2):
     if i % 2 == 0:
          print(i);


# Ejercicio 7
num = int(input("Ingrese un número: "));

for i in range(1, num):
     print(i);


# Ejercicio 8
num = 0
even = 0;
odd = 0;
positive = 0;
negative = 0;

for i in range(100):
     num = int(input("Ingrese 100 números: "));

     if num % 2 == 0:
         even += 1;
     elif num % 2 != 0:
         odd += 1;
    
     if num > 0:
         positive += 1;
     elif num < 0:
         negative += 1;

print("Números pares:", even);
print("Números impares:", odd);
print("Números positivos:", positive);
print("Números negativos:", negative);

# Ejercicio 9
num = 0
count = 0
sum = 0
median = 0
for i in range(100):
     num = int(input("Ingrese 100 números: "));
     count += 1
     sum += num

median = sum / count

print("La media de los 100 números es:", median)


# Ejercicio 10
num = int(input("Ingrese un número: "))
numList = list(str(num))

numList.reverse()

print("".join(numList))

