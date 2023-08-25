from flaskr import create_app
from .modelos import  db, Cancion , Album , Usuario ,Medio

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#prueba
with app.app_context():
    a = Album(titulo='chuchis', anio=2028, descripcion='chuchis',medio=Medio.CD)
    u = Usuario(nombre_usuario='juanito',contrasena='asdaf')
    c =Cancion(titulo='mi cancion',minutos=1 , segundos=15 , interprete='lolo')
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Usuario.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())
    


