import random
from datetime import date




def fechaAleatoria(año_minimo):
    año = str(random.randint(año_minimo, 2022))
    mes = (random.randint(1, 12))
    if mes < 10:
        mes = "0" + str(mes)
    dia = random.randint(0, 30)
    if dia < 10:
        dia = "0" + str(dia)
    date = año + str(mes) + str(dia)

    return int(date)

class cuentaBancaria:
    
    def __init__(self, ID, nombre, saldo):
        self.fecha_apertura = fechaAleatoria(1910)
        self.numero_cuenta = random.randint(100000000000, 999999999999)
        self.max_negativo = 0
        self.fechaTope = 0
        self.id = int(ID)
        self.nombre = nombre
        self.saldo = int(saldo)

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad):
        #Meter cosa de quitar 5% si fecha actual menor que fecha tope
        if int(str(date.today()).replace("-", "")) - self.fechaTope <= 0:
            cantidad = cantidad - ((cantidad * 5) / 100)

        if self.saldo - cantidad >= 0:
            self.saldo = self.saldo - cantidad
            print("Retirada exitosa, su saldo es de", self.saldo)
        else:
            if self.saldo - cantidad >= self.max_negativo:
                self.saldo = self.saldo - cantidad
                print("Retirada exitosa, su saldo es de", self.saldo)
            else:
                print("REVERT. Excede la maxima deuda posible si realiza esta transaccion!!")
    
    def tranferir(self, to, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo = self.saldo - cantidad
            to.saldo = to.saldo + cantidad
            print("Transferencia realizada a", to.nombre, "Su saldo es de", self.saldo)
        else:
            if self.saldo - cantidad >= self.max_negativo:
                self.saldo = self.saldo - cantidad
                to.saldo = to.saldo + cantidad
                print("Transferencia realizada a", to.nombre, "Su saldo es de", self.saldo)
            else:
                print("REVERT. Excede la maxima deuda posible si realiza esta transaccion!!")
    
    def details(self):
        print("Numero de cuenta:", self.numero_cuenta)
        print("Identificador cuenta:", self.id)
        print("Nombre del titular:", self.nombre)
        print("Saldos disponible:", self.saldo)
        print("Fecha apertura:", self.fecha_apertura)
        print("Fecha limite sin comision:", self.fechaTope)
        print("Maxima deuda posible:", self.max_negativo)
        print("-----------------------")



class cuentaClaseObrera:
    def __init__(self, ID, nombre, saldo):
        self.cuenta = cuentaBancaria(ID, nombre, saldo)
    

class PlazoFijo:
    def __init__(self, ID, nombre, saldo):
        self.cuenta = cuentaBancaria(ID, nombre, saldo)
        self.cuenta.fechaTope = fechaAleatoria((self.cuenta.fecha_apertura + 1) // 10000)

class CuentaVip:
    def __init__(self, ID, nombre, saldo):
        self.cuenta = cuentaBancaria(ID, nombre, saldo)
        self.cuenta.max_negativo = -3000


obrero = cuentaClaseObrera(1, "Pepe Molina", 10000)
tontoDelFijo = PlazoFijo(2, "jaime Navarro", 10000)
burgues = CuentaVip(3, "Carla Alvareda", 10000)

obrero.cuenta.tranferir(burgues.cuenta, 2000)
tontoDelFijo.cuenta.ingresar(250)
tontoDelFijo.cuenta.retirar(250)
burgues.cuenta.retirar(13000)

obrero.cuenta.details()
tontoDelFijo.cuenta.details()
burgues.cuenta.details()
