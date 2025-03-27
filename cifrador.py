import os
from cryptography.fernet import Fernet
from tkinter import messagebox

class Cifrador:
    def __init__(self, clave_file="clave.key"):
        self.clave_file = clave_file
        if not os.path.exists(self.clave_file):
            self.generar_clave()

    def generar_clave(self):
        clave = Fernet.generate_key()
        with open(self.clave_file, "wb") as clave_file:
            clave_file.write(clave)
        messagebox.showinfo("Clave Generada", "Clave guardada en 'clave.key'")

    def cargar_clave(self):
        if not os.path.exists(self.clave_file):
            messagebox.showerror("Error", "No se encontró el archivo 'clave.key'. Genera una clave primero.")
            return None
        return open(self.clave_file, "rb").read()

    def cifrar(self, mensaje):
        clave = self.cargar_clave()
        if clave is None:
            return None
        fernet = Fernet(clave)
        return fernet.encrypt(mensaje.encode()).decode()

    def descifrar(self, mensaje_cifrado):
        clave = self.cargar_clave()
        if clave is None:
            return None
        fernet = Fernet(clave)
        try:
            return fernet.decrypt(mensaje_cifrado.encode()).decode()
        except Exception:
            messagebox.showerror("Error", "No se pudo descifrar el mensaje. Verifica la clave y el mensaje cifrado.")
            return None