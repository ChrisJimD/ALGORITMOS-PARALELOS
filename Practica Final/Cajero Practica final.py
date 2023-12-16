class Banco:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuenta:
    def __init__(self, numero_cuenta, saldo, limite_credito, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.limite_credito = limite_credito
        self.tipo_cuenta = tipo_cuenta

class Cliente:
    def __init__(self, nombre, direccion, numero_cuenta, saldo, contrasena):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.contrasena = contrasena

class Cajero:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

class CajeroAutomatico:
    def __init__(self, banco, clientes):
        self.banco = banco
        self.clientes = clientes
        self.cliente_autenticado = None

    def validarusuario(self, numero_cuenta, contrasena):
        for cliente in self.clientes:
            if cliente.numero_cuenta == numero_cuenta and cliente.contrasena == contrasena:
                self.cliente_autenticado = cliente
                return True
        return False

    def menu(self):
        print("¿Qué desea hacer?")
        print("1. Retirar efectivo")
        print("2. Ingresar efectivo")
        print("3. Transferir fondos")
        print("4. Pagar factura")
        print("    a. Pagar factura del cable ($1000)")
        print("    b. Pagar factura de la universidad ($3200)")
        print("5. Ver balance")
        print("0. Salir")

    def IngresoEfectivo(self, cantidad):
        self.cliente_autenticado.saldo += cantidad
        print(f"Se ingresaron {cantidad} a la cuenta de {self.cliente_autenticado.nombre}. Nuevo saldo: {self.cliente_autenticado.saldo}")

    def RetiroEfectivo(self, cantidad):
        if self.cliente_autenticado.saldo >= cantidad:
            self.cliente_autenticado.saldo -= cantidad
            print(f"Se retiraron {cantidad} de la cuenta de {self.cliente_autenticado.nombre}. Saldo restante: {self.cliente_autenticado.saldo}")
        else:
            print("Saldo insuficiente.")

    def TransferenciaFondos(self, info_cuenta_destino, cantidad):
        if self.cliente_autenticado.saldo >= cantidad:
            # Lógica de transferencia de fondos
            self.cliente_autenticado.saldo -= cantidad
            print(f"Se transfirieron {cantidad} desde la cuenta {self.cliente_autenticado.numero_cuenta} a {info_cuenta_destino}.")
            print(f"Nuevo saldo: {self.cliente_autenticado.saldo}.")
        else:
            print("Saldo insuficiente para realizar la transferencia.")

    def PagarFactura(self, tipo_factura):
        if tipo_factura == 'a':
            factura = "cable"
            monto = 1000
        elif tipo_factura == 'b':
            factura = "universidad"
            monto = 3200
        else:
            print("Opción no válida.")
            return

        if self.cliente_autenticado.saldo >= monto:
            self.cliente_autenticado.saldo -= monto
            print(f"Se pagó la factura de {factura} por ${monto}. Saldo restante: {self.cliente_autenticado.saldo}")
        else:
            print(f"Saldo insuficiente para pagar la factura de {factura}.")

    def VerBalance(self):
        print(f"Balance de la cuenta de {self.cliente_autenticado.nombre}: {self.cliente_autenticado.saldo}")

# Creación de instancia con contraseña
cliente1 = Cliente("Christopher Jimenez", "Calle Tropical", "53605", 10000, "1215")

# Creación de instancia de CajeroAutomatico
banco = Banco("Banco Principal")
clientes = [cliente1]
cajero_automatico = CajeroAutomatico(banco, clientes)

# Solicitud
numero_cuenta = input("Ingrese el número de cuenta: ")
contrasena = input("Ingrese la contraseña: ")

# Validar
if cajero_automatico.validarusuario(numero_cuenta, contrasena):
    print(f"Usuario autenticado como {cajero_automatico.cliente_autenticado.nombre}.")

    while True:
        cajero_automatico.menu()

        opcion = input("Ingrese el número de la operación que desea realizar (0 para salir): ")

        if opcion == '0':
            print("Sesión terminada. Gracias por usar el cajero automático.")
            break

        if opcion.isdigit() and 1 <= int(opcion) <= 5:
            opcion = int(opcion)
            if opcion == 3:
                info_cuenta_destino = input("Ingrese el numero de la cuenta destino: ")
                cantidad = float(input("Ingrese la cantidad que desea transferir: "))
                cajero_automatico.TransferenciaFondos(info_cuenta_destino, cantidad)
            elif opcion == 1:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cajero_automatico.RetiroEfectivo(cantidad)
            elif opcion == 2:
                cantidad = float(input("Ingrese la cantidad a ingresar: "))
                cajero_automatico.IngresoEfectivo(cantidad)
            elif opcion == 4:
                subopcion = input("Seleccione la factura que desea pagar (a/b): ")
                cajero_automatico.PagarFactura(subopcion)
            elif opcion == 5:
                cajero_automatico.VerBalance()
        else:
            print("Opción no válida. Ingrese un número del 1 al 5 o 0 para salir.")
else:
    print("Usuario o contraseña incorrectos.")
