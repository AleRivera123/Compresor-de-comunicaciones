from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# Importa la clase CompresorRLE de tu módulo de compresión
import sys
sys.path.append("src")  # Añade el directorio 'src' a los directorios donde Python busca módulos
import src.compressor.compressorlogic as compresorlogic  # Importa el módulo con la lógica de compresión
from src.compressor.compressorlogic import *  # Importa todas las clases y funciones del módulo de lógica del compresor

class MiAplicacion(App):
    def build(self):
        Window.clearcolor = (0.06, 0.1, 0.12, 1)  # Establece el color de fondo de la ventana

        # Layout principal con orientación vertical
        layout = BoxLayout(orientation='vertical', padding=[10, 20], spacing=10)

        # Título de la aplicación
        titulo = Label(text='Compresor de Comunicaciones', font_size='40sp', color=(0.2, 0.45, 0.8, 1), size_hint=(1, None), height=60)

        # Descripción de la aplicación
        descripcion = Label(text=('El Compresor de Comunicaciones es una herramienta diseñada para optimizar la '
                                  'transmisión de datos al reducir el tamaño de los archivos sin comprometer la '
                                  'integridad de la información.'),
                            font_size='16sp', color=(0.7, 0.7, 0.7, 1), size_hint=(1, None), halign='left', valign='middle')
        descripcion.bind(size=descripcion.setter('text_size'))  # Ajusta el tamaño del texto al tamaño del widget

        layout.add_widget(titulo)  # Añade el título al layout
        layout.add_widget(descripcion)  # Añade la descripción al layout

        # Input para texto a comprimir/descomprimir
        self.entrada = TextInput(hint_text='Escribe algo aquí o introduce el texto comprimido', font_size=25, size_hint=(2, 0.6), background_color=(0.12, 0.14, 0.17, 1), foreground_color=(0.8, 0.8, 0.8, 1))
        layout.add_widget(self.entrada)

        # Layout para botones con acción de compresión y descompresión
        layout_botones = BoxLayout(size_hint=(1, 0.15), spacing=10)
        boton1 = Button(text='Comprimir', background_normal='', background_color=(0.2, 0.45, 0.8, 1), color=(1, 1, 1, 1))
        boton2 = Button(text='Descomprimir', background_normal='', background_color=(0.2, 0.45, 0.8, 1), color=(1, 1, 1, 1))
        boton1.bind(on_press=self.comprimir)  # Vincula el botón a la función comprimir
        boton2.bind(on_press=self.descomprimir)  # Vincula el botón a la función descomprimir
        layout_botones.add_widget(boton1)
        layout_botones.add_widget(boton2)
        layout.add_widget(layout_botones)

        # Input para mostrar resultados de la compresión/descompresión
        self.resultado = TextInput(text='Aquí se mostrará el resultado...', font_size=25)
        layout.add_widget(self.resultado)

        # Inicializa la clase de compresión
        self.compresor = compresorlogic.CompresorRLE()

        return layout  # Devuelve el layout principal de la aplicación

    def comprimir(self, instance):
        # Método para comprimir texto
        result = self.compresor.comprimir(self.entrada.text)
        self.resultado.text = result

    def descomprimir(self, instance):
        # Método para descomprimir texto
        result = self.compresor.descomprimir(self.entrada.text)
        self.resultado.text =  result

if __name__ == '__main__':
    MiAplicacion().run()  # Ejecuta la aplicación
