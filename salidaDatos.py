text="otro texto"
n=5
print("Un texto",text,"y un número",n)

cadena="un texto {} y un número {}".format(text,n)
print(cadena)

print("un texto {1} y un número {0}".format(text,n))

print("un texto {texto} y un número {num}".format(texto=text,num=n))

#Alineamiento a la derecha:
print("{:>30}".format("palabra"))

#Alineamiento al centro:
print("{:^30}".format("palabra"))

#Alineamiento a la derecha y truncamiento a 3 caracteres:
print("{:>30.3}".format("palabra"))

#Formateo de números enteros, rellenados con espacios:
print("{:4d}".format(10))       #:4d --- 4 dígitos
print("{:4d}".format(100))
print("{:4d}".format(1000))