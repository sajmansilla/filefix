#!/usr/bin/python3
# -*- coding: utf-8 -*-

import easygui as eg
import tkinter as tk
import control as ctrl

fields = [("Entrada", "Null"), ("Salida", "Null")]


class Vista():

    def __init__(self):

        controlador = ctrl.Control()

        self.root = tk.Tk()
        self.root.title("FileFix")
        # #Labels##
        self.rootLabel = tk.Label(
            self.root,
            text="Seleccione los archivos de entrada y salida",
            padx=0)
        # #Buttons##
        self.BtExit = tk.Button(
            self.root, text="Salir", command=self.root.quit)

        self.BtConvertir = tk.Button(
            self.root, text="Convertir", padx=30,
            command=lambda: controlador.main())

        self.BtEntrada = tk.Button(
            self.root, text="in",
            command=lambda: controlador.set_entrada(self))

        self.BtSalida = tk.Button(
            self.root, text="out",
            command=lambda: controlador.set_salida(self))

    def dir_open(self):
        directorio = eg.diropenbox(msg="Abrir directorio:",
                                   title="Control: diropenbox",
                                   default='')

        eg.msgbox(directorio, "diropenbox", ok_button="Continuar")
        return directorio

    def file_open(self):
        extension = ["*.py", "*.pyc"]
        archivo = eg.fileopenbox(msg="Abrir archivo",
                                 title="Control: fileopenbox",
                                 default='',
                                 filetypes=extension)
        print(archivo)
        return archivo

        eg.msgbox(archivo, "fileopenbox", ok_button="Continuar")
        return archivo

    def file_save(self):
        extension = ["*.py", "*.pyc"]
        archivo = eg.filesavebox(msg="Guardar archivo",
                                 title="Control: filesavebox",
                                 default='',
                                 filetypes=extension)

        eg.msgbox(archivo, "filesavebox", ok_button="Continuar")
        return archivo

    def grid(self):
        self.rootLabel.pack()
        self.fckPackFields()
        self.BtConvertir.pack(side="right")
        self.BtExit.pack(side="left")
        # ##self.BtNewWindow.pack(side="right")

    def fckPackFields(self):
        if fields:
            for field in fields:
                # #create labels##
                row = tk.Frame(self.root)
                nameLabel = tk.Label(row, text=field[0]) # , anchor="center")
                valueLabel = tk.Label(row, text=field[1])
                # #pack labels##
                row.pack(side="top", padx = 5, pady = 5, fill = "x") # , fill="x", padx=5, pady=5)
                nameLabel.pack(side="left", expand=True, fill="x")
                self.BtEntrada.pack(side="left", expand=True, fill="x")
                valueLabel.pack(side="left", expand=True, fill="x")
                self.BtSalida.pack(side="left", expand=True, fill="x")

    def run(self):
        self.grid()
        self.root.mainloop()
        self.root.destroy()