from flask_restful import Resource
from ..modelos import db,Cancion,CancionSchema
from flask import request

cancion_schema=CancionSchema()

class VistasCanciones(Resource):
    def get(self):#me trae todas las canciones
        return[cancion_schema.dump(Cancion)for Cancion in Cancion.query.all()]
    
    
    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'],\
                        minutos=request.json['minutos'],\
                        segundos=request.json['segundos'],\
                        interprete=request.json['interprete'])
        db.session.add(nueva_cancion)#agregar en la bd
        db.session.commit()#guardar los cambioa 
        return cancion_schema.dump(nueva_cancion)#retorna la nueva cancion en formato json 


class VistaCancion(Resource):
    
    
    def get(self, id_cancion):
        return cancion_schema.dump(Cancion.query.get_or_404(id_cancion))
    
    #consultar
    def put(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        cancion.titulo =  request.json.get('titulo',cancion.titulo)
        cancion.minutos = request.json.get('minutos',cancion.minutos)
        cancion.segundos = request.json.get('segundos',cancion.segundos)
        cancion.interprete = request.json.get('interprete',cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)     
    
    #eliminar
    def delete(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        db.session.delete(cancion)
        db.session.commit()
        return'operacion exitosa',204 
            
    
    