#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *

class View(Toplevel):
    def __init__(self, root):
        Toplevel.__init__(self, root)
        self.protocol("WM_DELETE_WINDOW", root.destroy)  # Protocolo a usar al pulsar en la X de cierre
        self.title('Filefix')  # Nombramos la ventana

        row1 = Frame(self)     #creamos un Frame dentro de la ventana creada
        row2 = Frame(self)     #creamos otro Frame dentro de la ventana creada
        botonera = Frame(self)  # creo la row de los botones

        self.lEntrada = Label(row1, text="Entrada")#Ponemos una línea de texto
        self.lIn = Label(row1, text="Ningun archivo seleccionado")#Ponemos una línea de texto
        self.bEntrada = Button(row1, text="...")

        self.lSalida = Label(row2, text="Salida")#Ponemos una línea de texto
        self.lOut = Label(row2, text="Ningun archivo seleccionado")#Ponemos una línea de texto
        self.bSalida = Button(row2, text="...")

        self.bConvert = Button(botonera, text="Convertir")

        row1.pack(side="top", fill="x", padx=5, pady=5)            #Lo situamos en la ventana
        self.lEntrada.pack(side="left", fill="x", padx=5, pady=5)
        self.lIn.pack(side="left", fill="x", padx=5, pady=5)
        self.bEntrada.pack(side="right", fill="x", padx=5, pady=5)

        row2.pack(side="top", fill="x", padx=5, pady=5)            #Lo situamos en la ventana
        self.lSalida.pack(side="left", fill="x", padx=5, pady=5)
        self.lOut.pack(side="left", fill="x", padx=5, pady=5)
        self.bSalida.pack(side="right", fill="x", padx=5, pady=5)

        botonera.pack(side="top")
        self.bConvert.pack(side="bottom")
