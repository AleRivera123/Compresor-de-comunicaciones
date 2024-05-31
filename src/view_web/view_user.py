from flask import Blueprint, render_template, request, redirect, url_for, flash

Blueprint = Blueprint("vista_usuarios", __name__, "templates")

import sys

sys.path.append("src")

import src.controller.ControladorUsuarios as ControladorUsuarios
from src.controller.ControladorUsuarios import UserData
from src.model.Usuario import *
from src.compressor.compressorlogic import CompresorRLE


class UserInput:
    def __init__(self, nombre, cedula, telefono, correo, texto_original, tipo_evento):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
        self.texto_original = texto_original
        self.tipo_evento = tipo_evento

    def validate(self):
        if not all([self.nombre, self.cedula, self.correo, self.telefono, self.texto_original, self.tipo_evento]):
            return "Todos los campos son requeridos."

        if self.tipo_evento not in ['comprimir', 'descomprimir']:
            return "Tipo de evento inválido. Debe ser 'comprimir' o 'descomprimir'."

        self.validate_email(self.correo)

    @staticmethod
    def validate_email(email):
        import re
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Correo electrónico inválido."


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
    try:
        usuario = UserData.query_user(cedula)
        return render_template("searched_user.html", user=usuario)
    except DataValidationError as e:
        return render_template("searched_user.html", user=None)



@Blueprint.route("/delete_user")
def delete_user():
    return render_template("delete_user.html")

@Blueprint.route("/user_deleted")
def user_deleted():
    cedula = request.args["cedula"]
    try:
        UserData.delete_user(cedula)
        usuario = UserData.query_user(cedula)
        return render_template("user_deleted.html", Usuario=usuario)
    except DataValidationError as e:
        flash("Error al eliminar el usuario: " + str(e))
        return redirect(url_for("vista_usuarios.delete_user"))





@Blueprint.route("/update_user")
def update_user():
    return render_template("update_user.html")

@Blueprint.route("/updated-user", methods=["POST", "GET"])
def updated_user():
    if request.method == "GET":
        cedula = request.args.get("cedula")
        if cedula and cedula.isdigit():
            try:
                usuario = UserData.query_user(int(cedula))
                return render_template("updated_user.html", Usuario=usuario)
            except DataValidationError as e:
                flash(str(e))
                return redirect(url_for("vista_usuarios.update_user"))
        else:
            flash("Por favor, proporcione una cédula válida.")
            return redirect(url_for("vista_usuarios.update_user"))
    elif request.method == "POST":
        cedula = request.form.get("cedula")
        campo = request.form.get("campo")
        nuevo_valor = request.form.get("nuevo_valor")

        if not cedula or not cedula.isdigit():
            flash("Por favor, proporcione una cédula válida.")
            return redirect(url_for("vista_usuarios.update_user"))

        try:
            if campo not in ['telefono', 'nombre', 'correo']:
                flash("Campo de actualización inválido.")
                return redirect(url_for("vista_usuarios.update_user"))

            UserData.update_user(int(cedula), campo, nuevo_valor)
            flash("Usuario actualizado correctamente.")
            return redirect(url_for("vista_usuarios.update_user"))

        except DataValidationError as e:
            flash(str(e))
            return redirect(url_for("vista_usuarios.update_user"))

@Blueprint.route("/crear-usuario")
def create_user():
    return render_template("create_user.html")

@Blueprint.route("/new_user", methods=["POST"])
def new_user():
    cedula = request.form["cedula"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    correo = request.form["correo"]
    texto_original = request.form["texto_original"]
    tipo_evento = request.form["tipo_evento"]

    # Mensaje de depuración para ver los datos recibidos
    print(
        f"Datos recibidos: Cedula={cedula}, Nombre={nombre}, Telefono={telefono}, Correo={correo}, Texto Original={texto_original}, Tipo de Evento={tipo_evento}")

    usario_prueba = UserInput(nombre=nombre, cedula=cedula, telefono=telefono,
                              correo=correo, texto_original=texto_original, tipo_evento=tipo_evento)

    validacion = usario_prueba.validate()

    # Mensaje de depuración para ver si la validación fue exitosa
    if not validacion:
        print("Validación fallida")
        return render_template("create_user.html", error="Validation failed. Please check your inputs.")
    else:
        print("Validación exitosa")
        compresorRLE = CompresorRLE()
        texto_procesado = compresorRLE.comprimir(usario_prueba.texto_original)
        UserData.insert_user(
            usario_prueba.cedula, usario_prueba.nombre, usario_prueba.telefono,
            usario_prueba.correo, usario_prueba.tipo_evento, usario_prueba.texto_original,
            texto_procesado=texto_procesado
        )
        return render_template("user_created.html", Usuario=usario_prueba)
