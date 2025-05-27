import sys

if len(sys.argv) != 2:
    print("(el comando necesita un argumento) python archivo.py 'celcius'")
    sys.exit(1)


archivo = sys.argv[1]

#leer archivo
with open(archivo, "r", encoding="utf-8") as f:
    print(f.read())