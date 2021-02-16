import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import scrolledtext
import tkinter as tk


filename = "data.csv"
nombreColumnas = ["Porcentaje", "Tiempo"]
dataFrame = pd.read_csv(filename, names=nombreColumnas,
                        delimiter=",", header=0)
processDf = dataFrame.drop([95, 96, 97, 98, 99])

# processDf.head()


fig = plt.figure(figsize=(14, 14))
plt.scatter(processDf['Porcentaje'], processDf['Tiempo'])
plt.plot(processDf['Porcentaje'], processDf['Tiempo'])
plt.xlabel('Number of Images')
plt.ylabel('Computational Hours')
plt.grid()
# processDf.keys()

nImages = processDf['Porcentaje'].values.reshape(-1, 1)
Hours = processDf['Tiempo'].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(nImages, Hours)
Hours_pred = linear_regressor.predict(nImages)

m = linear_regressor.coef_[0][0]
c = linear_regressor.intercept_[0]
label = r'$Hours = %0.4f*nImages %+0.4f$' % (m, c)
print(label)

Hours = 0.0115*nImages -0.4891

fig = plt.figure(figsize=(4, 4))
# plt.scatter(processDf['Porcentaje'],processDf['Tiempo'])
plt.plot(processDf['Porcentaje'], processDf['Tiempo'], label='Measured Hours')
plt.plot(nImages, Hours_pred, color='red', label=label)
plt.xlabel('Number of Images')
plt.ylabel('Computational Hours')
plt.legend()
plt.grid()




root = Tk()
root.geometry("760x440+100+100")

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()
plot_widget.place(x=350, y=100)
mainloop()

