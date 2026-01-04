from customtkinter import *
import subprocess
import sys

class ConnectWindow(CTk):
    def __init__(self):
        super().__init__()

        self.name = "Player"
        self.host = "127.0.0.1"
        self.port = 8080

        self.title("Ping Pong Launcher")
        self.geometry("320x420")
        self.resizable(False, False)

        CTkLabel(self, text="🎮 Ping Pong Online", font=("Arial", 22, "bold")).pack(pady=20)

        self.name_entry = CTkEntry(self, placeholder_text="Нікнейм")
        self.name_entry.pack(pady=10, padx=30, fill="x")

        self.host_entry = CTkEntry(self, placeholder_text="IP сервера")
        self.host_entry.insert(0, "127.0.0.1")
        self.host_entry.pack(pady=10, padx=30, fill="x")

        self.port_entry = CTkEntry(self, placeholder_text="Порт")
        self.port_entry.insert(0, "8080")
        self.port_entry.pack(pady=10, padx=30, fill="x")

        self.status = CTkLabel(self, text="", text_color="red")
        self.status.pack(pady=5)

        CTkButton(
            self,
            text="ПРИЄДНАТИСЯ",
            height=45,
            command=self.on_connect
        ).pack(pady=20, padx=30, fill="x")

    def on_connect(self):
        if self.name_entry.get():
            self.name = self.name_entry.get()

        if self.host_entry.get():
            self.host = self.host_entry.get()

        try:
            self.port = int(self.port_entry.get())
        except ValueError:
            self.status.configure(text="❌ Невірний порт")
            return

        self.destroy()

        # Запуск клієнта pygame з аргументами
        subprocess.Popen([
            sys.executable,
            "client.py",
            self.host,
            str(self.port),
            self.name
        ])

if __name__ == "__main__":
    app = ConnectWindow()
    app.mainloop()
