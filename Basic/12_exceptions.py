### EXception Handling ###

numberOne, numberTwo = 5, 1
numberTwo = "1"

# Try-Except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Error: Se ha producido un error")

# Try-Except-Else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Error: Se ha producido un error")
else:
    #Esto se ejecuta si no hay error osea que no se produsca una exception
    print("La ejecucion continua correctamente")
finally: # Opcional
    # Esto se ejecuta siempre, haya error o no
    print("LA ejecucion continua")

# Exceptiones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Error: Se ha producido un Typerror")
except ValueError:
    print("Error: Se ha producido un ValueError")

# Captura de la informacion de la exception

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)