from tkinter import ttk
import tkinter as t
from tkinter import messagebox
from convertidor import *

#Pantalla
root = t.Tk()
root.title("Convertidor de Bases")
root.geometry("500x500")
root.resizable(0,0)

icono = t.PhotoImage(file="unnamed.png")
root.iconphoto(True,icono,icono)
#=================================

#funciones
base = 2
conv = 10
def ingresar_lista():
    archivo = open("Datos/cache.txt", "r")
    leer = archivo.readlines()
    for i in leer:
        i = i.strip()
        me_lista.insert(t.END, i)
    archivo.close()

def entry_origen_ajuste(arg):
    e_Marco_og.configure(height=(e_Marco_og.get().count('\n') + 1))
        
def Memoria_boton():
    guardar = e_Marco_og.get()
    
    if (guardar == ""):
        messagebox.showinfo("Error al guardar","Debes ingresar al menos un valor para poder guardar un valor de cualquier base")
        return
    else:
        mantener = open("Datos/cache.txt", "r")
        for i in mantener:
            if (i == f"{guardar}\n"):
                messagebox.showinfo("Error al guardar","Ya existe el mismo dato, ingresa otro de nuevo")
                mantener.close()
                return
        me_lista.insert(t.END, guardar)
        mantener.close()
        
        archivo = open("Datos/cache.txt", "a")
        archivo.write(f"{guardar}\n")
        archivo.close()
        
        e_Marco_og.config(state="normal")
        e_Marco_og.delete(0, t.END)
        e_Marco_og.config(state="readonly")
    
def memory_borrar_boton():
    archivo = open("Datos/cache.txt", "r")
    indice = me_lista.curselection()
    leer = archivo.readlines()
    archivo.close()
    
    try:
        dato = me_lista.get(indice)
    except:
        messagebox.showinfo("Error al borrar","Debes seleccionar un valor para borrar")
        return
    
    sobreescribir = open("Datos/cache.txt", "w")
    guardar = []
    
    for i in leer:
        i = i.strip()
        if (i != dato):
            guardar += [f"{i}\n"]

    for i in guardar:
        sobreescribir.write(i)
    sobreescribir.close()
    me_lista.delete(indice,indice)
    
    return
def restaurar_boton():
    indice = me_lista.curselection()
    try:
        dato = me_lista.get(indice)
    except:
        messagebox.showinfo("Error al restaurar","Debes seleccionar un valor para restaurar")
        return
    
    if (dato == ""):
        messagebox.showinfo("Error al restaurar","Debes seleccionar un valor para restaurar")
        return
    
    if (base == 2):
        try:
            num = int(dato)
        except:
            messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
            return
        
        for i in dato:
            i = int(i)
            if (i < 0) or (i > 1):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
            
    elif (base == 3):
        try:
            num = int(dato)
        except:
            messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
            return
        
        for i in dato:
            i = int(i)
            if (i < 0) or (i > 2):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
            
    elif (base == 4):
        try:
            num = int(dato)
        except:
            messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
            return
        
        for i in dato:
            i = int(i)
            if (i < 0) or (i > 3):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
            
    elif (base == 5):
        try:
            num = int(dato)
        except:
            messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
            return
        
        for i in dato:
            i = int(i)
            if (i < 0) or (i > 5):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
            
    elif (base == 6):
        try:
            num = int(dato)
        except:
            messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
            return
        
        for i in dato:
            i = int(i)
            if (i < 0) or (i > 5):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
    
    elif (base == 7):
        try:
            num = int(dato)
        except:
            messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
            return
        
        for i in dato:
            i = int(i)
            if (i < 0) or (i > 6):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
            
    elif (base == 8):
        try:
            num = int(dato)
        except:
            messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
            return
        
        for i in dato:
            i = int(i)
            if (i < 0) or (i > 7):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
            
    elif (base == 9):
        try:
            num = int(dato)
        except:
            messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
            return
        
        for i in dato:
            i = int(i)
            if (i < 0) or (i > 8):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
            
    elif (base == 10):
        try:
            num = int(dato)
        except:
            messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
            return
        
        for i in dato:
            i = int(i)
            if (i < 0) or (i > 9):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
            
    elif (base == 11):
        validar = ["0","1","2","3","4","5","6","7","8","9","A"]
        
        for i in dato:
            check = False
            for x in validar:
                if (i == x):
                    check = True
            if (check == False):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
        
    elif (base == 12):
        validar = ["0","1","2","3","4","5","6","7","8","9","A","B"]
        
        for i in dato:
            check = False
            for x in validar:
                if (i == x):
                    check = True
            if (check == False):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
        
    elif (base == 13):
        validar = ["0","1","2","3","4","5","6","7","8","9","A","B","C"]
        
        for i in dato:
            check = False
            for x in validar:
                if (i == x):
                    check = True
            if (check == False):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
    
    elif (base == 14):
        validar = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D"]
        
        for i in dato:
            check = False
            for x in validar:
                if (i == x):
                    check = True
            if (check == False):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
    
    elif (base == 15):
        validar = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E"]
        
        for i in dato:
            check = False
            for x in validar:
                if (i == x):
                    check = True
            if (check == False):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
        
    elif (base == 16):
        validar = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        
        for i in dato:
            check = False
            for x in validar:
                if (i == x):
                    check = True
            if (check == False):
                messagebox.showinfo("Error al restaurar","El valor no se puede restaurar debido a que la base origen no concuerda")
                return
        
    e_Marco_og.config(state="normal")
    e_Marco_og.delete(0, t.END)
    e_Marco_og.insert(0,f"{dato}")
    e_Marco_og.config(state="readonly")
            

def contarCaracter(valor):
    contador = 0
    for i in valor:
        contador += 1
    
    return contador -1
def boton_borrar_todo():
    e_Marco_og.config(state="normal")
    e_Marco_og.delete(0, t.END)
    e_Marco_og.config(state="readonly")

def boton_borrar():
    e_Marco_og.config(state="normal")
    e_Marco_og.delete(contarCaracter(e_Marco_og.get()),t.END)
    e_Marco_og.config(state="readonly")
    
def boton_valor(valor):
    e_Marco_og.config(state="normal")
    salvar = e_Marco_og.get()
    e_Marco_og.delete(0, t.END)
    e_Marco_og.insert(0, str(salvar) + str(valor))
    e_Marco_og.config(state="readonly")

def boton_convertir():
    convertir = e_Marco_og.get()
    if (convertir == ""):
        messagebox.showinfo("Error al calcular","Debes ingresar al menos un valor para poder convertir a cualquier base")
        return
    if (base == 2):
        convertir = int(convertir)
        if (conv == 2):
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(convertir))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 3):
            res = base2_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 4):
            res = base2_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 5):
            res = base2_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 6):
            res = base2_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 7):
            res = base2_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 8):
            res = base2_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 9):
            res = base2_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 10):
            res = base2_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 11):
            res = base2_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 12):
            res = base2_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 13):
            res = base2_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 14):
            res = base2_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 15):
            res = base2_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 16):
            res = base2_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
    elif (base == 3):
        convertir = int(convertir)
        if (conv == 2):
            res = base3_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base3_a_base3(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(convertir))
            e_Marco_ds.config(state="readonly")
        elif (conv == 4):
            res = res = base3_a_base4(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 5):
            res = res = base3_a_base5(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = res = base3_a_base6(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = res = base3_a_base7(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = res = base3_a_base8(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = res = base3_a_base9(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = res = base3_a_base10(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = res = base3_a_base11(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = res = base3_a_base12(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = res = base3_a_base13(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = res = base3_a_base14(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = res = base3_a_base15(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = res = base3_a_base16(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
    elif (base == 4):
        convertir = int(convertir)
        if (conv == 2):
            res = base4_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base4_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(convertir))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base4_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base4_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base4_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base4_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base4_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base4_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base4_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base4_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base4_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base4_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base4_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base4_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
    elif (base == 5):
        convertir = int(convertir)
        if (conv == 2):
            res = base5_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base5_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base5_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base5_a_base5(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(convertir))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base5_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base5_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base5_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base5_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base5_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base5_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base5_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base5_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base5_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base5_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base5_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
    elif (base == 6):
        convertir = int(convertir)
        if (conv == 2):
            res = base6_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base6_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base6_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base6_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(convertir))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base6_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base6_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base6_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base6_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base6_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base6_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base6_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base6_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base6_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base6_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
    elif (base == 7):
        convertir = int(convertir)
        if (conv == 2):
            res = base7_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base7_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base7_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base7_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base7_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(convertir))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base7_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base7_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base7_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base7_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base7_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base7_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base7_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base7_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base7_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
    elif (base == 8):
        convertir = int(convertir)
        if (conv == 2):
            res = base8_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base8_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base8_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base8_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base8_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base8_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(convertir))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base8_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base8_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base8_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base8_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base8_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base8_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base8_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base8_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
    elif (base == 9):
        convertir = int(convertir)
        if (conv == 2):
            res = base9_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base9_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base9_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base9_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base9_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base9_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base9_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(convertir))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base9_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base9_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base9_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base9_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base9_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base9_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base9_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        
    elif (base == 10):
        convertir = int(convertir)
        if (conv == 2):
            res = base10_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base10_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base10_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base10_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base10_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base10_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base10_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base10_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base10_a_base10(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(convertir))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base10_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base10_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base10_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base10_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base10_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base10_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
    elif (base == 11):
        
        if (conv == 2):
            res = base11_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base11_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base11_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base11_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base11_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base11_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base11_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base11_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base11_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base11_a_base11(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(convertir))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base11_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base11_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")

        elif (conv == 14):
            res = base11_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base11_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base11_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
    elif (base == 12):
        
        if (conv == 2):
            res = base12_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base12_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base12_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base12_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base12_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base12_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base12_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base12_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base12_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base12_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base12_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base12_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base12_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base12_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base12_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
    elif (base == 13):
        
        if (conv == 2):
            res = base13_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base13_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base13_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base13_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base13_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base13_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base13_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base13_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base13_a_base10(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base13_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base13_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base13_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base13_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base13_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base13_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
    elif (base == 14):
        
        if (conv == 2):
            res = base14_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base14_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base14_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base14_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base14_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base14_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base14_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base14_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base14_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base14_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base14_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base14_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base14_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base14_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base14_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
    elif (base == 15):
        
        if (conv == 2):
            res = base15_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base15_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base15_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base15_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base15_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base15_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base15_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base15_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base15_a_base10(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base15_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base15_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base15_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base15_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base15_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base15_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
    elif (base == 16):
        
        if (conv == 2):
            res = base16_a_base2(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 3):
            res = base16_a_base3(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        
        elif (conv == 4):
            res = base16_a_base4(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
        elif (conv == 5):
            res = base16_a_base5(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 6):
            res = base16_a_base6(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 7):
            res = base16_a_base7(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 8):
            res = base16_a_base8(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 9):
            res = base16_a_base9(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 10):
            res = base16_a_base10(convertir)
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 11):
            res = base16_a_base11(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 12):
            res = base16_a_base12(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 13):
            res = base16_a_base13(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 14):
            res = base16_a_base14(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 15):
            res = base16_a_base15(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
        elif (conv == 16):
            res = base16_a_base16(convertir)
            
            e_Marco_ds.config(state="normal")
            e_Marco_ds.delete(0, t.END)
            e_Marco_ds.insert(0, str(res))
            e_Marco_ds.config(state="readonly")
            
def Valores_OG(arg):
    global base
    e_Marco_og.config(state="normal")
    e_Marco_og.delete(0, t.END)
    seleccion = d_marco_og.get()
    
    for i in marco_val.winfo_children():
        i.destroy()
    if (seleccion == "Base 2"):
        base = 2
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)

        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
    elif (seleccion == "Base 3"):
        base = 3
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)

        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
    elif (seleccion == "Base 4"):
        base = 4
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
    elif (seleccion == "Base 5"):
        base = 5
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
    elif (seleccion == "Base 6"):
        base = 6
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
    elif (seleccion == "Base 7"):
        base = 7
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
        b_seis = t.Button(marco_val, text="6", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("6"))
        b_seis.grid(row=2,column=2,padx=2)
        b_seis.place_configure(height=40,x=110,y=100)
        
    elif (seleccion == "Base 8"):
        base = 8
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
        b_seis = t.Button(marco_val, text="6", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("6"))
        b_seis.grid(row=2,column=2,padx=2)
        b_seis.place_configure(height=40,x=110,y=100)
        
        b_siete = t.Button(marco_val, text="7", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("7"))
        b_siete.grid(row=2,column=3,padx=2)
        b_siete.place_configure(height=40,x=165,y=100)
    
    elif (seleccion == "Base 9"):
        base = 9
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
        b_seis = t.Button(marco_val, text="6", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("6"))
        b_seis.grid(row=2,column=2,padx=2)
        b_seis.place_configure(height=40,x=110,y=100)
        
        b_siete = t.Button(marco_val, text="7", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("7"))
        b_siete.grid(row=2,column=3,padx=2)
        b_siete.place_configure(height=40,x=165,y=100)
        
        #Tercera Fila
        b_ocho = t.Button(marco_val, text="8", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("8"))
        b_ocho.grid(row=3,column=0,padx=2,pady=15)
        b_ocho.place_configure(height=40,y=150)
        
    elif (seleccion == "Base 10"):
        base = 10
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
        b_seis = t.Button(marco_val, text="6", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("6"))
        b_seis.grid(row=2,column=2,padx=2)
        b_seis.place_configure(height=40,x=110,y=100)
        
        b_siete = t.Button(marco_val, text="7", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("7"))
        b_siete.grid(row=2,column=3,padx=2)
        b_siete.place_configure(height=40,x=165,y=100)
        
        #Tercera Fila
        b_ocho = t.Button(marco_val, text="8", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("8"))
        b_ocho.grid(row=3,column=0,padx=2,pady=15)
        b_ocho.place_configure(height=40,y=150)
        
        b_nueve = t.Button(marco_val, text="9", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("9"))
        b_nueve.grid(row=3,column=1,padx=2,pady=15)
        b_nueve.place_configure(height=40,y=150,x=55)
    
    elif (seleccion == "Base 11"):
        base = 11
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
        b_seis = t.Button(marco_val, text="6", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("6"))
        b_seis.grid(row=2,column=2,padx=2)
        b_seis.place_configure(height=40,x=110,y=100)
        
        b_siete = t.Button(marco_val, text="7", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("7"))
        b_siete.grid(row=2,column=3,padx=2)
        b_siete.place_configure(height=40,x=165,y=100)
        
        #Tercera Fila
        b_ocho = t.Button(marco_val, text="8", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("8"))
        b_ocho.grid(row=3,column=0,padx=2,pady=15)
        b_ocho.place_configure(height=40,y=150)
        
        b_nueve = t.Button(marco_val, text="9", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("9"))
        b_nueve.grid(row=3,column=1,padx=2,pady=15)
        b_nueve.place_configure(height=40,y=150,x=55)
        
        b_A = t.Button(marco_val, text="A", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("A"))
        b_A.grid(row=3,column=2,padx=2,pady=15)
        b_A.place_configure(height=40,y=150,x=110)
        
    elif (seleccion == "Base 12"):
        base = 12
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
        b_seis = t.Button(marco_val, text="6", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("6"))
        b_seis.grid(row=2,column=2,padx=2)
        b_seis.place_configure(height=40,x=110,y=100)
        
        b_siete = t.Button(marco_val, text="7", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("7"))
        b_siete.grid(row=2,column=3,padx=2)
        b_siete.place_configure(height=40,x=165,y=100)
        
        #Tercera Fila
        b_ocho = t.Button(marco_val, text="8", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("8"))
        b_ocho.grid(row=3,column=0,padx=2,pady=15)
        b_ocho.place_configure(height=40,y=150)
        
        b_nueve = t.Button(marco_val, text="9", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("9"))
        b_nueve.grid(row=3,column=1,padx=2,pady=15)
        b_nueve.place_configure(height=40,y=150,x=55)
        
        b_A = t.Button(marco_val, text="A", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("A"))
        b_A.grid(row=3,column=2,padx=2,pady=15)
        b_A.place_configure(height=40,y=150,x=110)
        
        b_B = t.Button(marco_val, text="B", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("B"))
        b_B.grid(row=3,column=3,padx=2,pady=15)
        b_B.place_configure(height=40,y=150,x=165)
    
    elif (seleccion == "Base 13"):
        base = 13
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
        b_seis = t.Button(marco_val, text="6", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("6"))
        b_seis.grid(row=2,column=2,padx=2)
        b_seis.place_configure(height=40,x=110,y=100)
        
        b_siete = t.Button(marco_val, text="7", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("7"))
        b_siete.grid(row=2,column=3,padx=2)
        b_siete.place_configure(height=40,x=165,y=100)
        
        #Tercera Fila
        b_ocho = t.Button(marco_val, text="8", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("8"))
        b_ocho.grid(row=3,column=0,padx=2,pady=15)
        b_ocho.place_configure(height=40,y=150)
        
        b_nueve = t.Button(marco_val, text="9", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("9"))
        b_nueve.grid(row=3,column=1,padx=2,pady=15)
        b_nueve.place_configure(height=40,y=150,x=55)
        
        b_A = t.Button(marco_val, text="A", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("A"))
        b_A.grid(row=3,column=2,padx=2,pady=15)
        b_A.place_configure(height=40,y=150,x=110)
        
        b_B = t.Button(marco_val, text="B", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("B"))
        b_B.grid(row=3,column=3,padx=2,pady=15)
        b_B.place_configure(height=40,y=150,x=165)
        
        #Cuarta Fila
        b_C = t.Button(marco_val, text="C", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("C"))
        b_C.grid(row=4,column=0,padx=2)
        b_C.place_configure(height=40,y=200)
        
    elif (seleccion == "Base 14"):
        base = 14
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
        b_seis = t.Button(marco_val, text="6", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("6"))
        b_seis.grid(row=2,column=2,padx=2)
        b_seis.place_configure(height=40,x=110,y=100)
        
        b_siete = t.Button(marco_val, text="7", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("7"))
        b_siete.grid(row=2,column=3,padx=2)
        b_siete.place_configure(height=40,x=165,y=100)
        
        #Tercera Fila
        b_ocho = t.Button(marco_val, text="8", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("8"))
        b_ocho.grid(row=3,column=0,padx=2,pady=15)
        b_ocho.place_configure(height=40,y=150)
        
        b_nueve = t.Button(marco_val, text="9", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("9"))
        b_nueve.grid(row=3,column=1,padx=2,pady=15)
        b_nueve.place_configure(height=40,y=150,x=55)
        
        b_A = t.Button(marco_val, text="A", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("A"))
        b_A.grid(row=3,column=2,padx=2,pady=15)
        b_A.place_configure(height=40,y=150,x=110)
        
        b_B = t.Button(marco_val, text="B", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("B"))
        b_B.grid(row=3,column=3,padx=2,pady=15)
        b_B.place_configure(height=40,y=150,x=165)
        
        #Cuarta Fila
        b_C = t.Button(marco_val, text="C", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("C"))
        b_C.grid(row=4,column=0,padx=2)
        b_C.place_configure(height=40,y=200)
        
        b_D = t.Button(marco_val, text="D", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("D"))
        b_D.grid(row=4,column=1,padx=2)
        b_D.place_configure(height=40,y=200,x=55)
        
    elif (seleccion == "Base 15"):
        base = 15
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
        b_seis = t.Button(marco_val, text="6", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("6"))
        b_seis.grid(row=2,column=2,padx=2)
        b_seis.place_configure(height=40,x=110,y=100)
        
        b_siete = t.Button(marco_val, text="7", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("7"))
        b_siete.grid(row=2,column=3,padx=2)
        b_siete.place_configure(height=40,x=165,y=100)
        
        #Tercera Fila
        b_ocho = t.Button(marco_val, text="8", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("8"))
        b_ocho.grid(row=3,column=0,padx=2,pady=15)
        b_ocho.place_configure(height=40,y=150)
        
        b_nueve = t.Button(marco_val, text="9", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("9"))
        b_nueve.grid(row=3,column=1,padx=2,pady=15)
        b_nueve.place_configure(height=40,y=150,x=55)
        
        b_A = t.Button(marco_val, text="A", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("A"))
        b_A.grid(row=3,column=2,padx=2,pady=15)
        b_A.place_configure(height=40,y=150,x=110)
        
        b_B = t.Button(marco_val, text="B", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("B"))
        b_B.grid(row=3,column=3,padx=2,pady=15)
        b_B.place_configure(height=40,y=150,x=165)
        
        #Cuarta Fila
        b_C = t.Button(marco_val, text="C", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("C"))
        b_C.grid(row=4,column=0,padx=2)
        b_C.place_configure(height=40,y=200)
        
        b_D = t.Button(marco_val, text="D", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("D"))
        b_D.grid(row=4,column=1,padx=2)
        b_D.place_configure(height=40,y=200,x=55)
        
        b_E = t.Button(marco_val, text="E", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("E"))
        b_E.grid(row=4,column=2,padx=2)
        b_E.place_configure(height=40,y=200,x=110)
        
    elif (seleccion == "Base 16"):
        base = 16
        
        b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
        b_CE.grid(row=0,column=0,padx=2)
        b_CE.place_configure(height=40)

        b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
        b_M.grid(row=0,column=1,padx=2)
        b_M.place_configure(height=40,x=55)
        
        b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
        b_borrar.grid(row=0,column=2,padx=2)
        b_borrar.place(x=109,width=105,height=40)
        
        #Fila Uno
        b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
        b_cero.grid(row=1,column=0,padx=2,pady=15)
        b_cero.place_configure(height=40,y=50)
                
        b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
        b_uno.grid(row=1,column=1,padx=2,pady=15)
        b_uno.place_configure(height=40,x=55,y=50)
        
        b_dos = t.Button(marco_val, text="2", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("2"))
        b_dos.grid(row=1,column=2,padx=2,pady=15)
        b_dos.place_configure(height=40,x=110,y=50)
        
        b_tres = t.Button(marco_val, text="3", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("3"))
        b_tres.grid(row=1,column=3,padx=2,pady=15)
        b_tres.place_configure(height=40,x=165,y=50)
        
        #Segunda fila
        b_cuatro = t.Button(marco_val, text="4", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("4"))
        b_cuatro.grid(row=2,column=0,padx=2)
        b_cuatro.place_configure(height=40,y=100)
        
        b_cinco = t.Button(marco_val, text="5", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("5"))
        b_cinco.grid(row=2,column=1,padx=2)
        b_cinco.place_configure(height=40,x=55,y=100)
        
        b_seis = t.Button(marco_val, text="6", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("6"))
        b_seis.grid(row=2,column=2,padx=2)
        b_seis.place_configure(height=40,x=110,y=100)
        
        b_siete = t.Button(marco_val, text="7", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("7"))
        b_siete.grid(row=2,column=3,padx=2)
        b_siete.place_configure(height=40,x=165,y=100)
        
        #Tercera Fila
        b_ocho = t.Button(marco_val, text="8", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("8"))
        b_ocho.grid(row=3,column=0,padx=2,pady=15)
        b_ocho.place_configure(height=40,y=150)
        
        b_nueve = t.Button(marco_val, text="9", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("9"))
        b_nueve.grid(row=3,column=1,padx=2,pady=15)
        b_nueve.place_configure(height=40,y=150,x=55)
        
        b_A = t.Button(marco_val, text="A", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("A"))
        b_A.grid(row=3,column=2,padx=2,pady=15)
        b_A.place_configure(height=40,y=150,x=110)
        
        b_B = t.Button(marco_val, text="B", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("B"))
        b_B.grid(row=3,column=3,padx=2,pady=15)
        b_B.place_configure(height=40,y=150,x=165)
        
        #Cuarta Fila
        b_C = t.Button(marco_val, text="C", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("C"))
        b_C.grid(row=4,column=0,padx=2)
        b_C.place_configure(height=40,y=200)
        
        b_D = t.Button(marco_val, text="D", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("D"))
        b_D.grid(row=4,column=1,padx=2)
        b_D.place_configure(height=40,y=200,x=55)
        
        b_E = t.Button(marco_val, text="E", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("E"))
        b_E.grid(row=4,column=2,padx=2)
        b_E.place_configure(height=40,y=200,x=110)
        
        b_F = t.Button(marco_val, text="F", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("F"))
        b_F.grid(row=4,column=3,padx=2)
        b_F.place_configure(height=40,y=200,x=165)
        
    e_Marco_og.config(state="readonly")
    return base

def Valores_DS(arg):
    global conv
    seleccion = d_marco_ds.get()
    
    if (seleccion == "Binario"):
        conv = 2
    elif (seleccion == "Ternario"):
        conv = 3
    elif (seleccion == "Cuaternario"):
        conv = 4
    elif (seleccion == "Quinario"):
        conv = 5
    elif (seleccion == "Senario"):
        conv = 6
    elif (seleccion == "Septenario"):
        conv = 7
    elif (seleccion == "Octal"):
        conv = 8
    elif (seleccion == "Nonario"):
        conv = 9
    elif (seleccion == "Decimal"):
        conv = 10
    elif (seleccion == "Undecimal"):
        conv = 11
    elif (seleccion == "Duodecimal"):
        conv = 12
    elif (seleccion == "Tridecimal"):
        conv = 13
    elif (seleccion == "Cuadridecimal"):
        conv = 14
    elif (seleccion == "Quindecial"):
        conv = 15
    elif (seleccion == "Hexadecimal"):
        conv = 16
#============================================================0

#Label Frames
marco = t.LabelFrame(root, text="Configuración",borderwidth=1,bg="white",relief="solid",font=("Arial", 14))
marco.place_configure(x=10,y=10,width=480)
#========================================

#DropDown
opciones_og = [
    "Base 2",
    "Base 3",
    "Base 4",
    "Base 5",
    "Base 6",
    "Base 7",
    "Base 8",
    "Base 9",
    "Base 10",
    "Base 11",
    "Base 12",
    "Base 13",
    "Base 14",
    "Base 15",
    "Base 16"
]
opciones_ds = [
    "Binario",
    "Ternario",
    "Cuaternario",
    "Quinario",
    "Senario",
    "Septenario",
    "Octal",
    "Nonario",
    "Decimal",
    "Undecimal",
    "Duodecimal",
    "Tridecimal",
    "Cuadridecimal",
    "Quindecial",
    "Hexadecimal"
]


#Texto
text_vacio = ttk.Label(marco, text="")
text_vacio.grid(row= 0, column=0,padx= 0, pady= 2,sticky="W")

text_base = ttk.Label(marco, text="Base origen")
text_base.grid(row= 1, column=0,padx= 10, pady= 2,sticky="W")

text_ds = ttk.Label(marco, text="Base destino")
text_ds.grid(row= 1, column=2,padx= 35, pady= 2,sticky="W")
text_ds.place_configure(x=265,y=26)

#
d_marco_og = ttk.Combobox(marco,values=opciones_og,state="readonly")
d_marco_og.place_configure(x=88,y=25,width=100)
d_marco_og.set("Base 2")


d_marco_ds = ttk.Combobox(marco,values=opciones_ds,state="readonly")
d_marco_ds.place_configure(x=344,y=25,width=100)
d_marco_ds.set("Decimal")

d_marco_og.bind("<<ComboboxSelected>>", Valores_OG)

d_marco_ds.bind("<<ComboboxSelected>>", Valores_DS)
#Entradas
e_Marco_og = ttk.Entry(marco,width=30,state="readonly")
e_Marco_og.grid(row= 3, column=0,padx= 10, pady= 10,sticky="E")

e_Marco_ds = ttk.Entry(marco,state="readonly",width=30)
e_Marco_ds.grid(row= 3, column=2,padx= 40, pady= 10,sticky="E")
e_Marco_ds.place_configure(x=267,y=56)

#estilos
estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure('TButton', foreground="white", background="#33A2FF", borderwidth=0)
estilos.configure("TLabel", background="white")
estilos.configure("TCombobox", fieldbackground="white", background="white", foreground="black")
estilos.configure("TScrollbar", background="lightgray", troughcolor="white")
#Botones


b_convertir = ttk.Button(marco, text="Convertir", command=boton_convertir,width=15) #
b_convertir.grid(row= 4, column=0,padx= 10, pady= 10,sticky="W")

#=========================================================================================================

marco_val = t.LabelFrame(root, text="Valores",padx=10,pady=10,bg="white",borderwidth=1,relief="solid",font=("Arial", 14))
marco_val.place_configure(x=10,y=180,height=280,width=233)

#Botones
b_CE = t.Button(marco_val, text="CE", width=6,height=1,background="#33A2FF",border=False,fg="white",command=boton_borrar_todo)
b_CE.grid(row=0,column=0,padx=2)
b_CE.place_configure(height=40)

b_M = t.Button(marco_val, text="M", width=6,height=1,background="#33A2FF",border=False,fg="white",command=Memoria_boton)
b_M.grid(row=0,column=1,padx=2)
b_M.place_configure(height=40,x=55)

b_borrar = t.Button(marco_val, text="Borrar", width=13,height=1,background="#33A2FF",border=False,fg="white", command=boton_borrar)
b_borrar.grid(row=0,column=2,padx=2)
b_borrar.place(x=109,width=105,height=40)

b_cero = t.Button(marco_val, text="0", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("0"))
b_cero.grid(row=1,column=0,padx=2,pady=15)
b_cero.place_configure(height=40,y=50)
        
b_uno = t.Button(marco_val, text="1", width=6,height=1,background="#33A2FF",border=False,fg="white", command= lambda: boton_valor("1"))
b_uno.grid(row=1,column=1,padx=2,pady=15)
b_uno.place_configure(height=40,x=55,y=50)

#=========================================================================================================000
marco_memory = t.LabelFrame(root, text="Memoria",padx=10,pady=10,bg="white",borderwidth=1,relief="solid",font=("Arial", 14))
marco_memory.place_configure(x=250,y=180,height=280,width=240)

#Memoria
me_lista = t.Listbox(marco_memory,activestyle="none", selectbackground='#33A2FF',relief="solid")
me_lista.pack()
me_lista.place_configure(height=188,width=176,x=20,y=10)
me_lista.yview("moveto", 0.82)
ingresar_lista()

me_scroll = ttk.Scrollbar(marco_memory,orient=t.VERTICAL, command=me_lista.yview)
me_scroll.pack()
me_scroll.place_configure(x=195,y=10,height=190)
me_scroll.set(0.2, 0.5)

me_lista.config(yscrollcommand=me_scroll.set)

me_res = t.Button(marco_memory,text="Restaurar",background="#33A2FF",border=False,fg="white",command=restaurar_boton)
me_res.pack()
me_res.place_configure(x=22,y=210,height=30,width=84)

me_Borrar = t.Button(marco_memory,text="Borrar",background="#33A2FF",border=False,fg="white",command=memory_borrar_boton)
me_Borrar.pack()
me_Borrar.place_configure(x=120,y=210,height=30,width=84)

root.mainloop()

print("Ventana cerrada")
