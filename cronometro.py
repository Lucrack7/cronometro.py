import tkinter as tk

class Cronometro:
    def __init__(self, master):
        self.master = master
        self.master.title("⏱️ Cronómetro")
        self.master.geometry("300x150")
        self.master.resizable(False, False)

        self.segundos = 0
        self.en_ejecucion = False
        self.reloj = None

        # Etiqueta de tiempo
        self.label = tk.Label(master, text="00:00:00", font=("Consolas", 30))
        self.label.pack(pady=20)

        # Botones
        frame_botones = tk.Frame(master)
        frame_botones.pack()

        self.boton_iniciar = tk.Button(frame_botones, text="▶️ Iniciar", command=self.iniciar)
        self.boton_iniciar.grid(row=0, column=0, padx=5)

        self.boton_pausar = tk.Button(frame_botones, text="⏸️ Pausar", command=self.pausar)
        self.boton_pausar.grid(row=0, column=1, padx=5)

        self.boton_reiniciar = tk.Button(frame_botones, text="🔁 Reiniciar", command=self.reiniciar)
        self.boton_reiniciar.grid(row=0, column=2, padx=5)

    def formato_tiempo(self, s):
        h = s // 3600
        m = (s % 3600) // 60
        s = s % 60
        return f"{h:02}:{m:02}:{s:02}"

    def actualizar(self):
        if self.en_ejecucion:
            self.segundos += 1
            self.label.config(text=self.formato_tiempo(self.segundos))
            self.reloj = self.master.after(1000, self.actualizar)

    def iniciar(self):
        if not self.en_ejecucion:
            self.en_ejecucion = True
            self.actualizar()

    def pausar(self):
        if self.en_ejecucion:
            self.en_ejecucion = False
            if self.reloj:
                self.master.after_cancel(self.reloj)

    def reiniciar(self):
        self.pausar()
        self.segundos = 0
        self.label.config(text="00:00:00")

# Lanzamiento de la app
if __name__ == "__main__":
    root = tk.Tk()
    app = Cronometro(root)
    root.mainloop()
