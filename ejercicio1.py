principiantes=0
avanzados=0
cantidad=0

while True:
    try:
        cantidad=int(input("ingrese cantidad de deportistas:"))
        if cantidad > 0:
            break
        print("ingrese un numero entero positivo")
    except ValueError:
        print("ingrese un numero")
for i in range (cantidad):
    while True:
        codigo=input("ingrese codigo del socio: ")
        if len (codigo.strip())>=5 and " " not in codigo: #el strip borra los espacios en blanco
            break
        print("debe tener un largo minimo de 5 caracteres sin espacios")
    while True:
        try:
            practica=int(input("ingrese años de practica:"))
            if practica>0:
                break
            print("ingrese un numero positivo")
        except ValueError:
            print("ingrese un numero")
    if practica>3:
        avanzados +=1
    else:
        principiantes+=1
print(f"cantidad de avanzados {avanzados}")
print(f"cantidad de principiantes {principiantes}")