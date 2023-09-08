from flask_restful import Resource
from ..modelos import db, Cancion,CancionSchema
from flask import request
from flask_jwt_extended import jwt_required,create_access_token
from datetime import datetime
from ..tareas import registrar_log


cancion_schema= CancionSchema()


class VistaSignIn(Resource):
    def post(self):
        '''usuario=request.json['usuario']
        contrasena=request.json['contrasena']
        usuario_encontrado=Cancion.query.filter_by(usuario=usuario).first()'''
        usuario=request.json['usuario']

        if usuario != 'Orlando':
            return {'mensaje': 'Usuario no encontrado'}, 404
        if usuario == 'Orlando':
            registrar_log.delay(usuario,datetime.utcnow())
            token_de_acceso=create_access_token(identity=request.json['usuario'])
            return {'token': token_de_acceso}, 200


class VistaCanciones(Resource):
    @jwt_required()
    def get(self):
        return [cancion_schema.dump(cancion) for cancion in Cancion.query.all()]
    
    @jwt_required()
    def post(self):
        nueva_cancion=Cancion(titulo=request.json['titulo'], minutos=request.json['minutos'], 
                              segundos=request.json['segundos'], interprete=request.json['interprete'])
        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)


class VistaCancion(Resource):
    @jwt_required()
    def get(self, id):
        return cancion_schema.dump(Cancion.query.get_or_404(id))
    
    @jwt_required()
    def put(self, id):
        cancion=Cancion.query.get_or_404(id)
        cancion.titulo=request.json.get('titulo', cancion.titulo)
        cancion.minutos=request.json.get('minutos', cancion.minutos)
        cancion.segundos=request.json.get('segundos', cancion.segundos)
        cancion.interprete=request.json.get('interprete', cancion.interprete)
        db.session.commit()
        return cancion_schema.dump(cancion)
    
    @jwt_required()
    def delete(self, id):
        cancion=Cancion.query.get_or_404(id)
        db.session.delete(cancion)
        db.session.commit()
        return 'Operación Exitosa', 204
