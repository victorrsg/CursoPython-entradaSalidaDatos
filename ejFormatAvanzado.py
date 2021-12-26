# **Avanzado** Crea un script que realice las siguientes tareas:
# Debe tomar un argumento que será un int
# En caso de no recivir uno, salta error

# El objetivo es descomponer en unidades, decenas, centenas... un número
# Utilizando formateo:

import sys
if len(sys.argv)==2:
    num=int(sys.argv[1])
    if num>1 and num<9999:
        cadena=str(num)
        long=(len(cadena))
        
        for i in range(long):
            print("{:04d}".format(int(cadena[long-1-i])*10**i))
else:
    print("error""Ejemplo: ejEntradaDatos.py 1 2")
