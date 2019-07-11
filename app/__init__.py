from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from app import views #va después porque app tiene que estar creado ya porque views utiliza la app

app.config.from_object('config')
