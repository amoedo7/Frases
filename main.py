import os
from itertools import combinations

# Leer las palabras de bip39.txt
with open('bip39.txt', 'r') as f:
    words = [line.strip() for line in f.readlines()]

# Función para crear combinaciones y guardarlas en el sistema de archivos
def crear_esquema(comb, ruta):
    if len(comb) == 0:
        return
    palabra_actual = comb[0]
    nueva_ruta = os.path.join(ruta, palabra_actual)
    if not os.path.exists(nueva_ruta):
        os.makedirs(nueva_ruta)
    
    # Si queda más de una palabra, sigue dividiendo
    for i in range(1, len(comb)):
        crear_esquema(comb[i:], nueva_ruta)

# Generar combinaciones de 12, 18 o 24 palabras
for comb in combinations(words, 12):
    crear_esquema(list(comb), "/path/to/your/github/repository")  # Cambia la ruta por el repositorio adecuado
