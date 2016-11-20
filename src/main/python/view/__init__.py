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

        # self.BtEntrada = tk.Button(
        #     self.row, text="in",
        #     command=lambda: controlador.set_entrada(self))
        #
        # self.BtSalida = tk.Button(
        #     self.row, text="out",
        #     command=lambda: controlador.set_salida(self))

    def dir_open(self):
        directorio = eg.diropenbox(msg="Abrir directorio:",
                                   title="Control: diropenbox",
                                   default='')

        return directorio

    def file_open(self):
        extension = ["*.py", "*.pyc"]
        archivo = eg.fileopenbox(msg="Abrir archivo",
                                 title="Control: fileopenbox",
                                 default='',
                                 filetypes=extension)
        print(archivo)
        return archivo

    def file_save(self):
        extension = ["*.py", "*.pyc"]
        archivo = eg.filesavebox(msg="Guardar archivo",
                                 title="Control: filesavebox",
                                 default='',
                                 filetypes=extension)
        return archivo

    def grid(self):
        self.rootLabel.pack()
        self.fckPackFields()
        self.BtConvertir.pack(side="right")
        self.BtExit.pack(side="left")
        # ##self.BtNewWindow.pack(side="right")

    def fckPackFields(self):
        controlador = ctrl.Control()

        if fields:
            i = 1
            for field in fields:
                # #create labels##
                row = tk.Frame(self.root)
                nameLabel = tk.Label(row, text=field[0]) # , anchor="center")
                valueLabel = tk.Label(row, text=field[1])
                self.BtEntrada = tk.Button(
                    row, text="in",
                    command=lambda: controlador.set_entrada(self))

                self.BtSalida = tk.Button(
                    row, text="out",
                    command=lambda: controlador.set_salida(self))
                # #pack labels##
                row.pack(side="top", fill="x", padx=5, pady=5) # , fill="x", padx=5, pady=5)
                nameLabel.pack(side="left", fill="x", padx=5, pady=5)
                valueLabel.pack(side="left", fill="x", padx=5, pady=5)
                if i==1:
                    self.BtEntrada.pack(side="left", fill="x", padx=5, pady=5)
                    i = i + 1
                else:
                    self.BtSalida.pack(side="left", fill="x", padx=5, pady=5)

        # #Buttons##
        self.BtExit = tk.Button(
            self.root, text="Salir", command=self.root.quit)

        self.BtConvertir = tk.Button(
            self.root, text="Convertir", padx=30,
            command=lambda: controlador.main())

    def run(self):
        self.grid()
        self.root.mainloop()
        self.root.destroy()