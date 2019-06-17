from flask_script import Manager
from web import create_app
from web.setting import setting

app = create_app()
app.register_blueprint(setting,url_prefix='')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()