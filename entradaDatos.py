import sys
texto = sys.argv[1]
repeticiones =sys.argv[2]
repeticiones=int(sys.argv[2])

if len(sys.argv)==3:
    for r in range(repeticiones):
        print(texto)
else:
    print("Error, introduce el número correcto de argumentos")