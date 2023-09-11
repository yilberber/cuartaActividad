import pandas as pd # importar pandas

# Importar datos del csv
data_teorico = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documentos\1.YILBER\UNIVERSIDAD DISTRITAL\INGENIERIA CIVIL\PROGRAMACIÓN II\actividad_4-main\actividad_4-main\data\Data ingeniero.csv")

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico(): #obtener datos relacionados al esfuerzo
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]'] #extae la columna esfuerzo
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]'] #extrae la columna deformacion
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion #devuelve los datos


