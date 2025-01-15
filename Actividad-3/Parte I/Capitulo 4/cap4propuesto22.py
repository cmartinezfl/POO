import tkinter as tk

app = tk.Tk()
app.geometry("250x260")
tk.Wm.wm_title(app, "Datos")

l_nom = tk.Label(app, text= "Nombre empleado:")
l_nom.pack()
e_nom = tk.Entry(app)
e_nom.pack()

l_sal = tk.Label(app, text= "Salario/Hora:")
l_sal.pack()
e_sal = tk.Entry(app)
e_sal.pack()

l_num = tk.Label(app, text= "Horas trabajadas en el mes:")
l_num.pack()
e_num = tk.Entry(app)
e_num.pack()

def salario():
    sal= float(e_sal.get())
    horas= int(e_num.get())

    final_salario= sal * horas

    if final_salario > 450000:
        l_fnom = tk.Label(app, text= e_nom.get())
        l_fnom.pack()

        l_fsal = tk.Label(app, text= f"{final_salario:.2f} COP")
        l_fsal.pack()

    else: 
        l_fnom = tk.Label(app, text= e_nom.get())
        l_fnom.pack()

boton = tk.Button(app, text="Calcular Salario", command=salario)
boton.pack(pady=20)

app.mainloop()