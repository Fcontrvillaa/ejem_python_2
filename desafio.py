
# conversion de temp   sys.argv()


import sys

if len(sys.argv) != 2:
    print("(el comando necesita un argumento) python archivo.py 'celcius'")
    sys.exit(1)

""""

Celsius a Fahrenheit: °F = (°C * 9/5) + 32 
Celsius a Kelvin: K = °C + 273.15
Celsius a Rankine: °R = (°C * 9/5) + 491.67

"""

celcius = float(sys.argv[1])

print(celcius)

conversiones = {
    "Fahrenheit :" : (celcius * (9/5)) + 32 ,
    "kelvin :" : celcius + 273.15,
    "Rankine :" : (celcius * (9/5)) + 491.67
}

for k , v in conversiones.items():
    print(k , v)