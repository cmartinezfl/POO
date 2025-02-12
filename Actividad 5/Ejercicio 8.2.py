import tkinter as tk
import math

app= tk.Tk()
app.geometry("250x400")
tk.Wm.wm_title(app, "Calificaciones")

label_nota1 = tk.Label(app, text="Nota 1:")
label_nota1.pack()
entry_nota1 = tk.Entry(app)
entry_nota1.pack()

label_nota2 = tk.Label(app, text="Nota 2:")
label_nota2.pack()
entry_nota2 = tk.Entry(app)
entry_nota2.pack()

label_nota3 = tk.Label(app, text="Nota 3:")
label_nota3.pack()
entry_nota3 = tk.Entry(app)
entry_nota3.pack()

label_nota4 = tk.Label(app, text="Nota 4:")
label_nota4.pack()
entry_nota4 = tk.Entry(app)
entry_nota4.pack()

label_nota5 = tk.Label(app, text="Nota 5:")
label_nota5.pack()
entry_nota5 = tk.Entry(app)
entry_nota5.pack()

def proceso():

    N = []

    n1 = float(entry_nota1.get())
    n2 = float(entry_nota2.get())
    n3 = float(entry_nota3.get())
    n4 = float(entry_nota4.get())
    n5 = float(entry_nota5.get())

    N.extend([n1,n2,n3,n4,n5])

    mayor = max(N)
    menor = min(N)

    promedio = round((n1 + n2 + n3 + n4 + n5)/5, 2)     

    suma = 0

    for i in N:

        resta = round(i - promedio, 2)

        cuadrado = round(resta**2,2)
        
        suma += cuadrado

    div = round(suma/4 , 2)

    raiz = math.sqrt(div)

    desviacion = round(raiz, 2)

    label_mayor = tk.Label(app, text=f"Mayor califiacion: {mayor}")
    label_mayor.pack()
    label_menor = tk.Label(app, text=f"Menor califiacion: {menor}")
    label_menor.pack() 
    label_promedio = tk.Label(app, text=f"Promedio de notas: {promedio}")
    label_promedio.pack()
    label_desviacion = tk.Label(app, text=f"Desviacion estandar: {desviacion}")
    label_desviacion.pack()

procesar = tk.Button(app, text="Procesar", command=proceso)
procesar.pack(pady=20)


app.mainloop()