import tkinter as tk

app = tk.Tk()
app.geometry("200x200")
tk.Wm.wm_title(app, "Comparacion")

label_A = tk.Label(app, text="A: ")
label_A.pack(anchor="w")
entry_A = tk.Entry(app)
entry_A.pack(anchor="w")

label_B = tk.Label(app, text="B: ")
label_B.pack(anchor="w")
entry_B = tk.Entry(app)
entry_B.pack(anchor="w")

def comparar():

    A= float(entry_A.get())
    B= float(entry_B.get())
    comparacion = "..."

    if A>B:
        comparacion = "mayor"

    elif B>A:
        comparacion = "menor"

    elif A==B:
        comparacion = "igual"
    
    mensaje = f"A es {comparacion} que B"

    label_resultado = tk.Label(app, text=mensaje)
    label_resultado.pack(pady=5)

boton = tk.Button(app, text="Comparar", command=comparar)
boton.pack(pady=20)

app.mainloop()
