from flaskr import create_app
from .modelos import db, Cancion,Album, Usuario,Medio
from .modelos import AlbumSchema

app = create_app('dfault')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    album_schema= AlbumSchema()
    A=Album(titulo="Album1", anio=2020, descripcion="Album de prueba",  medio=Medio.DISCO)
    B=Album(titulo="Pies Descalzos", anio=1998, descripcion="Album de Shakira",  medio=Medio.CD)
    db.session.add(A)
    db.session.add(B)
    db.session.commit()
    print([album_schema.dump(album) for album in Album.query.all()])