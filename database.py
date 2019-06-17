from sqlalchemy import create_engine, MetaData, Table

engine = create_engine("mysql://device:'ZC2019@bi.cbpm'@192.168.31.63:3306/train",convert_unicode=True)
metadata = MetaData(bind=engine)

drivers = Table('driver', metadata, autoload=True)
alarm = Table('alarm', metadata, autoload=True)
modules = Table('modules', metadata, autoload=True)
arguments = Table('arguments', metadata, autoload=True)