# /usr/bin/env  python     # Linea de inicializacion
# -*- coding: UTF-8 -*-

# Modulos que se importan
from tkinter import *
from control import Control


# Documentacion del script
__author__ = 'Sebastian Mansilla'
""" Llamada main """

# Declaracion de variables Globales


# Declaracion de Funciones

if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    app = Control(root)
    root.mainloop()         #Cerramos la edicion de la ventana y esperamos a eventos