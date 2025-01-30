import threading
import time

# Función para empacar productos
def empacar_pedidos():
    for i in range(5):
        print(f"[Empaque] Empacando pedido {i + 1}")
        time.sleep(1)  # Simula que tarda 1 segundo por pedido

# Función para procesar pagos
def procesar_pagos():
    for i in range(5):
        print(f"[Pago] Procesando pago para pedido {i + 1}")
        time.sleep(0.8)  # Simula que tarda 0.8 segundos por pago

# Función para enviar confirmaciones por correo
def enviar_correos():
    for i in range(5):
        print(f"[Correo] Enviando confirmación de pedido {i + 1}")
        time.sleep(1.2)  # Simula que tarda 1.2 segundos por correo

# Crear hilos para cada tarea
hilo_empaque = threading.Thread(target=empacar_pedidos)
hilo_pago = threading.Thread(target=procesar_pagos)
hilo_correo = threading.Thread(target=enviar_correos)

# Iniciar los hilos
hilo_empaque.start()
hilo_pago.start()
hilo_correo.start()

# Esperar a que los hilos terminen
hilo_empaque.join()
hilo_pago.join()
hilo_correo.join()

print("¡Todos los pedidos han sido procesados con éxito!")