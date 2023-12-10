class Empleado:
   
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado:")
        self.apellido = input("Ingrese el apellido del empleado:")
        self.edad = int(input("Ingrese la edad del empleado:"))
        self.sexo = input("Ingrese el sexo del empleado:")
        self.direccion = input("Ingrese la dirección del empleado:")
        self.email = input("Ingrese el email del empleado:")

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
        print("Dirección:", self.direccion)
        print("Email:", self.email)

    def Afp(self, sb):
        return sb * 0.0287
    
    def Irs(self, sb):
        if sb <= 416220.00:            
            print("NO PAGA IMPUESTOS SOBRE LA RENTA")
            return 0
        elif sb <= 624329.00:
            return sb * 0.15
        elif sb <= 867123.00:
            return sb * 0.20
        else:
            return sb * 0.25
                  
    def Sfs(self, sb):
        return sb * 0.0304
    
    def TotalDesc(self, afp, irs, sfs):
        if sueldo < 416220.00:
            return afp + sfs
        else:   
            return afp + irs + sfs
    
    def SueldoNeto(self, sb, td):
        return sb - td

emp = Empleado()

sueldo = float(input("Ingrese su sueldo: "))
sueldo = sueldo * 12
afp = emp.Afp(sueldo)
sfs = emp.Sfs(sueldo)
irs = emp.Irs(sueldo)
descuento = emp.TotalDesc(afp, irs, sfs)
sn = emp.SueldoNeto(sueldo, descuento)

emp.imprimir()
print("Afp          : {:0.2f}".format(afp))
print("Sfs          : {:0.2f}".format(sfs))

if sueldo > 416220.00:
    print("Irs          : {:0.2f}".format(irs))

print("Descuento    : {:0.2f}".format(descuento))
print("Sueldo Neto  : {:0.2f}".format(sn))
