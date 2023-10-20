numero=1
sueldo=0
total=0

while numero <=5:
    sueldo= int(input("Entre sueldo:"))
    total= total + sueldo
    numero+=1
print ("Total de sueldos:", total)