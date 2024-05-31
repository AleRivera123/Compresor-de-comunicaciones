from flask import Flask, request, jsonify , url_for

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
from flask import render_template
import sys
sys.path.append("src")

from src.view_web import view_user

# Flask constructor: crea una variable que nos servirá para comunicarle a Flask
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)
app.register_blueprint(view_user.Blueprint)

# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run( debug=True )