"""
pregunta 1
total = float(input("ingresa el valor de la cuenta: "))
porcentaje = float(input("agrega el porcentaje de propina: "))

suma = total + porcentaje / 100

print (f"el total a pagar es de {suma}")
"""

"""
pregunta 2
horas = int(input("ingresa un numero de horas trabajadas: "))
minutos = int(input("ingresa el total de minutos trabajados: "))

suma1 = horas * 3600
suma2 = minutos * 60
print (f"la hora {horas} tiene un total de: {suma1} segundos")
print (f"los minutos {minutos} tienen un total de segundos de: {suma2}")
"""


"""
pregunta 3
numero = int(input("ingresa un numero: "))

if numero < 100:
    print(f"el numero {numero} esta entre el 1 y el 100")

elif numero == 100:
    print(f" el numero {numero} es igual a 100")

else:
    print("Numero no valido")
"""

"""
pregunta 4
entrada = 10
porcentaje = 20
print (f"el valor de la entrada es {entrada}$")

edad = int(input("ingresa tu edad:"))

if edad > 60:
    print("tienes descuento del 20%")
    suma = entrada + porcentaje / 100
    print (f"el total a pagar es de {suma}$")

else:
    print("no tienes descuento")
    print(f"la entrada cuesta: {entrada}$")    
"""

"""
pregunta 5
letra = input("ingresa una letra: ").lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print (f" la letra {letra} es una vocal")

else:
    print (f" la letra {letra} es una consonante")
"""

"""
pregunta 6
lado1 = float(input("ingresa el valor del primer lado: "))
lado2 = float(input("ingresa el valor del segundo lado: "))
lado3 = float(input("ingresa el valor del tercer lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("el triangulo es equilatero  ")

elif lado1 == lado2 and lado1 != lado3:
    print("el triangulo es isosceles ") 

else:
    print("el triangulo es escaleno")       
"""
"""
pregunta 7
saldo = 1000
print (f"el saldo actual es de {saldo}$")

extraer = int(input("ingresa el monto a extraer: ""$"))

if extraer <= saldo:
    print ("extraccion exitosa")
    print (f"el saldo acual es de {saldo - extraer}$")

else:
    print ("saldo insuficiente")
"""

"""
pregunta 8
limite = int(input("ingrese el limite de velocidad: "))
velocidad = int(input("ingrese la velocidad actual: "))

if velocidad > limite:
    exceso = velocidad - limite
    multa = 50
    for i in range(int(exceso)):
        multa = multa + 5
    print ("excediste el limite de velocidad")
    print (f"el valor de la multa es de: {multa}$")


else:
    print ("no excediste el limite de velocidad")
"""   


"""
pregunta 9
año = int(input("ingresa un año: "))

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print(f"El año {año} es bisiesto.")

else: 
    print ("el año no es bisiesto")
"""



"""
pregunta 10
promedio = float(input("ingrese promedio del estudiante: "))
ingresos = float(input("ingrese ingresos del estudiante: "))
distancia = int(input("ingrese distancia del estudiante: "))

if promedio > 90 and ingresos < 500:
    print ("beca completa")

elif promedio > 80 and distancia >50:
    print ("beca de transporte")   

else:
    print("no hay beca disponible")     
"""


"""
pregunta 11
salario = float(input("ingrese el valor del impuesto: "))


if salario >= 0 and salario < 10000:
    print("no se aplica impuesto")

elif salario > 1000 and salario < 30000:
    impuesto = (salario * 10) / 100
    print(f"el impuesto total es del 10% lo cual la cuenta total haria {salario + impuesto}")

else:
    impuesto = (salario * 20) / 100
    print (F"el impuesto total es del 20% lo cual la cuenta total haria {salario + impuesto}")
"""


"""
pregunta 12
dia = input("agrega un dia de la semana: ").lower()
mes = input("agrega un mes del año: ").lower()  
año = int(input("agrega un año: "))

if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "viernes" or dia == "sabado" or dia == "domingo":
    print()

elif (mes == "enero" or mes == "febrero" or mes == "marzo" or mes == "abril" or mes == "mayo" or mes == "junio" or mes == "julio" or mes == "agosto" or mes == "septiembre" or mes == "octubre" or mes == "noviembre" or mes == "diciembre"):
    print()
     

else:
    print("datos no validos")


print(f"el dia {dia} existe")
print (f"el mes {mes} existe")
if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print("el año es biciesto")
else:
    print("el año no es biciesto")    
"""


jugador1 = input("jugador 1, ¿piedra papel o tijera? : ")
jugador2 = input("jugador 2, ¿piedra papel o tijera? : ")


if jugador1 == "tijera" or jugador1 == "piedra" or jugador1 == "papel":

    if jugador2 == "tijera" or jugador2 == "piedra" or jugador2 == "papel":
         if jugador1 == jugador2:
             print("empate")

elif jugador1 == "tijera" and jugador2 == "papel":
    print("gana jugador 1")    



        

else:
    print ("ninguno")


        




















