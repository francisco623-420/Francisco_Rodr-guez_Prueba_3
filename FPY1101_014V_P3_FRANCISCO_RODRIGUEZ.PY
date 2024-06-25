


#esta lista guarda los datos de los vehiculos
datos_vehiculo = []

#variables auxiliares
tipo_vehiculo = ["auto", "camion", "camioneta", "moto"]
patente = ""
marca = ""
precio = 0
multas = 0
monto_mul = 0
fecha_mul = ""
fecha_ing = ""
run_duenio = 0
nombre_duenio = ""


#definimos las funciones
def grabar_vehiculo(tipo, paten, marc, preci, mul, mon_mul, fech_mul, fech_ing, run_due, nom_due):
    datos_vehiculo.append([tipo, paten, marc, preci, mul, mon_mul, fech_mul, fech_ing, run_due, nom_due])


def buscar_vehiculo(datos,patente):
    if len(datos) == 0:
        print("no hay vehiculos registrados")
        return

    for datos in datos:
        if datos[1] == patente:
            print("Tipo\t Patente\t  Marca\t Precio\t Multas\t Monto_multas\t Fecha_multa\t Fecha_ingreso\t run_duelo\t Nombre_dueño")
            for i in datos:
                print(f"{i}\t", end="")
            print()



def imprime_certificado (datos, patente):
    for datos in datos:
        if datos [1] == patente:
            for i in datos:
                print(f"para la patente:{patente} se extienden los siguientes sertificados:")
                print("1.- amision de gases: malo ")
                print("2.- anotaciones viigentes: todo malo xd")
                print("3.- multas: no pasa nada")
#no alcance a ahcer los demas for profe :c 

while True:
    print("Bienvenido a auto seguro\n")
    print("___Menú___\n")
    print("1.- ingresar datos del vehiculo")
    print("2.- Consultar datos del vehiculo")
    print("3.- Imprimir sertificados")
    print("4.- Salir")

    try:
        op = int(input("favor de ingresar su opcion: "))
    except:
        op = 0

    if op == 1:
        while True:
            vehiculo = input(f"escriiba su tipo de vehiculo {tipo_vehiculo}: ")
            vehiculo.lower()
            if vehiculo not in tipo_vehiculo:
                print("vehiculo no valido")
            else:
                break


        while True:
            patente = input("ingrese su patente: ")
            if len(patente) > 0 and len(patente) <7:
                break
            else:
                print("tienen que se 6 caracteres")

        while True:
            marca = input("Ingrese la marca del vehiculo: ")
            if len(marca) >= 2 and len(marca) < 16:
                break
            else:
                print("La marca tiene que ser entre 2 y 15 caracteres")

        while True:
            try:
                precio = int(input("ingrese el precio del vehiculo: "))
            except:
                precio = 0
            if precio > 5000000:
                break
            else:
                print("El precio debe ser mayor a 5 millones")
        while True:
            try:
                multas = int(input("Ingrese la cantidad de multas: "))
            except:
                multas = -1
            if multas > -1:
                break
            else:
                print("El numero debe ser mayor a 0")

        while True:
            try:
                monto_mul = int(input("ingrese el monto de la o las multas sumadas: "))
            except:
                monto_mul == -1
            if monto_mul > -1:
                break
            else:
                print("el monto debe ser mayor a -1")

        while True:
            fecha_mul = input("Ingrese la fecha de la multa en el formato xx/xx/xxxx : ")
            if len(fecha_mul) > 0 and len(fecha_mul) < 12:
                break
            else:
                print("favor de ingresar la fecha en el formato solicitado")
                
        while True:
            fecha_ing = input("ingrese la fecha de ingreso del vehiculo en el formato xx/xx/xxxx : ")
            if len(fecha_ing) > 0 and len(fecha_ing) < 11:
                break
            else:
                print("favor de ingresar la fecha en el formato solicitado")

        while True:
            try:
                run_duenio = int(input("Ingrese su rut sin puntos ni digito verificador: "))
            except:
                run_duenio = 0
            if run_duenio > 5000000 and run_duenio < 30000000:
                break
            else:
                print("favor de ingresar maximo 8 caracteres")

        while True:
            nombre_duenio = input("Ingrese el nombre del dueño: ")
            if len(nombre_duenio) > 0:
                break
            else:
                print("el campo no puede estra vacio")

        grabar_vehiculo(vehiculo, patente, marca, precio, multas, monto_mul, fecha_mul, fecha_ing, run_duenio, nombre_duenio)


    elif op == 2:
        patente = input("ingrese la patente del vehiculo que busca: ")
        buscar_vehiculo(datos_vehiculo, patente)

    elif op == 3:
        patente = input("ingrese la patente para los los certificados: ")
        imprime_certificado(datos_vehiculo, patente)
    elif op == 4:
        print("gracias por participar!")
        break

    else:
        print("favor de ingresar una opcion valida")