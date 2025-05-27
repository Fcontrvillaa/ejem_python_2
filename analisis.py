import sys
"""
if len(sys.argv) != 2:
    print("(el comando necesita un argumento) python archivo.py 'celcius'")
    sys.exit(1)
"""

archivo = sys.argv[1]

#numero de caracteres distintos
#numero de palabras distintos



#leer archivo
with open(archivo, "r", encoding="utf-8") as f:
    #print(f.read())
    texto = f.read()

#print (texto)

total_letras = textolen(texto)
total_palabras = texto.split
print(len(total_palabras))

