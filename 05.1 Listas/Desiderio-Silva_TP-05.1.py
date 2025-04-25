
# Actividades:
 
# 1)
nums_1_to_100 = list(range(4, 101, 4));

print(nums_1_to_100);


# 2)
fav_things = ["hk", "blasf", "ori1", "ori2", "ender"];

print(fav_things[3]);


# 3)
empty_list = [];
empty_list.append("lala");
empty_list.append("po");
empty_list.append("wisiwisi");

print(empty_list);


# 4)
animales = ["perro", "gato", "conejo", "pez"];
animales[1] = "loro";
animales[-1] = "oso";

print(animales)


# 5)
numeros = [8, 15, 3, 22, 7];
numeros.remove(max(numeros));

print(numeros);     # Output: [8, 15, 3, 7]

'''
    Explicación:
El programa comienza definiendo la variable "numeros", en la cual se le asigna un array con 5 números diferentes.
Luego el programa remueve el número mas grande ingresado utilizando remove() y max().
Por último el programa imprime la variable de "numeros".
'''


# 6)
nums_10_to_30 = list(range(10, 31, 5));

print(nums_10_to_30[0:2]);


# 7)
autos = ["sedan", "polo", "suran", "gol"];
autos[1] = "crazy";
autos[2] = "dude";

print(autos);


# 8)
dobles = [];
dobles.append(5*2);
dobles.append(10*2);
dobles.append(15*2);

print(dobles);


# 9)
compras = [
    ["pan", "leche"],
    ["arroz", "fideos","salsa"],
    ["agua"]
    ];

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)


# 10)
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)
