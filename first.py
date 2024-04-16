import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

df = pd.read_csv('Lstm.csv' , delimiter=';' , decimal=',') 

x = df.Volt 
y = df.Watt 

x1 = x[:-1] 
y1 = y[:-1] 

y2 = df.PUI 
y3 = y2[:-1]

y_av = (y1 + y3)/2 


t = np.linspace(0,240)
k , d   = np.polyfit(x1 ,y_av ,1 ) 
fit = k*x1 + d

title = r"$\varepsilon_0$"

plt.scatter(x1,y1 , color = 'g' ,marker = 'x' ,  label = 'P')
plt.scatter(x1 , y3, color = 'b' , marker = '*' , label = r"$P_{UI}$")
plt.plot(x1 , fit , color = 'orange' , label = 'linear fit ') 
plt.xlabel('x')
plt.ylabel(r"$\alpha$")
plt.title(title)
plt.show()