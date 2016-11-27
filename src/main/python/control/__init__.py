# /usr/bin/env  python     # Linea de inicializacion
# -*- coding: UTF-8 -*-

# Modulos que se importan
import os
import codecs
import easygui as eg
from model.clases import Linea
from view import *

# Documentacion del script
__author__ = 'Sebastian Mansilla'
""" Modulo de ejemplo """

# Declaracion de variables Globales
path_salida = ''
path_entrada = ''
path_temp = ''
provincias = {
    'C': 0, 'B': 1, 'K': 2, 'X': 3, 'W': 4,
    'E': 5, 'Y': 6, 'M': 7, 'F': 8, 'A': 9,
    'J': 10, 'D': 11, 'S': 12, 'G': 13, 'T': 14,
    'H': 16, 'U': 17, 'P': 18, 'N': 19, 'Q': 20,
    'L': 21, 'R': 22, 'Z': 23, 'V': 24}


# Declaracion de Clases
class Control:
    """docstring for  Control"""


    #vista.file_open()
    path_entrada = ''
    path_temp = './salida.prn'
    #vista.file_save()
    path_salida = ''

    def __init__(self, root):
        print("Esta es la clase control")
        #self.model = Linea(0)
        self.view = View(root)
        self.view.bEntrada.config(command = self.set_entrada)
        self.view.bSalida.config(command = self.set_salida)
        self.view.bConvert.config(command = self.main)


    # Declaracion de Funciones

    def set_entrada(self):
        extension = ['*.tsv', '*.txt']
        self.path_entrada = eg.fileopenbox(msg="Abrir archivo",
                                 title="Control: fileopenbox",
                                 default='',
                                 filetypes=extension)
        print(self.path_entrada)
        self.view.lIn.config(text = self.path_entrada)

    def set_salida(self):
        extension = ["*.pnr"]
        self.path_salida = eg.filesavebox(msg="Guardar archivo",
                                 title="Control: filesavebox",
                                 default='',
                                 filetypes=extension)
        print(self.path_salida)
        self.view.lOut.config(text = self.path_salida)


    def obtener_razon_social(self,linea):
        if len(linea[len(linea) - 5]) == 1:
            posicion = 5
        elif len(linea[len(linea) - 6]) == 1:
            posicion = 6
        else:
            posicion = 0

        razon_social = linea[5:len(linea) - posicion]
        razon_social = ' '.join(razon_social) + '                         '
        razon_social = razon_social[0:29]
        return razon_social


    def obtener_provincia(self,linea):
        if len(linea[len(linea) - 5]) == 1:
            provincia = linea[len(linea) - 5]
        elif len(linea[len(linea) - 6]) == 1:
            provincia = linea[len(linea) - 6]
        else:
            provincia = ''

        try:
            provincia = '00' + str(provincias[provincia])
            provincia = provincia[len(provincia) - 2:]
            return provincia
        except KeyError:
            print("Error en comprobante nro: " + str(self.nro_comprobante))
            print("Intenta ingresar como Razón Social: " + str(razon_social))


    def preparar_archivo(self,path_entrada, path_salida):
        infile = codecs.open(path_entrada, 'r', 'latin-1')
        outfile = codecs.open(path_salida, 'w', 'latin-1')

        outfile.write(infile.read())

        outfile.close()
        infile.close()

        infile = open(path_salida, 'r')
        return infile


    def obtener_cuit(self,linea):
        if linea[len(linea) - 4].find(',') == -1 and \
                len(linea[len(linea) - 4]) >= 11:
            cuit = linea[len(linea) - 4].replace('-', '')
            cuit = cuit.replace('.', '')
        elif linea[len(linea) - 5].find(',') == -1 and \
                len(linea[len(linea) - 5]) >= 11:
            cuit = linea[len(linea) - 5].replace('-', '')
            cuit = cuit.replace('.', '')
        else:
            cuit = '00000000000'
        return cuit


    def obtener_no_gravado(self,linea):
        if linea[len(linea) - 4].find(',') > 0:
            no_gravado = linea[len(linea) - 4]
            no_gravado = no_gravado.replace('.', '')
            no_gravado = no_gravado.replace(',', '')
        else:
            no_gravado = 0
        no_gravado = float(no_gravado) / 100
        no_gravado = str(no_gravado)
        return str(no_gravado)


    def obtener_gravado(self,linea):
        gravado = linea[len(linea) - 3]

        gravado = gravado.replace('.', '')
        gravado = gravado.replace(',', '')
        try:
            gravado = float(gravado) / 100
            gravado = str(gravado)
            return gravado
        except Exception as e:
            print("Tipo excepcion: " + type(e))
            print("Excepcion: " + e)


    def obtener_iva(self,linea):
        iva = linea[len(linea) - 2]
        iva = iva.replace('.', '')
        iva = iva.replace(',', '')
        iva = float(iva) / 100
        iva = str(iva)
        return iva

    def obtener_total(self,linea):
        total = linea[len(linea) - 1]
        total = total.replace('.', '')
        total = total.replace(',', '')
        total = float(total) / 100
        total = str(total)
        return total

    def tratar_linea(self, linea):
        # Elimino caracteres a izquierda y derecha de la linea y
        # separo por espacios.
        linea = linea.strip()
        linea = linea.split()
        return linea

    def obtener_nro_comprobante(self,linea):
        nro_comprobante = linea[4]
        return nro_comprobante

    def obtener_punto_venta(self,linea):
        pto_vta = linea[3]
        pto_vta = '0000' + str(pto_vta)
        pto_vta = pto_vta[len(pto_vta) - 4:]
        return pto_vta

    def obtener_tipo_comp(self,linea):
        letra_comprobante = linea[2]
        return letra_comprobante

    def obtener_nombre_comp(self,linea):
        tipo_comprobante = linea[1]
        return tipo_comprobante

    def obtener_fecha(self,linea):
        fecha = linea[0]
        return fecha

    def calcular_cond_fiscal(self,tipo, cuit):
        if int(cuit) > 0:
            if tipo == 'A':
                condic_fiscal = 'RI'
            else:
                condic_fiscal = 'MT'
        else:
            condic_fiscal = 'CF'
        return condic_fiscal

    def calcular_tipo_doc_cliente(self,cuit):
        if int(cuit) > 0:
            tipo_doc_cliente = '80'
        else:
            tipo_doc_cliente = '99'
        return tipo_doc_cliente

    # def main():
    #     print("Llamada buena")

    def main(self):
        """Main"""

        # #vista.file_open()
        # path_entrada = '/home/sebastian/PycharmProjects/filefix/DANI0716.tsv'
        # path_temp = './salida.prn'
        # #vista.file_save()
        # path_salida = '/home/sebastian/PycharmProjects/filefix/nuevo.prn'

        entrada = self.preparar_archivo(self.path_entrada, self.path_temp)
        salida = codecs.open(self.path_salida, 'w', 'latin-1')

        for line in entrada:
            if line[0].isdigit() and line[1] == "/":
                line = '0' + line

            if len(line) > 1 and (line[1] == "/" or line[2] == "/"):
                linea_split = self.tratar_linea(line)
                total_linea = self.obtener_total(linea_split)  # linea.len() - 1
                iva_linea = self.obtener_iva(linea_split)  # linea.len() - 2
                gravado = self.obtener_gravado(linea_split)  # linea.len() - 3
                no_gravado = self.obtener_no_gravado(linea_split)  # linea.len() - 4

                cuit = self.obtener_cuit(linea_split)  # linea.len() - 4/- 5
                #provincia = self.obtener_provincia(linea_split)  # linea.len()-5/-6
                #razon_social = self.obtener_razon_social(linea_split)

                nro_comprobante = self.obtener_nro_comprobante(linea_split)  # linea[4]
                punto_venta = self.obtener_punto_venta(linea_split)  # linea[3]
                tipo_comprobante = self.obtener_tipo_comp(linea_split)  # linea[2]
                nombre_comprobante = self.obtener_nombre_comp(linea_split)  # linea[1]
                fecha = self.obtener_fecha(linea_split)  # linea[0]

                outline = Linea(nro_comprobante)
                outline.nombre_comprobante = nombre_comprobante
                outline.tipo_comprobante = tipo_comprobante
                outline.punto_venta = punto_venta
                outline.nro_comprobante = nro_comprobante
                outline.fecha = fecha
                outline.codigo_neto_gravado = 'VTA'
                outline.neto_gravado = gravado
                outline.cod_concepto_no_gravado = 'NG'
                outline.conceptos_no_gravados = no_gravado
                outline.cod_operacion_exenta = 'EXV'
                outline.operaciones_exentas = '0'
                outline.codigo_perc_ret_pc = 'P01'
                outline.percepciones = '0'
                outline.provincia_ret_perc = linea_split
                outline.tasa_iva = '21'
                outline.iva_liquidado = iva_linea
                outline.debito_fiscal = iva_linea
                outline.total = total_linea
                outline.condicion_fiscal_cliente = self.calcular_cond_fiscal(
                    tipo_comprobante, cuit)
                outline.cuit_cliente = cuit
                outline.nombre_cliente = linea_split
                outline.domicilio_cliente = ''
                outline.codigo_postal = '0'
                outline.provincia = linea_split
                outline.tipo_doc_cliente = self.calcular_tipo_doc_cliente(cuit)
                outline.moneda = ''
                outline.tipo_cambio = '0'
                outline.cai_cae = ''

                salida.write(str(outline) + '\n')

        entrada.close()
        salida.close()
        os.remove(self.path_temp)

        print("Arranco con\nentrada = " + self.path_entrada + "\nsalida = "
            + self.path_salida + "\ntemp = " + self.path_temp)
        #outline1 = Linea()

        eg.msgbox("El archivo se ha terminado de generar.\nPuede encontrarlo en: " + self.path_salida)
