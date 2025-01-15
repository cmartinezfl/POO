import tkinter as tk

app = tk.Tk()
app.geometry("260x260")
tk.Wm.wm_title(app, "Ecuacion")

l_A = tk.Label(app, text= "A:")
l_A.pack()
e_A = tk.Entry(app)
e_A.pack()

l_B = tk.Label(app, text= "B:")
l_B.pack()
e_B = tk.Entry(app)
e_B.pack()

l_C = tk.Label(app, text= "C:")
l_C.pack()
e_C = tk.Entry(app)
e_C.pack()

def calculo():
    a = float(e_A.get())
    b = float(e_B.get())
    c = float(e_C.get())

    x = -b 
    y_1 = (b**2) - (4*a*c)

    if y_1 < 0:
        l_sol = tk.Label(app, text = "La solucion pertenece a los numeros complejos")
        l_sol.pack()

    else:
        y = (y_1)**0.5
        z = 2*a

        solucion_1 = (x + y) / z
        solucion_2 = (x - y) / z

        l_sol1 = tk.Label(app, text=f"Solucion 1: {solucion_1}")
        l_sol1.pack()
        l_sol2 = tk.Label(app, text=f"Solucion 2: {solucion_2}")
        l_sol2.pack()


boton = tk.Button(app, text = "Calcular", command = calculo)
boton.pack(pady=20)

app.mainloop()
