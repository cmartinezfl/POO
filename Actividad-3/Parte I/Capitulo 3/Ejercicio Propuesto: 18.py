import tkinter as tk

app = tk.Tk()
app.geometry("250x260")
tk.Wm.wm_title(app, "Datos")

label_code = tk.Label(app, text="Codigo:")
label_code.pack(anchor="w")
entry_code = tk.Entry(app)
entry_code.pack(anchor="w")

label_names = tk.Label(app, text="Nombres:")
label_names.pack(anchor="w")
entry_names = tk.Entry(app)
entry_names.pack(anchor="w")

label_horas = tk.Label(app, text="Horas trabajadas en el mes:")
label_horas.pack(anchor="w")
entry_horas = tk.Entry(app)
entry_horas.pack(anchor="w")

label_valor = tk.Label(app, text="Valor de hora:")
label_valor.pack(anchor="w")
entry_valor = tk.Entry(app)
entry_valor.pack(anchor="w")

label_retencion = tk.Label(app, text="Retencion (porcentaje):")
label_retencion.pack(anchor="w")
entry_retencion = tk.Entry(app)
entry_retencion.pack(anchor="w")

def mostrar_informacion():

    codigo = f"Codigo: {entry_code.get()}"
    nombres = f"Nombres: {entry_names.get()}"
    horas = entry_horas.get()
    valor = entry_valor.get()
    retencion_str = entry_retencion.get()
    retencion_float = float(retencion_str)
    retencion = retencion_float/100
    
    salario_bruto = int(horas)*int(valor)
    salario_neto = salario_bruto - (salario_bruto*retencion) 

    resultado_ventana = tk.Toplevel(app)
    resultado_ventana.geometry("300x130")
    resultado_ventana.title("Resultado")
    
    # Mostrar el mensaje en la nueva ventana
    label_codigo = tk.Label(resultado_ventana, text=codigo)
    label_codigo.pack(pady=2, anchor="w")

    label_nombres = tk.Label(resultado_ventana, text=nombres)
    label_nombres.pack(pady=2, anchor="w")

    label_bruto = tk.Label(resultado_ventana, text=f"Salario Bruto: {salario_bruto} COP")
    label_bruto.pack(pady=2, anchor="w")

    label_neto = tk.Label(resultado_ventana, text=f"Salario Neto: {int(salario_neto)} COP")
    label_neto.pack(pady=2, anchor="w")

calcular = tk.Button(app, text="Enviar", command=mostrar_informacion)
calcular.pack(pady=20)

app.mainloop()
