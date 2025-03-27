import tkinter as tk
from cifrador import Cifrador
from tkinter import messagebox

class CifradorGUI:
    def __init__(self, root):
        self.cifrador = Cifrador()
        self.root = root
        self.root.title("Cifrador y Descifrador de Mensajes")
        self.root.geometry("500x400")
        self.root.configure(bg="#2c3e50")
        
        self.frame = tk.Frame(root, bg="#2c3e50")
        self.frame.pack(pady=10)
        
        tk.Label(self.frame, text="Cifrador y Descifrador", fg="white", bg="#2c3e50", font=("Arial", 16, "bold")).pack()
        
        tk.Button(self.frame, text="Generar Clave", command=self.cifrador.generar_clave, bg="#27ae60", fg="white", font=("Arial", 12)).pack(pady=5)
        
        tk.Label(self.frame, text="Mensaje / Mensaje Cifrado:", fg="white", bg="#2c3e50", font=("Arial", 12)).pack()
        self.entrada_mensaje = tk.Text(self.frame, height=5, width=50)
        self.entrada_mensaje.pack(pady=5)
        
        tk.Button(self.frame, text="Cifrar", command=self.cifrar_mensaje, bg="#2980b9", fg="white", font=("Arial", 12)).pack(pady=5)
        tk.Button(self.frame, text="Descifrar", command=self.descifrar_mensaje, bg="#c0392b", fg="white", font=("Arial", 12)).pack(pady=5)
        
        tk.Label(self.frame, text="Resultado:", fg="white", bg="#2c3e50", font=("Arial", 12)).pack()
        self.salida_mensaje = tk.Text(self.frame, height=5, width=50)
        self.salida_mensaje.pack(pady=5)

    def cifrar_mensaje(self):
        mensaje = self.entrada_mensaje.get("1.0", tk.END).strip()
        if not mensaje:
            messagebox.showerror("Error", "El mensaje no puede estar vacío.")
            return
        mensaje_cifrado = self.cifrador.cifrar(mensaje)
        self.salida_mensaje.delete("1.0", tk.END)
        self.salida_mensaje.insert(tk.END, mensaje_cifrado)
    
    def descifrar_mensaje(self):
        mensaje_cifrado = self.entrada_mensaje.get("1.0", tk.END).strip()
        if not mensaje_cifrado:
            messagebox.showerror("Error", "El mensaje cifrado no puede estar vacío.")
            return
        mensaje_descifrado = self.cifrador.descifrar(mensaje_cifrado)
        self.salida_mensaje.delete("1.0", tk.END)
        self.salida_mensaje.insert(tk.END, mensaje_descifrado if mensaje_descifrado else "Error al descifrar.")
