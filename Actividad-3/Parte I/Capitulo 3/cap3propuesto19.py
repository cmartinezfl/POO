import tkinter as tk

app = tk.Tk()
app.geometry("200x200")
tk.Wm.wm_title(app, "Triangulo")

label_lado = tk.Label(app, text="Lado del triangulo:")
label_lado.pack(anchor="w")
entry_lado = tk.Entry(app)
entry_lado.pack(anchor="w")

def Calculo():
    Lado = float(entry_lado.get())

    perimetro = Lado * 3
    altura = (3**0.5 /2)*Lado
    area = (3**0.5 /4) * Lado**2

    label_perimetro = tk.Label(app, text=f"Perimetro: {perimetro:.2f}")
    label_perimetro.pack()

    label_altura = tk.Label(app, text=f"Perimetro: {altura:.2f}")
    label_altura.pack()

    label_area = tk.Label(app, text=f"Perimetro: {area:.2f}")
    label_area.pack()

calcular = tk.Button(app, text="Calcular", command=Calculo)
calcular.pack(pady=20)

app.mainloop()
