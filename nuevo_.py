import tkinter as tk
import random

# Variables globales de vida y ataques especiales
vida_pc = 90
vida_usuario = 100
vidas_disponibles = 3
vidas_pc = 3

def actualizar_texto(mensaje_extra=""):
    etiqueta_estado.config(text=f"Vida PC: {vida_pc} | Vida Usuario: {vida_usuario}\n{mensaje_extra}")

def ataque_usuario(tipo):
    global vida_pc, sables_disponibles
    if tipo == "LANCE":
        vida_pc -= 10
        mensaje = "Usaste LANCE"
    elif tipo == "SABLE" and vida_disponibles > 0:
        vida_pc -= 15
        sables_disponibles -= 1
        mensaje = f"Usaste SABLE. Te quedan {vida_disponibles}."
    else:
        mensaje = "¡Ya no te quedan vidas!"

    if vida_pc <= 0:
        finalizar_juego("¡Ganaste!")

    actualizar_texto(mensaje)
    ventana.after(1000, ataque_pc)  # Espera 1 segundo y ataca la PC

def ataque_pc():
    global vida_usuario, sables_pc
    tipo = random.randint(1, 2)
    if tipo == 1:
        vida_usuario -= 10
        mensaje = "PC usó PC"
    elif tipo == 2 and vida_pc > 0:
        vida_usuario -= 15
        vida_pc -= 1
        mensaje = f"PC usó VIDA. Le quedan {vida_pc}."

    if vida_usuario <= 0:
        finalizar_juego("¡La PC te ganó!")

    actualizar_texto(mensaje)

def finalizar_juego(mensaje_final):
    boton_PC.config(state="disabled")
    boton_USUARIO.config(state="disabled")
    actualizar_texto(mensaje_final)

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Batalla: Usuario vs PC")
ventana.geometry("400x300")

etiqueta_estado = tk.Label(ventana, text="Presiona un botón para atacar", font=("Arial", 12))
etiqueta_estado.pack(pady=20)

boton_PC = tk.Button(ventana, text="PC", font=("Arial", 14), width=15, command=lambda: ataque_usuario("PC"))
boton_PC.pack(pady=5)

boton_USUARIO = tk.Button(ventana, text="USUARIO", font=("Arial", 14), width=15, command=lambda: ataque_usuario("USUARIO"))
boton_USUARIO.pack(pady=5)

ventana.mainloop()