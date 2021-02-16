import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os


def report():
    filename="data.csv"
    nombreColumnas = ["Porcentaje","Tiempo"]
    dataFrame = pd.read_csv(filename,names=nombreColumnas, delimiter=",",header=0)
    dataFrameClean = dataFrame.drop([95,96,97,98,99])
    
    dataFrameClean.head()
    fig = plt.figure(figsize=(14,14))
    plt.scatter(dataFrameClean['Porcentaje'],dataFrameClean['Tiempo'])
    plt.plot(dataFrameClean['Porcentaje'],dataFrameClean['Tiempo'])
    plt.xlabel('Porcentajes Obtenidos')
    plt.ylabel('Tiempo Calculado')
    plt.grid()

    porcenO = dataFrameClean['Porcentaje'].values.reshape(-1,1)
    tiempoO = dataFrameClean['Tiempo'].values.reshape(-1,1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(porcenO, tiempoO)
    Hours_pred = linear_regressor.predict(porcenO)

    print("report")
    print(Hours_pred)
    
def runAB(n):
    consulta = ""
    url = urlTexField.get()
    canti = cantPetiTexField.get()
    concu = cantConcuTexField.get()

    if url == "":
        url = "uis.edu.co"
        canti = 10
        concu = 10

    if n == 0:

        messagebox.showerror(message="SELECCIONE EL TIPO DE CONSULTA", title="ERROR!!!")

    if n == 1 :
        consulta = "ab -n "+str(canti)+" -e data.csv https://www."+url+"/"
        print(consulta)

    if n == 2:
        consulta = "ab -n "+str(canti)+" -c "+str(concu)+" -e data.csv https://www."+url+"/"
        print(consulta)

    
    res = os.popen(consulta).read()
    txtRes.delete("0.0", tk.END)
    txtRes.insert(1.0, str(res))
    report()

def runFunt():
    runAB(combo.current())


root = Tk()
root.geometry("900x800+100+100")
root.title("APATCSC")

main = Frame(root)
main.pack(fill=BOTH, expand=1)

canv = Canvas(main)
canv.pack(side=LEFT, fill=BOTH, expand=1)

scrbar= ttk.Scrollbar(main,orient=VERTICAL, command=canv.yview)
scrbar.pack(side=RIGHT, fill=Y)

canv.configure(yscrollcommand=scrbar.set)
canv.bind('<Configure>',lambda e: canv.configure(scrollregion=canv.bbox("all")))

secFrame = Frame(canv)

canv.create_window((0,0),window=secFrame, anchor = "nw")



# button close
btnClose = Button(root, text="QUIT", fg="red", command=root.destroy)
btnClose.place(x=740, y=0)


# titles
Label(root, text="APLICATIVO PYTHON PARA ANALISIS DE TIEMPOS DE CARGA").place(
    x=200, y=10)
Label(root, text="EN SEGUNDO PLANO SECUENCIALES O CONCURRENTES").place(x=210, y=30)

# url Textfield
Label(root, text="INTRODUSCA LOS DATOS DE LA CONSULTA").place(x=0, y=80)
Label(root, text="URL: ").place(x=0, y=100)

urlTexField = Entry(root, width=20, text="")
urlTexField.place(x=40, y=100)
urlTexField.insert(END, "")

#cantida Textfield
Label(root, text="# PETICIONES: ").place(x=210, y=100)
cantPetiTexField = Entry(root, width=5, text="")
cantPetiTexField.place(x=315, y=100)
cantPetiTexField.insert(END, "")

#cantida concurrentes Textfield
Label(root, text="# CONCURRENTES: ").place(x=365, y=100)
cantConcuTexField = Entry(root, width=5, text="")
cantConcuTexField.place(x=500, y=100)
cantConcuTexField.insert(END, "")
# combbox
Label(root, text="TIPO: ").place(x=550, y=100)
combo = ttk.Combobox(root,
                            values=[
                                "Seleccionar",
                                "SECUENCIAL",
                                "CONCURRENTE"], width=13)

combo.place(x=595, y=100)
combo.current(0)
# button run
btnRun = Button(root, command=runFunt, text="Analizar")
btnRun.place(x=718, y=96)

#textscroll Reporte
Label(root, text="RESULTADOS ").place(x=20, y=150)
txtRes = scrolledtext.ScrolledText(root, width=70, height=10)
txtRes.place(x=20, y=180)

Label(root, text="ANALISIS ").place(x=20, y=360)
txtAn = scrolledtext.ScrolledText(root, width=70, height=10)
txtAn.place(x=20, y=385)

root.mainloop()
