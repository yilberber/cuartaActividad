from data.data import * #se importaron los datos
from BD.baseDatos import *#se iportaron datos de base de datos
from sklearn.linear_model import LinearRegression #se importo la regresion lineal
from grafica.grafica import * #importscion de la grafica
import pandas as pd #importacion de pandas 

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico()

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos() #lista de los datos reales
data_real = pd.DataFrame(data_list)
data_real_fit = data_real
#se separan esfuerzo y deformacion en X y Y
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1)
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1)
#limites para X y Y basados en los ultimos datos reales
x_lim = data_real['Esfuerzo[kN]'].iloc[-1]
y_lim = data_real['Deformacion[mm]'].iloc[-1]
model = LinearRegression() #modelo de regresión lineal
model.fit(X, y) # se muestra el modelo
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1) # Se realiza una predicción utilizando el modelo para una carga de 3000 kN y se redondea a una décima
print('la predicción a 1000 kN es de: ', prediction ,'mm') # se muestra el modelo de predicción  


dataRealEsfuerzo = data_real['Esfuerzo[kN]']
dataRealDeformacion = data_real['Deformacion[mm]']

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion)
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)

