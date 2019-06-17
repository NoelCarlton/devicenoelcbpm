from web import db

class Driver(db.Model):
    __tablename__ = 'driver'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140),nullable=False)
    telephone = db.Column(db.String(12), unique=True, nullable=False)
    age = db.Column(db.Integer, default=0, nullable=False)
    avatar = db.relationship('Avatars', backref='driver')

    def __repr__(self):
        return '<Driver {}>'.format(self)

    def __init__(self, name=None, telephone=None, age  = 0):
        self.name = name
        self.telephone = telephone
        self.age = age


class Alarm(db.Model):
    __tablename__ = 'alarm'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    driver = db.Column(db.String(12), nullable = False)
    type = db.Column(db.String(8), nullable = False)
    trainSeries = db.Column(db.String(7), nullable = False)
    deviceCode = db.Column(db.String(10), nullable = False)
    createTime = db.Column(db.DateTime, nullable = False)
    path = db.Column(db.String(20), nullable = False)
    isUpload = db.Column(db.Integer, nullable= False, default = 0)
    model = db.Column(db.String(20), nullable = False)

    def __repr__(self):
        return '< Alarm {}>'.format(self)

class Device(db.Model):
    __tablename__ = 'arguments'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    resolution = db.Column(db.Integer, nullable = False)
    codeRate = db.Column(db.Integer, nullable = False)
    bitRate = db.Column(db.Integer, nullable = False)
    quality = db.Column(db.String(10), nullable = False)
    frame = db.Column(db.Integer, nullable = False)
    ip = db.Column(db.String(15), nullable = False)
    gataway = db.Column(db.String(15), nullable= False, default = 0)
    port = db.Column(db.Integer, nullable = False)

    def __init__(self, resolution=None, codeRate=None, bitRate=None, quality=None, frame=None, ip=None, gataway=None, port=None):
        self.resolution=resolution
        self.codeRate = codeRate
        self.bitRate =bitRate
        self.quality = quality
        self.frame = frame
        self.ip = ip
        self.gataway = gataway
        self.port = port

class Avatars(db.Model):
    __tablename__: 'avatars'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    type = db.Column(db.Integer, nullable=False, default = 0)
    telephone = db.Column(db.String(12), db.ForeignKey('driver.telephone'),nullable=False)
    avatar = db.Column(db.String(50), nullable = False)
    character = db.Column(db.Text(200), nullable=False)

    def __init__(self,telephone,avatar,type):
        self.telephone=telephone
        self.avatar = avatar,
        self.type = type