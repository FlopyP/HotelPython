#creamos un objeto de reservas

class Reserva:
    #atributo de clase
    reservas = [ ]
    #constructor
#    def __init__(self, cod, ape, nom, dni, mail, cant, hab, ingr, egr, pago):
#        self.codigo = cod
#        self.apellido = ape
#        self.nombre = nom
#        self.dni = dni
#        self.mail = mail
#        self.cantidad = cant
#        self.habitacion = hab
#        self.ingreso = ingr
#        self.egreso = egr
#        self.pago = pago


    #----------------------------------------------
    #Metodo para dar de alta a los huespedes
    #----------------------------------------------

    def agregar_reserva(self, cod, ape, nom, dni, mail, cant, hab, ingr, egr, pago):
        if self.ver_reservas(cod):
            return False
        else:
            huesped = {
                "codigo": cod,
                "apellido": ape,
                "nombre": nom,
                "dni": dni,
                "mail": mail,
                "cantidad": cant,
                "habitacion": hab,
                "ingreso": ingr,
                "egreso": egr,
                "pago": pago 
            }
            self.reservas.append(huesped)
            return True

#----------------------------------------------
#Funcion para listar a las reservas
#----------------------------------------------

    def listar_reservas(self):
        print("-"*15)
        for reserva in self.reservas:
            print(f"    Codigo: {reserva['codigo']}")
            print(f"  Apellido: {reserva['apellido']}")
            print(f"    Nombre: {reserva['nombre']}")
            print(f"       DNI: {reserva['dni']}")
            print(f"      Mail: {reserva['mail']}")
            print(f"  Cantidad: {reserva['cantidad']}")
            print(f"Habitacion: {reserva['habitacion']}")
            print(f"   Ingreso: {reserva['ingreso']}")
            print(f"    Egreso: {reserva['egreso']}")
            print(f"      Pago: {reserva['pago']}")
            print("-"*15)

#----------------------------------------------
#Funcion para consultar las reservas
#----------------------------------------------

    def ver_reservas(self, cod):
        for reserva in self.reservas:
            if reserva['codigo'] == cod:
                return reserva
        return False

#----------------------------------------------
#Funcion para mostrar las reservas
#----------------------------------------------

    def mostrar_reservas(self, reserva):
        print("-"*15)
        print(f"    Codigo: {reserva['codigo']}")
        print(f"  Apellido: {reserva['apellido']}")
        print(f"    Nombre: {reserva['nombre']}")
        print(f"       DNI: {reserva['dni']}")
        print(f"      Mail: {reserva['mail']}")
        print(f"  Cantidad: {reserva['cantidad']}")
        print(f"Habitacion: {reserva['habitacion']}")
        print(f"   Ingreso: {reserva['ingreso']}")
        print(f"    Egreso: {reserva['egreso']}")
        print(f"      Pago: {reserva['pago']}")
        print("-"*15)

#----------------------------------------------
#Funcion para eliminar una reserva
#----------------------------------------------

    def eliminar_reservas(self, cod):
        for reserva in self.reservas:
            if reserva['codigo'] == cod:
                self.reservas.remove(reserva)
                return True
        return False

#----------------------------------------------
#Funcion para modificar las reservas
#----------------------------------------------

    def modificar_reserva(cod, ape, nom, dni, mail, cant, hab, ingr, egr, pago):
        reserva = ver_reservas(cod)
        if reserva:
            reserva["codigo"] = cod
            reserva["apellido"] = ape
            reserva["nombre"] = nom
            reserva["dni"] = dni
            reserva["mail"] = mail
            reserva["cantidad"] = cant
            reserva["habitacion"] = hab
            reserva["ingreso"] = ingr
            reserva["egreso"] = egr
            reserva["pago"] = pago 

            eliminar_reservas(cod)
            reservas.append(reserva)
            return True
        else:
            return False

#----------------------------------------------------------------------------------------------

#print("\033[H\033[J")
#print(agregar_reserva(1, "Perez", "Alejando", 24595284, "alejandroperez@gmail.com", 2, "HTML" , 12122023, 20122023, "tarjeta"))
#print(agregar_reserva(2, "Rico", "Maria", 35167585, "rico_maria@gmail.com", 4, "PYTHON" , 12122023, 20122023, "tarjeta"))
#print(agregar_reserva(3, "Rodriguez", "Liliana", 15635744, "llrodriguez@gmail.com", 2, "JAVASCRIPT" , 22122023, 27122023, "efectivo"))

#print(reservas)

#listar_reservas()

#aux = ver_reservas(1)
#if aux:
#    mostrar_reservas(aux)
#else:
#    print("Reserva no encontrada.")

#print(modificar_reserva(1, "Paez", "Alejando", 15494294, "alejandro_paez@gmail.com", 2, "HTML" , 12122023, 20122023, "tarjeta"))
#listar_reservas()


#----------------------------------------------------------------------------------------------

print("\033[H\033[J")

huesped = Reserva()


huesped.agregar_reserva(1, "Perez", "Alejando", 24595284, "alejandroperez@gmail.com", 2, "HTML", 12122023, 20122023, "tarjeta")

#huesped2.agregar_reserva(2, "Rico", "Maria", 35167585, "rico_maria@gmail.com", 4, "PYTHON" , 12122023, 20122023, "tarjeta")

#a = huesped1.ver_reservas(1)
#b = huesped2.ver_reservas(2)

huesped.listar_reservas()

#huesped.mostrar_reservas(a)
#huesped.mostrar_reservas(b)
