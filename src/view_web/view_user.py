from flask import Blueprint,render_template, request, redirect, url_for

Blueprint= Blueprint("vista_usuarios", __name__, "templates")

import sys
sys.path.append("src")

import src.controller.ControladorUsuarios as ControladorUsuarios
from src.model import Usuario


@Blueprint.route("/")
def Home():
   return render_template("index.html")

@Blueprint.route("/serch_user")
def insert_user():
   # request.args es un diccionario que contiene los parametros en le URL solicitada
   return render_template("serch_user.html")

@Blueprint.route("/searched_user")
def searched_user():
   cedula = request.args["cedula"]
   usuario = ControladorUsuarios.BuscarPorCedula(cedula)
   return render_template("searched_user.html", Usuario = usuario)

@Blueprint.route("/delete_user")
def delete_user():
    return render_template("delete_user.html")

@Blueprint.route("/user_deleted")
def user_deleted():
    cedula = request.args.get("cedula")
    usuario = ControladorUsuarios.delete_user(cedula)

    return render_template("user_deleted.html", Usuario=usuario)


@Blueprint.route("/update_user")
def update_user():
    return render_template("update_user.html")

@Blueprint.route("/updated_user")
def updated_user():
    nombre = request.args.get("nombre")
    cedula = request.args.get("cedula")
    campo = request.args.get("campo")
    nuevo_valor = request.args.get("nuevo_valor")
    usuario = ControladorUsuarios.update_user(cedula, campo, nuevo_valor)
    return render_template("updated_user.html", Usuario=usuario)

@Blueprint.route("/crear-usuario")
def create_user():
   return render_template("create_user.html")


@Blueprint.route("/crear-usuario", methods=["GET"])
def crear_usuario():
   cedula = request.args.get("cedula")
   nombre = request.args.get("nombre")
   telefono = request.args.get("telefono")
   correo = request.args.get("correo")
   tipo_evento = request.args.get("tipo_evento")
   texto_original = request.args.get("texto_original")
   texto_procesado = request.args.get("texto_procesado", "")  # Default to empty string if not provided

   usuario_prueba = Usuario(
      cedula=cedula,
      nombre=nombre,
      telefono=telefono,
      correo=correo,
      TipoEvento=tipo_evento,
      TextoOriginal=texto_original,
      TextoProcesado=texto_procesado
   )

   ControladorUsuarios.insert_user(usuario_prueba)
   return redirect(url_for('vista_usuarios.user_created'))

@Blueprint.route("/user_created")
def user_created():
    return render_template("user_created.html")

@Blueprint.route('/update_user')
def update_user_page():
    return render_template("update_user.html")