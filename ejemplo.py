import threading
import time

# Función para empacar productos
def empacar_pedidos():
    for i in range(5):
        print(f"[Empaque] Inicio de empaque de pedido {i + 1}")
        time.sleep(1)  # Simula que tarda 1 segundo por pedido

# Función para procesar pagos
def procesar_pagos():
    for i in range(5):
        print(f"[Pago] Procesamiento para pago {i + 1}")
        time.sleep(0.8)  # Simula que tarda 0.8 segundos por pago

# Función para enviar confirmaciones por correo
def enviar_correos():
    for i in range(5):
        print(f"[camikasiandrea2017@gmail.com] Enviando confirmación de pedido {i + 1}")
        time.sleep(1.2)  # Simula que tarda 1.2 segundos por correo

# Crear hilos para cada tarea
hilo_empacando = threading.Thread(target=empacar_pedidos)
hilo_recepcion_pago = threading.Thread(target=procesar_pagos)
hilo_enviar_correos = threading.Thread(target=enviar_correos)

# Iniciar los hilos
hilo_empacando.start()
hilo_recepcion_pago.start()
hilo_enviar_correos.start()

# Esperar a que los hilos terminen
hilo_empacando.join()
hilo_recepcion_pago.join()
hilo_enviar_correos.join()

print("Exito en todos los procesos de pedidos!")