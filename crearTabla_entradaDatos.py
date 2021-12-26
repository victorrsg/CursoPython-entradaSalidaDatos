import sys
if len(sys.argv)==3:
    n1=int(sys.argv[1])
    n2=int(sys.argv[2])

    if n1>=1 and n1<=9 and n2>=1 and n2<=9:
        for filas in range(n1):
            print("")
            for col in range(n2):
                print("*",end="")
else:
    print("error""Ejemplo: ejEntradaDatos.py 1 2")
