from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class CLIENT(db.Model):

    PRENOM_CLIENT = db.Column(db.String(30),  nullable=False)
    
    NOM_CLIENT= db.Column(db.String(30),  nullable=False)
    ADRESSE_MAIL =  db.Column(db.String(250),  nullable=False, unique=True, primary_key=True)
    PASSWD = db.Column(db.String(100),  nullable=False)
    donnees = db.relationship('CONCERNE', backref='user', lazy='dynamic')

    

    def __init__(self, email, firstname , lastname, passwd):
        self.PRENOM_CLIENT     = firstname
        self.NOM_CLIENT    = lastname
        self.ADRESSE_MAIL = email
        self.set_passwd(passwd)
    
    def set_passwd(self, password):
        self.PASSWD = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.PASSWD, password)
    
    def __repr__(self):
        return '<User %r>' % (self.PRENOM_CLIENT)

class DAATE(db.Model):
    DAATE = db.Column(db.DATE(), nullable=False, primary_key = True, unique=False)
    donnees = db.relationship('CONCERNE', backref='date', lazy='dynamic')
    def __init__(self, date):
        self.DAATE = date

    def __repr__(self):
        return '<DATE %d>' %(self.DAATE)


class CONCERNE(db.Model):
    # __tablename__ = 'CONCERNE'
    LONGITUDE = db.Column(db.Integer, nullable = False)
    LATITUDE= db.Column(db.Integer, nullable=False)
    ALTIUDE= db.Column(db.Integer, nullable=False)
    MODULE_ACCEL= db.Column(db.Integer, nullable = False)
    ADRESSE_MAIL =  db.Column(db.String,  db.ForeignKey('CLIENT.ADRESSE_MAIL'), primary_key=True)
    DAATE = db.Column(db.DATE(), db.ForeignKey('DAATE.DAATE'), primary_key=True)
    
    
    def __init__(self, email, date, long, lat, alt, mod):
        self.ADRESSE_MAIL = email
        self.DAATE = date
        self.LONGITUDE = long
        self.LATITUDE = lat
        self.ALTIUDE = alt
        self.MODULE_ACCEL = mod

    def __repr__(self):
        return '<DATA : %d>' % (self.MODULE_ACCEL)

