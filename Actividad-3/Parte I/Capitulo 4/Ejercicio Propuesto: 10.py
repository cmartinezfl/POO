import tkinter as tk

app = tk.Tk()
app.geometry("250x320")
tk.Wm.wm_title(app, "Datos")

#Num. Inscripcion
label_num = tk.Label(app, text="Numero de inscripcion: ")
label_num.pack()
entry_num = tk.Entry(app)
entry_num.pack()

#Nombres
label_name = tk.Label(app, text="Nombres:")
label_name.pack()
entry_name = tk.Entry(app)
entry_name.pack()

#Patrimonio
label_pat = tk.Label(app, text="Patrimonio: ")
label_pat.pack()
entry_pat = tk.Entry(app)
entry_pat.pack()

#Estrato social
label_est = tk.Label(app, text="Estrato social:")
label_est.pack()
entry_est = tk.Entry(app)
entry_est.pack()

def proceso():

    num= entry_num.get()
    name= entry_name.get()
    pat= float(entry_pat.get())
    est= float(entry_est.get())
    base = 50000
    incremento= 0.03

    if pat > 2000000 and est > 3:
        mat= base + (pat*incremento)

    else: 
        mat= base

    #show num
    label_r_num = tk.Label(app, text=f"Numero de inscripcion: {num}")
    label_r_num.pack()  

    #show name
    label_r_name = tk.Label(app, text=f"Nombres: {name}")
    label_r_name.pack() 

    #show mat
    label_mat = tk.Label(app, text=f"Pago por matricula: {mat:.2f} COP")
    label_mat.pack() 
    
boton = tk.Button(app, text= "Continuar", command= proceso)
boton.pack(pady=20)

app.mainloop()


