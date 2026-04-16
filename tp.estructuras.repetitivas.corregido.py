#Trabajo Practico Estructuras Repetitivas
#Ejercicio 1 "Caja del Kiosco"
precio_descuento=0
precio_nodescuento=0
ahorro=0
promedio=0
total_descuento=0
nombre_cliente=input("Ingrese su nombre porfavor:").title()
while not nombre_cliente.isalpha():
    nombre_cliente=input("Ingrese su nombre solo con letras porfavor:")
Cantidad_producto=input("Ingrese la cantidad de productos deseada:")
while not Cantidad_producto.isdigit() or Cantidad_producto=="0":
    Cantidad_producto=input("Ingrese un numero mayor que 0:")
print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {Cantidad_producto}")
Cantidad_producto=int(Cantidad_producto)
for i in range(1,Cantidad_producto+1):
    precio=input(f"Precio del producto {i}: ")
    while not precio.isdigit() or precio=="0":
        precio=input(f"Precio del producto {i}: ")
    descuento=input(f"El producto {i} tiene descuento? S/N: ").upper()
    while not descuento.isalpha():
        descuento=input("Porfavor, escriba las letras S o N: ").upper()
    precio=int(precio)
    promedio+=precio
    if "S" in descuento:
        precio=(precio*0.90)
        precio_descuento+=precio
    else:
        precio_nodescuento+=precio
total_descuento=precio_descuento+precio_nodescuento
print(f"Total sin descuento: {promedio}")
print(f"El total con descuento es: {total_descuento:.2f}")
print(f"El ahorro es {promedio-total_descuento:.2f}")
print(f"El promedio de los productos es: {total_descuento/Cantidad_producto:.2f}")

print("///////////////////////")
#Ejercicio 2 "Acceso al Campus y Menu Seguro"
usuario_correcto="alumno"
clave_correcta="python123"
intentos=1
while intentos<=3:
    usuario=input(f"intento n{intentos}/3 - Porfavor ingrese su usuario: ")
    contraseña=input("Porfavor ingresa su contraseña: ")
    if contraseña!=clave_correcta or usuario!=usuario_correcto:
        print("error credenciales invalidas.")
        intentos+=1
    if contraseña==clave_correcta and usuario==usuario_correcto:
        print("Acceso concedido!!")
        while True:
            print("1) Estado  2) Cambiar Clave  3) Mensaje Motivacional  4) Salir ")
            opcion=input("Opcion:")
            while not opcion.isdigit():
                 opcion=input("Ingrese un numero valido: ")
            while opcion not in ["1","2","3","4"]:
                 opcion=input("Opcion fuera del rango: ")
            if opcion=="1":
                print("Estado de inscripcion: (inscripto)")
            if opcion=="2":
                clave_correcta=input("Nueva clave: ")
                while len(clave_correcta)<6:
                    clave_correcta=input("Minimo 6 caracteres: ")
            if opcion=="3":
                print("-Sigue asi, constante, y te aseguro que dara frutos.")
            if opcion=="4":
                break
        break
    

if intentos==4:
    print("Cuenta bloqueada")
 

print("///////////////")
#Ejercicio 3 "Agenda de turnos con Nombres (sin listas)2"
lunes_1=""
lunes_2=""
lunes_3=""
lunes_4=""
martes_1=""
martes_2=""
martes_3=""
operador=input("Ingrese el nombre del operador: ")
while not operador.isalpha():
    operador=input("Ingrese el nombre del operador solo con letras: ")
while True:
    print("1)Reservar turno 2)Cancelar turno(Por nombre) 3)Ver agenda del dia 4)Ver resumen general 5)Cerras sistema")
    opcion=input("Opcion: ")
    while not opcion.isdigit():
        opcion=input("Ingrese un numero valido: ")
    if opcion=="1":
        dia=(input("Por favor ingrese (1) para Lunes o (2) para Martes: "))
        while not dia.isdigit():
            dia=(input("Ingrese un numero valido: "))
        if dia== "1":
            nombre_paciente=input("Ingrese el nombre del paciente: ")
            while not nombre_paciente.isalpha():
                 nombre_paciente=input("Ingrese el nombre del paciente solo con letras: ")
            nombre_paciente=nombre_paciente.title()
            if nombre_paciente == lunes_1 or nombre_paciente == lunes_2 or nombre_paciente == lunes_3 or nombre_paciente == lunes_4:
                 print("El paciente ya tiene un turno reservado para el lunes.")
            elif lunes_1=="":
                lunes_1=nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el lunes a las 9:00.")
            elif lunes_2=="":
                lunes_2=nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el lunes a las 10:00.")
            elif lunes_3=="":
                lunes_3=nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el lunes a las 11:00.")
            elif lunes_4=="":
                lunes_4=nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el lunes a las 12:00.")
            else:
                 print("No hay turnos disponibles para el lunes.")
        elif dia== "2":
            nombre_paciente=input("Ingrese el nombre del paciente: ")
            while not nombre_paciente.isalpha():
                nombre_paciente=input("Ingrese el nombre del paciente solo con letras: ")
            nombre_paciente=nombre_paciente.title()
            if nombre_paciente == martes_1 or nombre_paciente == martes_2 or nombre_paciente == martes_3:
                 print("El paciente ya tiene un turno reservado para el martes.")
            elif martes_1=="":
                martes_1=nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el martes a las 9:00.")
            elif martes_2=="":
                martes_2=nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el martes a las 10:00.")
            elif martes_3=="":
                martes_3=nombre_paciente
                print(f"Turno reservado para {nombre_paciente} el martes a las 11:00.")
            else:
                print("No hay turnos disponibles para el martes.")
        else:
            input("Opcion fuera del rango, presione enter para continuar.")
    if opcion=="2":
        dia=(input("Por favor ingrese (1) para Lunes o (2) para Martes: "))
        while not dia.isdigit():
            dia=(input("Ingrese un numero valido: "))
        if dia=="1":
            nombre_paciente=input("Ingrese su nombre: ")
            while not nombre_paciente.isalpha():
                nombre_paciente=input("Ingrese su nombre solo con letras: ")
            nombre_paciente=nombre_paciente.title()
            if nombre_paciente==lunes_1:
                lunes_1=""
                print(f"Turno de {nombre_paciente} cancelado.")
            elif nombre_paciente==lunes_2:
                lunes_2=""
                print(f"Turno de {nombre_paciente} cancelado.")
            elif nombre_paciente==lunes_3:
                lunes_3=""
                print(f"Turno de {nombre_paciente} cancelado.")
            elif nombre_paciente==lunes_4:
                lunes_4=""
                print(f"Turno de {nombre_paciente} cancelado.")
            else:
                print("No se encontró un turno reservado con ese nombre para el lunes.")
        elif dia=="2":
            nombre_paciente=input("Ingrese su nombre: ")
            while not nombre_paciente.isalpha():
                nombre_paciente=input("Ingrese su nombre solo con letras: ")
            nombre_paciente=nombre_paciente.title()
            if nombre_paciente==martes_1:
                martes_1=""
                print(f"Turno de {nombre_paciente} cancelado.")
            elif nombre_paciente==martes_2:
                martes_2=""
                print(f"Turno de {nombre_paciente} cancelado.")
            elif nombre_paciente==martes_3:
                martes_3=""
                print(f"Turno de {nombre_paciente} cancelado.")
            else:
                print("No se encontró un turno reservado con ese nombre para el martes.")
    if opcion=="3":
        print("Agenada del dia lunes:")
        if lunes_1!="":
            print(f"9:00 - {lunes_1}")
        else:
            print("9:00 - Disponible")
        if lunes_2!="":
            print(f"10:00 - {lunes_2}")
        else:            
            print("10:00 - Disponible")
        if lunes_3!="":           
            print(f"11:00 - {lunes_3}")
        else:
            print("11:00 - Disponible")
        if lunes_4!="":
            print(f"12:00 - {lunes_4}")
        else:
            print("12:00 - Disponible")
        print("Agenada del dia martes:")
        if martes_1!="":            
            print(f"9:00 - {martes_1}") 
        else:
            print("9:00 - Disponible")
        if martes_2!="":            
            print(f"10:00 - {martes_2}")
        else:
            print("10:00 - Disponible")
        if martes_3!="":            
            print(f"11:00 - {martes_3}") 
        else:
            print("11:00 - Disponible")
    if opcion=="4":
        turnos_ocupados_lunes=0
        turnos_disponibles_lunes=0
        if lunes_1!="":
            turnos_ocupados_lunes+=1
        else:
            turnos_disponibles_lunes+=1
        if lunes_2!="":
            turnos_ocupados_lunes+=1
        else:
            turnos_disponibles_lunes+=1
        if lunes_3!="":
            turnos_ocupados_lunes+=1
        else:
            turnos_disponibles_lunes+=1
        if lunes_4!="":            
            turnos_ocupados_lunes+=1
        else:
            turnos_disponibles_lunes+=1
        turnos_ocupados_martes=0
        turnos_disponibles_martes=0
        if martes_1!="":
            turnos_ocupados_martes+=1
        else:
            turnos_disponibles_martes+=1
        if martes_2!="":            
            turnos_ocupados_martes+=1
        else:
            turnos_disponibles_martes+=1
        if martes_3!="":            
            turnos_ocupados_martes+=1
        else:
            turnos_disponibles_martes+=1
        print(f"""Resumen general:
        Lunes: ({turnos_ocupados_lunes}) turno/s ocupados, {turnos_disponibles_lunes} turno/s disponibles.
        Martes: ({turnos_ocupados_martes}) turno/s ocupados, {turnos_disponibles_martes} turno/s disponibles.""")
    if opcion=="5":
        print("Sistema cerrado.")
        break
print("////////////////////////")
#Ejercicio 4 "Escape Room: La Boveda"
energia = 100 
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""              

nombre = input("Nombre del agente: ")
while not nombre.isalpha(): 
    print("Error: solo letras")
    nombre = input("Nombre del agente: ")
racha_forzar = 0  

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):

    print("\n--- ESTADO ---")
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)


    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: opción inválida")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1  

        if racha_forzar == 3:
            print("¡La cerradura se trabó! Alarma activada")
            alarma = True 
        else:
            
            if energia < 40:
                num = input("Riesgo de alarma (1-3): ")

                while not num.isdigit() or int(num) not in [1, 2, 3]:
                    print("Error")
                    num = input("Riesgo de alarma (1-3): ")

                if int(num) == 3:
                    alarma = True
            if not alarma:
                cerraduras_abiertas += 1
                print("Abriste una cerradura")
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0  
        for i in range(4):
            print("Hackeando...")
            codigo_parcial += "A"  
       
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Hackeo exitoso! Se abrió una cerradura")

   
    elif opcion == 3:
        tiempo -= 1
        racha_forzar = 0  
        energia += 15
        if energia > 100:  
            energia = 100
        if alarma:
            energia -= 10

if cerraduras_abiertas == 3:
    print("¡VICTORIA, HAS ABIERTO LAS 3 CERRADURAS!")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")
elif alarma and tiempo <= 3:
    print("DERROTA: sistema bloqueado")
print("///////////////////////")
#Ejercicio 5 "Escape Room: La arena del Gladiador"
print("=== BIENVENIDO A LA ARENA ===")
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: solo letras")
    nombre = input("Nombre del Gladiador: ")
nombre= nombre.upper()

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12
turno_jugador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    if turno_jugador: 
        print(f"\n{nombre} - HP: {vida_jugador} vs Enemigo - HP: {vida_enemigo} | Pociones: {pociones}")
        print("1. Ataque pesado")
        print("2. Rafaga Veloz")
        print("3. Curar")
        opcion = input("Opción: ")
        while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
            print("Error: opción inválida")
            opcion = input("Opción: ")

        opcion = int(opcion)

        if opcion == 1:
            if vida_enemigo< 20:
                danio_base*= 1.5
            vida_enemigo -= danio_base
            print(f"¡Atacaste al enemigo por {danio_base} puntos de daño!")
        elif opcion == 2:
            for i in range(3):
                vida_enemigo -= 5
                print("¡Ráfaga Veloz!, Golpe conectado por 5 puntos de daño!")
        elif opcion == 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("¡Usaste una poción y recuperaste 30 puntos de vida!")
            else:
                print("¡No te quedan pociones!")
        turno_jugador = False  
    
    else:
        vida_jugador -= danio_enemigo
        print("¡El enemigo atacó por 12!")
        turno_jugador = True
    print("=== NUEVO TURNO ===")

if vida_jugador > 0:
    print(f"¡VICTORIA DE {nombre}!")
else:
    print("DERROTA")

