#Importamos la libreria para medir 
import time 
#Funcion que muestra el tiempo total del trayecto
def mostrar_duracion_total(tiempo_movimiento, tiempo_parado):
    duracion_total = tiempo_movimiento + tiempo_parado
    print(f"Has recorrido en total {duracion_total:.2f} segundos")
#Funcion para calcular la tarifa total del viaje 
def calcular_tarifa(kilometros, tiempo_parado, tiempo_movimiento):
    tarifa_base = 2.50 # Tarifa fija para iniciar el viaje
    tarifa_kilometro = kilometros * 1.50 # Tarifa por kilometro recorrido
    tarifa_parado = tiempo_parado * 0.02  # Coste por  cada segundo detenido
    tarifa_movimiento = tiempo_movimiento * 0.05  #Coste por cade  segundo en movimiento
    tarifa_total = tarifa_base + tarifa_kilometro + tarifa_parado + tarifa_movimiento
    return tarifa_total  # Devolvemos o retornamos la TARIFA_TOTAL
#Funcion principal del programa
def taximetro():
    #Bienvenida y explicacion del prototipo
    print("----------------------------------------------------------------")
    print("\n             Bienvenido al TAXIMETRO FACTORIA F5            \n")
    print("Este prototipo simula un taximetro digital de  nivel esencial ")
    print("Desde la linea de comandos (CLI) ")
    print("Calcula el costo de un viaje segun el tiempo detenido, el")
    print("tiempo en movimiento y los kilometros\n")
    print("Tarifas: ")
    print("  - Tarifa base: 2.50 €")
    print("  - por kilometro: 1.50 €")
    print("  - por segundo  detenido : 0.02 €")
    print("  - por segundo movimiento : 0.05 €\n")
    print("---------------------------------------------------------------")
    #Variables para controlar el estado del viaje
    viaje_iniciado = False  #Verifica si hemos iniciado o no el trayecto(variable booleana)
    estado = None # Puede ser PARADO o en MOVIMENTO
    tiempo_inicio_estado = 0 #Guarda el momento en que se cambio al estado actual
    tiempo_parado = 0  # Tiempo total acumulado en estado parado
    tiempo_movimiento = 0  # Tiempo total acumulado en movieminto
    #Bucle principal del programa
    while True:
        #Mostramos el menu de opciones
        print("                        MENU                            \n")
        print("          1 . Iniciar trayecto                            ")
        print("          2 . Cambiar estado (parado o movimeinto)        ")
        print("          3 . Finalizar viaje y calcular tarifa           ")
        print("          4 . Salir del programa                          ")
        #Guarda la opcion elegida por el usuario
        opcion = input("\nSelecciona una opcion (1-4): ").strip().lower()
        print("---------------------------------------------------------------")
        if opcion == '1':
            if viaje_iniciado:
                print("Hay un trayecto en curso")
            else:# Se inicializan todas las variables relacionadas con el trayecto
                viaje_iniciado = True 
                tiempo_inicio_estado  = time.time()#Tener cuidado esta linea
                tiempo_parado = 0
                tiempo_movimiento = 0
                estado = "parado" # -----> Iniciamos el trayecto con el estado PARADO
                print("Trayecto iniciado. ........!!! ")
                print("---------------------------------------------------------------")
        elif opcion == '2':
            if not viaje_iniciado:
                print("Primero debes iniciar el trayecto (opcion 1) para modificarlo")
            else:
                #Calcula la duracion desde el el ultimo cambio de estado
                tiempo_actual = time.time()
                duracion = tiempo_actual -  tiempo_inicio_estado
                print(f"\nTiempo en estado '{estado}' : {duracion:.2f} segundos ")
                if estado == "parado":
                    tiempo_parado += duracion
                else:
                    tiempo_movimiento += duracion
                #Pedimos el nuevo estado
                print(" A  qué estado quieres cambiar?")
                print(" - Escribe 'parado' si el taxi se detiene.")
                print(" - Escribe 'movimiento' si el taxi esta en moviemnto.")
                nuevo_estado = input("Nuevo estado: ").strip().lower()

                if nuevo_estado in ["parado" , "movimiento"]:
                    estado = nuevo_estado
                    tiempo_inicio_estado = time.time()
                    print(f"Estado actualizado a : {estado}")
                    print("---------------------------------------------------------------")
                else: 
                    print("Estado no valido. Solo puede ser: PARADO o MOVIMIENTO\n ")
        elif opcion == '3':
            if not viaje_iniciado:
                print("No hay  trayecto en curso")
            else:
                print("Has elegido finalizar el trayecto.........")
                tiempo_actual = time.time()
                duracion = tiempo_actual - tiempo_inicio_estado
                # Sumamos el tiempo final deependiendo del ultimo estado
                if estado == "parado":
                    tiempo_parado += duracion
                else:
                    tiempo_movimiento += duracion 
                
                km_valido = False
                #Pedimos los kilometros recorridos
                while not km_valido:
                    km_input = input("Ingresa los kilometros recorridos(puede tener decimales) ")
                    km_input = km_input.replace(',' , '.')
                    if km_input.replace('.', '', 1).isdigit():
                        kilometros = float(km_input)
                        km_valido = True
                    else:
                        print("ERROR: Solo se permiten numeros(pueden ser decimales) ")
                       
                #Calculamos la tarifa
                tarifa = calcular_tarifa(kilometros, tiempo_parado, tiempo_movimiento)
                #Mostramos el resumen del viaje
                print("---------------------------------------------------------------")
                print("                  RESUMEN DEL VIAJE                            ")
                print(f"kilometros recorridos: {kilometros:.2f} km")
                print(f"Tiempo detenido: {tiempo_parado:.2f} segundos")
                print(f"Tiempo en movimiento: {tiempo_movimiento:.2f}segundos")
                print(f"Tarifa total: {tarifa:.2f} €") 
                print("---------------------------------------------------------------")
                #Mostramo sla duracion total del trayecto
                mostrar_duracion_total(tiempo_movimiento, tiempo_parado)
                #Reiniciamos variables para un nuevo trayecto
                viaje_iniciado = False
                estado = None
                tiempo_inicio_estado = 0
        elif opcion == "4":
                #Salimos del programa
                print("Gracias por usar el TAXIMETRO FACTORIA F5....     !")
                break
        #En caso de opcion invalida 
        else:
            print("Opcion invalida. Ingresa un numero(1-4)")
#Invocamos a la Funcion Principal : TAXIMETRO 
if __name__ == "__main__":
    taximetro()

                    
