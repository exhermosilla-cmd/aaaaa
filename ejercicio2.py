stock=30
arriendo=0

ciclo=True
while ciclo:
    print("== Menu Arriendos ==")
    print("1. Autos Disponibles")
    print("2. Arrendar Auto ")
    print("3. Devolver Auto")
    print("4. Historial de arriendos activos")
    print("5. Salir")
    try:
        op=int(input("Seleccione"))
        match op:
            case 1:
                print(f"Autos disponibles: {stock}")
            case 2:
                while True:
                    try:
                        cantidad=int(input("cantidad:"))
                        if cantidad > 0:
                            break
                        print("numero entero positivo")
                    except ValueError:
                        print("ingrese un numero")
                if cantidad <=stock:
                    stock -= cantidad
                    arriendo+= cantidad
                    print(f"{cantidad} de autos arriendados")
                else:
                    print(f"cantidad supera el stock, stock: {stock}")
            case 3:
                while True:
                    try:
                        cantidad=int(input("cantidad a devolver: "))
                        if cantidad >0:
                            break
                        print("ingrese entero positivo")
                    except ValueError:
                        print("ingrese un numero")
                if cantidad<=arriendo:
                    stock+= cantidad
                    arriendo-= cantidad
                    print("se devolvio..")
                else:
                    print(f"cantidad a devolver mayor a arrendado ({arriendo})")
            case 4:
                print(f"cantidad disponible: {stock}")
                print(f"cantidad arrendada: {arriendo}")
            case 5:
                print("adios..")
    except ValueError:
        print("ingrese numero")