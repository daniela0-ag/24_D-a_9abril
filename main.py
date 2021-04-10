import openpyxl
#importar docuemnto xls. 
from openpyxl import load_workbook
t=load_workbook("Matrices1.xlsx")
r=t.active
#crear las celdas en lista y muestra su valor.
A1=(int(r["A1"].value),int(r["B1"].value),int(r["C2"].value))
B1=(int(r["B2"].value),int(r["A2"].value),int(r["D2"].value))
celdas=[A1,B1]
for valor in celdas:
  print(valor)
# creo una matriz con las filas anteriores y muestro su dimencion ,en este caso es una matriz 2*3.
import numpy as np
w=np.array([A1,B1])
print(w)
print(w.shape)
#creo otra matriz con las celdas del excel, matriz 3*2, muesta su dimención. 
c1=np.matrix([A1,B1])
A2=(int(r["A2"].value),int(r["D1"].value))
A3=(int(r["A2"].value),int(r["C2"].value))
A4=(int(r["A1"].value),int(r["B2"].value))
celdas1=[A2,A3,A4]
for valor in celdas1:
  print(valor)
e=np.array([A2,A3,A4])
print(e)
print(e.shape)
#multiplico las doas matrices anteriores queda una matriz 2*2. 
c=np.matrix([A2,A3,A4])
rt=print((c1*c),"matriz e*w")
#creo otra matriz para sumarla con la matriz e.
matriz2= np.array([[3,4],[5,6],[4,7]])
#sumo las matrices e+matriz2.
print(matriz2+e,"matriz matriz2+e")
#multiplico la mariz w por un escalar.
print(4*w,"matriz 4*w")
t.close()
t.save("resultado1.xlsx")