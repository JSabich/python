persona = {
"nombre": "Juan",
"edad": 33,
"ciudad": "Buenos Aires"

}
print(persona["nombre"])
persona["edad"]=44

print(persona["edad"])
persona["profesion"]="ingeniero"

del persona["ciudad"]

#print(persona)
#print(persona.keys())
print(persona.values())
print(persona.items())

notas = {
    "Matemática": 9,
    "Lengua": 8,
    "Historia": 10
}

for clave, valor in notas.items():
    print(f"En {clave} saqué {valor}")

#notas["Biología"]=6

if "Biología" in notas:
    print(f"En Biología saqué {notas['Biología']}")
else:
    print("No cursé Biología.")

mi_diccionario = {'z': 3, 'a': 5, 'm': 1}

# Ordenar por claves
ordenado_por_claves = dict(sorted(mi_diccionario.items()))

print(ordenado_por_claves)


mi_diccionario = {'z': 3, 'a': 5, 'm': 1}

# Ordenar por valores
ordenado_por_valores = dict(sorted(mi_diccionario.items(), key=lambda item: item[1]))

print(ordenado_por_valores)
# Resultado: {'m': 1, 'z': 3, 'a': 5}



