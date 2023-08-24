
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class cancion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(128))
    minutos =  db.Column(db.Integer)
    segundos =  db.Column(db.Integer)
    interprete =  db.Column(db.String(128))
    
    def __repr__(self):
        return"{}-{}-{}-{}".format(self.titulo,self.minutos,self.segundos,self.interprete)

    