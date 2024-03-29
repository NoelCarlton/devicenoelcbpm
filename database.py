from sqlalchemy import create_engine, MetaData, Table

engine = create_engine("",convert_unicode=True)
metadata = MetaData(bind=engine)

drivers = Table('driver', metadata, autoload=True)
alarm = Table('alarm', metadata, autoload=True)
modules = Table('modules', metadata, autoload=True)
arguments = Table('arguments', metadata, autoload=True)
