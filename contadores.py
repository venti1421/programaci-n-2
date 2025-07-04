#contar veces ocuree un acondicion dada
#contar cuantas vocales tiene cualquier cadena.

# vocales = "aeiou"
# palabra = input("Escriba una palabra:")
# contador = 0
# for letra in palabra :
#     if letra.lower()in vocales:
#         contador += 1

# print(f"la palabra '{palabra}' tiene {contador} vocales")

# vocales = "aeiou"
# contador_vocales = {v : 0 for v in vocales}
# palabra = input("Escriba una palabra:")

# for letra in palabra:
#     letra_min = letra.lower()
#     if letra_min in vocales:
#         contador_vocales[letra_min]+= 1
# print("\nConteo de vocales: ")
# for v, c in contador_vocales.items():
#     print(f"  {v}: {c}")

vocales = "abcdefghijklmnopqrstwxyz"
contador_vocales = {v : 0 for v in vocales}
palabra = input("Escriba una palabra:")

for letra in palabra:
    letra_min = letra.lower()
    if letra_min in vocales:
        contador_vocales[letra_min]+= 1
print("\nConteo de vocales: ")
for v, c in contador_vocales.items():
    print(f"  {v}: {c}")