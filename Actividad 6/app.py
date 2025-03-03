import tkinter as tk
from tkinter import messagebox

app= tk.Tk()
app.geometry("270x460")
tk.Wm.wm_title(app, "Lista de pendientes")

pendientes=[]

label_descripcion = tk.Label(app, text="Con este programa generaras una lista de pendientes, puedes agregar pendientes, modificarlos y eliminar los finalizados.", wraplength=250)
label_descripcion.pack(pady=20)

def agregar_pendiente():

    pendiente = entry_pendiente.get().strip()
    
    if pendiente and pendiente not in pendientes:
        
        pendientes.append(pendiente)
        listbox.insert(tk.END, pendiente)
        entry_pendiente.delete(0, tk.END)

    elif pendiente in pendientes:
       
        messagebox.showerror("Error", "El pendiente ya está en la lista.")

def eliminar_pendiente():
   
    try:
        
        selected_index = listbox.curselection()[0]
        pendientes.pop(selected_index) 
        listbox.delete(selected_index)
        messagebox.showinfo("Éxito", "Pendiente eliminado correctamente.")
    
    except IndexError:
        
        messagebox.showerror("Error", "Seleccione un pendiente para eliminar.")        

def actualizar_pendiente():
    
    try:
        
        selected_index = listbox.curselection()[0] 
        nuevo_texto = entry_pendiente.get().strip()  

        if nuevo_texto and nuevo_texto not in pendientes:
           
            pendientes[selected_index] = nuevo_texto 
            listbox.delete(selected_index)  
            listbox.insert(selected_index, nuevo_texto)  
            entry_pendiente.delete(0, tk.END) 
        
        elif nuevo_texto in pendientes:
           
            messagebox.showerror("Error", "Ese pendiente ya existe.")
    
    except IndexError:
       
        messagebox.showerror("Error", "Seleccione un pendiente para actualizar.")

label_pendiente = tk.Label(app, text="Pendiente: ")
label_pendiente.pack(pady=5)

entry_pendiente = tk.Entry(app)
entry_pendiente.pack()

button_agregar = tk.Button(app, text="Agregar", command=agregar_pendiente)
button_agregar.pack(pady=10)

button_eliminar = tk.Button(app, text="Eliminar", command=eliminar_pendiente)
button_eliminar.pack(pady=10)

button_actualizar = tk.Button(app, text="Actualizar", command=actualizar_pendiente)
button_actualizar.pack(pady=10)


listbox = tk.Listbox(app, width=30, height=10)
listbox.pack()

app.mainloop()