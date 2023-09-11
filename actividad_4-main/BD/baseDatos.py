from pymongo.mongo_client import MongoClient

#CONEXIÓN
def conexion():
    uri = "mongodb+srv://yilber:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    return MongoClient(uri)

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos():
    client = conexion()  #Establece una conexión con la base de datos MongoDB
    db = client.actividad4.data_real #Accede a una colección específica dentro de la base de datos
    data_list = []
    for data_real_bd in db.find(): #Recorre todos los documentos en la colección
        data_list.append(data_real_bd) #Agrega cada documento encontrado a la lista
    return data_list #devuelve la lsta con los datos obtenidos de la base de datos

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""
