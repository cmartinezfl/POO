import tkinter as tk
import math

app= tk.Tk()
app.geometry("200x200")
tk.Wm.wm_title(app, "Figuras")

def cil():
    cil= tk.Tk()
    cil.geometry("300x250")
    tk.Wm.wm_title(cil, "Cilindro")

    l_rad = tk.Label(cil, text="Radio del Cilindro (cm):")
    l_rad.pack()
    e_rad = tk.Entry(cil)
    e_rad.pack()

    l_alt = tk.Label(cil, text="Altura del Cilindro (cm):")
    l_alt.pack()
    e_alt = tk.Entry(cil)
    e_alt.pack()

    def cal_cil():

        rad = float(e_rad.get())
        alt = float(e_alt.get())


        volumen = math.pi * (rad**2) * alt
        superficie = 2 * math.pi * rad * (rad + alt)

        l_vol = tk.Label(cil, text= f"Volumen del Cilindro (cm): {volumen:.2f} cm²")
        l_vol.pack()
        l_sup = tk.Label(cil, text= f"Superficie del Cilindro (cm): {superficie:.2f} cm²")
        l_sup.pack()


    b_cil = tk.Button(cil, text="Calcular", command=cal_cil)
    b_cil.pack(pady=20)    

    cil.mainloop()

cilindro = tk.Button(app, text="Cilindro", command=cil)
cilindro.pack(pady=20)

def esf():
    esf= tk.Tk()
    esf.geometry("300x250")
    tk.Wm.wm_title(esf, "Esfera")

    l_rad = tk.Label(esf, text="Radio de la Esfera (cm):")
    l_rad.pack()
    e_rad = tk.Entry(esf)
    e_rad.pack()

    def cal_esf():

        rad = float(e_rad.get())

        volumen = (4/3) * math.pi * (rad**3)
        superficie = 4 * math.pi * (rad**2)

        l_vol = tk.Label(esf, text= f"Volumen de la Esfera (cm): {volumen:.2f} cm²")
        l_vol.pack()
        l_sup = tk.Label(esf, text= f"Superficie de la Esfera (cm): {superficie:.2f} cm²")
        l_sup.pack()    

    b_esf = tk.Button(esf, text="Calcular", command=cal_esf)
    b_esf.pack(pady=20) 

    esf.mainloop()

esfera = tk.Button(app, text="Esfera", command=esf)
esfera.pack(pady=20)

def pir():
    pir= tk.Tk()
    pir.geometry("300x250")
    tk.Wm.wm_title(pir, "Piramide")

    l_base = tk.Label(pir, text="Base de la Piramide (cm):")
    l_base.pack()
    e_base = tk.Entry(pir)
    e_base.pack()

    l_alt = tk.Label(pir, text="Altura de la Piramide (cm):")
    l_alt.pack()
    e_alt = tk.Entry(pir)
    e_alt.pack()

    l_apo = tk.Label(pir, text="Apotema de la Piramide (cm):")
    l_apo.pack()
    e_apo = tk.Entry(pir)
    e_apo.pack()

    def cal_pir():

        base = float(e_base.get())
        alt = float(e_alt.get())
        apo = float(e_apo.get())

        areab = base**2
        perimb = base*4
        arealat = (perimb * apo) / 2 

        superficie = areab + arealat
        volumen = (1/3) * areab * alt

        l_vol = tk.Label(pir, text= f"Volumen de la Piramide (cm): {volumen:.2f} cm²")
        l_vol.pack()
        l_sup = tk.Label(pir, text= f"Superficie de la Piramide (cm): {superficie:.2f} cm²")
        l_sup.pack()


    b_pir = tk.Button(pir, text="Calcular", command=cal_pir)
    b_pir.pack(pady=20)  

    pir.mainloop()

Piramide = tk.Button(app, text="Piramide", command=pir)
Piramide.pack(pady=20)

app.mainloop()