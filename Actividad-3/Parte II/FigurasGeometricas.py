import tkinter as tk
import math

figuras = tk.Tk()
figuras.geometry("200x280")
tk.Wm.wm_title(figuras, "Figuras")

def circ():
    cir = tk.Tk()
    cir.geometry("400x160")
    tk.Wm.wm_title(cir, "Circulo")  

    l_rad = tk.Label(cir, text="Radio del circulo (cm):")
    l_rad.pack()
    e_rad = tk.Entry(cir)
    e_rad.pack()

    def cir_cal():
        radio = int(e_rad.get())

        perimetro = 2 * math.pi * radio
        area = math.pi * (radio ** 2)

        l_cir = tk.Label(cir, text=f"El circulo tiene perimetro: {perimetro:.2f} cm y un area de {area:.2f} cm")
        l_cir.pack(pady=10)


    b_cir = tk.Button(cir, text="Hallar area y perimetro", command = cir_cal)
    b_cir.pack()


    cir.mainloop()

circulo = tk.Button(figuras, text="Circulo", command=circ)
circulo.pack(pady=20)

def rect():
    rec = tk.Tk()
    rec.geometry("350x200")
    tk.Wm.wm_title(rec, "Rectangulo")  

    l_bas = tk.Label(rec, text="Base del rectangulo (cm):")
    l_bas.pack()
    e_bas = tk.Entry(rec)
    e_bas.pack()

    l_alt = tk.Label(rec, text="Altura del rectangulo (cm):")
    l_alt.pack()
    e_alt = tk.Entry(rec)
    e_alt.pack()

    def rec_cal():
        base= float(e_bas.get())
        altura= float(e_alt.get())

        perimetro= (2*base) + (2*altura)
        area= base*altura

        l_rec= tk.Label(rec, text= f"El rectangulo tiene perimetro: {perimetro:.2f} cm y un area de {area:.2f} cm")
        l_rec.pack(pady=10)

    b_rec = tk.Button(rec, text="Hallar area y perimetro", command = rec_cal)
    b_rec.pack()

    rec.mainloop()

rectangulo = tk.Button(figuras, text="Rectangulo", command=rect)
rectangulo.pack(pady=20)

def cuad():
    cua = tk.Tk()
    cua.geometry("350x180")
    tk.Wm.wm_title(cua, "Cuadrado")  

    l_lad = tk.Label(cua, text="Lado del cuadrado (cm):")
    l_lad.pack()
    e_lad = tk.Entry(cua)
    e_lad.pack()

    def cua_cal():
        lado = float(e_lad.get())

        perimetro = lado*4
        area = lado**2

        l_cua = tk.Label(cua, text=f"El cuadrado tiene perimetro: {perimetro:.2f} cm y un area de {area:.2f} cm")
        l_cua.pack(pady=10)
    
    
    b_cua = tk.Button(cua, text="Hallar area y perimetro", command = cua_cal)
    b_cua.pack()

    cua.mainloop()

cuadrado = tk.Button(figuras, text="Cuadrado", command=cuad)
cuadrado.pack(pady=20)

def tria():
    tri = tk.Tk()
    tri.geometry("350x240")
    tk.Wm.wm_title(tri, "Triangulo")  

    l_bas = tk.Label(tri, text="Base del triangulo (cm):")
    l_bas.pack()
    e_bas = tk.Entry(tri)
    e_bas.pack()

    l_alt = tk.Label(tri, text="Altura del triangulo (cm):")
    l_alt.pack()
    e_alt = tk.Entry(tri)
    e_alt.pack()

    def tri_cal1():
        base= float(e_bas.get())
        altura= float(e_alt.get())

        area = (1/2) * base * altura
        hipotenusa = math.sqrt((base**2) + (altura**2))
        perimetro = altura + base + hipotenusa 

        l_tri1 = tk.Label(tri, text= f"El triangulo tiene perimetro: {round(perimetro,2)} cm y un area de {round(area,2)} cm")
        l_tri1.pack(pady=10)

    def tri_cal2():
        base= float(e_bas.get())
        altura= float(e_alt.get())

        hipotenusa = math.sqrt((base**2) + (altura**2))

        if hipotenusa == base == altura:
            tipo = "Equilatero"

        elif hipotenusa != base != altura:
            tipo = "Escaleno"

        else:
            tipo = "Isosceles"

        l_tri2 = tk.Label(tri, text= f"El triangulo tiene hipotenusa: {round(hipotenusa,2)} cm y es un triangulo {tipo}")
        l_tri2.pack(pady=10)    

    b_tri = tk.Button(tri, text="Hallar area y perimetro", command = tri_cal1)
    b_tri.pack()

    b_tri = tk.Button(tri, text="Hallar hipotenusa y tipo", command = tri_cal2)
    b_tri.pack()

    tri.mainloop()

triangulo = tk.Button(figuras, text="Triangulo", command=tria)
triangulo.pack(pady=20)

figuras.mainloop()