from flaskr import create_app
from .modelos import db, Cancion,Album, Usuario,Medio
from .modelos import AlbumSchema,UsuarioSchema, CancionSchema
from .vistas import VistaCanciones, VistaCancion, VistaSignIn
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = create_app('dfault')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/canciones/<int:id>')
api.add_resource(VistaSignIn, '/signin')
jwt = JWTManager(app)   

with app.app_context():
    album_schema= AlbumSchema()
    A=Album(titulo="Album1", anio=2020, descripcion="Album de prueba",  medio=Medio.DISCO)
    B=Album(titulo="Pies Descalzos", anio=1998, descripcion="Album de Shakira",  medio=Medio.CD)
    db.session.add(A)
    db.session.add(B)
    db.session.commit()
    #print([album_schema.dump(album) for album in Album.query.all()])

    u=Usuario(nombre_usuario="usuario1", contrasena="1234")
    usuario_schema= UsuarioSchema()
    u.albumes.append(A)
    u.albumes.append(B)
    db.session.add(u)
    db.session.commit()
    #print([usuario_schema.dump(usuario) for usuario in Usuario.query.all()])

    c1=Cancion(titulo="Donde están los ladrones", minutos=3, segundos=30)
    c2=Cancion(titulo="Ciega, sordomuda", minutos=3, segundos=30)
    c3=Cancion(titulo="Inevitable", minutos=3, segundos=30)
    cancion_chema= CancionSchema()
    A.canciones.append(c1)
    A.canciones.append(c2)
    B.canciones.append(c3)
    db.session.commit()
    #print([album_schema.dump(album) for album in Album.query.all()])
    print([usuario_schema.dump(usuario) for usuario in Usuario.query.all()])
    print([cancion_chema.dump(cancion) for cancion in Cancion.query.all()])
