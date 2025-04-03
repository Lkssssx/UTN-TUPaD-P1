# Ejercicio 1)
edad = int(input("ingrese su edad: "));

if edad >= 18: 
    print("Es mayor de edad");


# Ejercicio 2)
nota = int(input("Ingrese su nota: "));

if nota >= 6:
    print("Aprobado");
else:
    print("Desaprobado");


# Ejercicio 3)
num = int(input("Ingrese  un número: "));

if num % 2 == 0:
    print("Ha ingresado un número par");
else:
    print("Por favor ingrese un número par");


# Ejercicio 4)
edad = int(input("ingrese su edad: "));
categoria = "";

if edad < 12 and edad >= 0:
    categoria = "Niño/a";
elif edad >= 12 and edad < 18:
    categoria = "Adolescente";
elif edad > 18 and edad < 30:
    categoria = "Adulto/a joven";
elif edad >= 30:
    categoria = "Adulto/a";

print(f"Usted pertenece a la categoría de {categoria}");


# Ejercicio 5)
password = input("Ingrese una contraseña de entre 8 y 14 caracteres: ");
validator = False;

if len(password) >= 8 and len(password) <= 14:
    validator = True;
else:
    validator = False;

if validator:
    print("Ha ingresado una contraseña correcta");
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres");

# Ejercicio 6)
import random
from statistics import mode, median, mean
random_numbers = [
    random.randint(1,100) for i in range(50)
    ]

print(mode(random_numbers));
print(median(random_numbers));
print(mean(random_numbers));

# Ejercicio 7)

phrase = input("Ingrese una frase o palabra: ");

if phrase[len(phrase) - 1] in set("aeiouAEIOU"):
    print(f"{phrase}!");
else:
    print(phrase);

# Ejercicio 8)
name = input("Ingrese su nombre: ");

print("Ingrese el numero de la accion que desee realizar: ");
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.");
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.");
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.");
num = int(input());

if num == 1:
    print(name.upper());
elif num == 2:
    print(name.lower())
elif num == 3:
    print(name.title())


# Ejercicio 9)
terremoto_int = int(input("Ingrese la magnitud de un terremoto: "));
terremoto = "";

if terremoto_int < 3:
    terremoto = "Muy leve";
elif terremoto_int >= 3 and terremoto_int < 4:
    terremoto = "Leve";
elif terremoto_int >= 4  and terremoto_int < 5:
    terremoto = "Moderado";
elif terremoto_int >= 5  and terremoto_int < 6:
    terremoto = "Fuerte";
elif terremoto_int >= 6  and terremoto_int < 7:
    terremoto = "Muy Fuerte";
elif terremoto_int >= 7:
    terremoto = "Extremo";

print(f"La maginitud de su terremoto es: {terremoto}");


# Ejercicio 10)

emisferio = input("En que emisferio se encuentra(N/S)? ").upper();
mes = int(input("Que en que mes del año encuentra (fecha)? "));
dia = int(input("Que dia del mes se encuentra (fecha)? "));

estacion = ""

if emisferio == "N":
    if (mes == 1) or (mes == 2):
        estacion = "Invierno"
    
    if (mes == 3) and (dia <= 20):
        estacion = "Invierno"
    elif (mes == 3) and (dia > 20):
        estacion = "Primavera"
    
    if (mes == 4) or (mes == 5):
        estacion = "Primavera"
    
    if (mes == 6) and (dia <= 20):
        estacion = "Primavera"
    elif (mes == 6) and (dia > 20):
        estacion = "Verano"

    if (mes == 7) or (mes == 8):
        estacion = "Verano"
    
    if (mes == 9) and (dia <= 20):
        estacion = "Verano"
    elif (mes == 9) and (dia > 20):
        estacion = "Otoño"

    if (mes == 10) or (mes == 11):
        estacion = "Otoño"
    
    if (mes == 12) and (dia <= 20):
        estacion = "Otoño"
    elif (mes == 12) and (dia > 20):
        estacion = "Invierno"

elif emisferio == "S":
    if (mes == 1) or (mes == 2):
        estacion = "Verano"
    
    if (mes == 3) and (dia <= 20):
        estacion = "Verano"
    elif (mes == 3) and (dia > 20):
        estacion = "Otoño"
    
    if (mes == 4) or (mes == 5):
        estacion = "Otoño"
    
    if (mes == 6) and (dia <= 20):
        estacion = "Otoño"
    elif (mes == 6) and (dia > 20):
        estacion = "Invierno"

    if (mes == 7) or (mes == 8):
        estacion = "Invierno"
    
    if (mes == 9) and (dia <= 20):
        estacion = "Invierno"
    elif (mes == 9) and (dia > 20):
        estacion = "Primavera"

    if (mes == 10) or (mes == 11):
        estacion = "Primavera"
    
    if (mes == 12) and (dia <= 20):
        estacion = "Primavera"
    elif (mes == 12) and (dia > 20):
        estacion = "Verano"

print(f"Usted esta en la estacion de: {estacion}")