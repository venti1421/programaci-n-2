#Ciclo For
#dominar el usi del ciclo for para iterar sobre rengo listas cadenas y dupla. aprender a usar contadores y acumuladores tanto dentro como por fuera del bucle.
#que es un for es un ciclo que permite recorre o secuencias o estuctraus que son iterables listas arreglos , string tuplas , diccinarios, rangos etc,

#For elemento in secuencia:
   #el codigo que se debe ejecutar repetidamente.

#Que es un rango : es una lista de items qu esta acotada tanto en principio como en fin, usualmente numerico.

# for i in range(5):
#     print(f"hola soy  el {i}")
# un rango originalmnete  puede tres paramaetro de los cuales solo el final del rango es obligatorio.
#range (inicio, fin ) siempre al final sumar uno "arranca desde cero"
#range (10, 0, -2) paso como avanzar
# for i in range(10,-10,-2):
#     print(f"hola soy  el {i}, pero en reversa")

# for cuenta in range(0, 1001, 5):
#    print(cuenta)

# nombres = ["Ana", "Luis", "Martica"]
# for nombre in nombres : 
#     print(f"hola, {nombre}. ¿Como estas?")

# print(f"hola, {nombres[1]}. como esta?")

#cadenas 

# palabra = "python"
# string = ["p","y","t","h","o","n"]

# for letra in palabra:
#     print(letra)

# for char in string :
#     print(char)

#"tupla"  es una lista o secuencia ordena y finita lo separa con coma entre parentesis

coordenada = (4, 7, 2)
for valor in coordenada:
    print(f"valor de la coordenada: {valor}")
