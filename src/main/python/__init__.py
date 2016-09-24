# /usr/bin/env  python     # Linea de inicializacion
# -*- coding: UTF-8 -*-

# Modulos que se importan
import os
import codecs
from src.main.python.clases import Linea

# Documentacion del script
__author__ = 'Sebastian Mansilla'
""" Modulo de ejemplo """

# Declaracion de variables Globales
provincias = {'C': 0, 'B': 1, 'K': 2, 'X': 3, 'W': 4, 'E': 5, 'Y': 6, 'M': 7, 'F': 8, 'A': 9, 'J': 10, 'D': 11, 'S': 12,
              'G': 13, 'T': 14, 'H': 16, 'U': 17, 'P': 18, 'N': 19, 'Q': 20, 'L': 21, 'R': 22, 'Z': 23, 'V': 24}


# Declaracion de Funciones


def obtener_razon_social(linea):
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


def obtener_provincia(linea):
    if len(linea[len(linea) - 5]) == 1:
        provincia = linea[len(linea) - 5]
    elif len(linea[len(linea) - 6]) == 1:
        provincia = linea[len(linea) - 6]
    else:
        provincia = ''

    provincia = '00' + str(provincias[provincia])
    provincia = provincia[len(provincia)-2:]
    return provincia


def preparar_archivo(path_entrada, path_salida):
    infile = codecs.open(path_entrada, 'r', 'latin-1')
    outfile = codecs.open(path_salida, 'w', 'utf-8')

    outfile.write(infile.read())

    outfile.close()
    infile.close()

    infile = open(path_salida, 'r')
    return infile


def obtener_cuit(linea):
    if linea[len(linea) - 4].find(',') == -1 and len(linea[len(linea) - 4]) >= 11:
        cuit = linea[len(linea) - 4].replace('-', '')
        cuit = cuit.replace('.', '')
    elif linea[len(linea) - 5].find(',') == -1 and len(linea[len(linea) - 5]) >= 11:
        cuit = linea[len(linea) - 5].replace('-', '')
        cuit = cuit.replace('.', '')
    else:
        cuit = '00000000000'
    return cuit


def obtener_no_gravado(linea):
    if linea[len(linea) - 4].find(',') > 0:
        no_gravado = linea[len(linea) - 4]
        no_gravado = no_gravado.replace('.', '')
        no_gravado = no_gravado.replace(',', '')
    else:
        no_gravado = 0
    no_gravado = float(no_gravado)/100
    no_gravado = str(no_gravado)
    return str(no_gravado)


def obtener_gravado(linea):
    gravado = linea[len(linea) - 3]
    gravado = gravado.replace('.', '')
    gravado = gravado.replace(',', '')
    gravado = float(gravado)/100
    gravado = str(gravado)
    return gravado


def obtener_iva(linea):
    iva = linea[len(linea) - 2]
    iva = iva.replace('.', '')
    iva = iva.replace(',', '')
    iva = float(iva)/100
    iva = str(iva)
    return iva


def obtener_total(linea):
    total = linea[len(linea) - 1]
    total = total.replace('.', '')
    total = total.replace(',', '')
    total = float(total)/100
    total = str(total)
    return total


def tratar_linea(linea):
    # Elimino caracteres a izquierda y derecha de la linea y separo por espacios.
    linea = linea.strip()
    linea = linea.split()
    return linea


def obtener_nro_comprobante(linea):
    nro_comprobante = linea[4]
    return nro_comprobante


def obtener_punto_venta(linea):
    pto_vta = linea[3]
    pto_vta = '0000' + str(pto_vta)
    pto_vta = pto_vta[len(pto_vta) - 4:]
    return pto_vta


def obtener_tipo_comprobante(linea):
    letra_comprobante = linea[2]
    return letra_comprobante


def obtener_nombre_comprobante(linea):
    tipo_comprobante = linea[1]
    return tipo_comprobante


def obtener_fecha(linea):
    fecha = linea[0]
    return fecha


def calcular_condicion_fiscal(tipo, cuit):
    if int(cuit) > 0:
        if tipo == 'A':
            condic_fiscal = 'RI'
        else:
            condic_fiscal = 'MT'
    else:
        condic_fiscal = 'CF'
    return condic_fiscal


def calcular_tipo_doc_cliente(cuit):
    if int(cuit) > 0:
        tipo_doc_cliente = '80'
    else:
        tipo_doc_cliente = '99'
    return tipo_doc_cliente


def main():
    """Main"""
    path_entrada = '/home/sebastian/PycharmProjects/filefix/DANI0716.tsv'
    path_salida = '/home/sebastian/PycharmProjects/filefix/temp.prn'

    entrada = preparar_archivo(path_entrada, path_salida)
    salida = codecs.open('/home/sebastian/PycharmProjects/filefix/salida.prn', 'w', 'utf-8')
    i = 0
    for line in entrada:
        if line[0].isdigit() and line[1] == "/":
            line = '0' + line

        if len(line) > 1 and (line[1] == "/" or line[2] == "/"):
            linea_split = tratar_linea(line)
            total_linea = obtener_total(linea_split)  # linea.len() - 1
            iva_linea = obtener_iva(linea_split)  # linea.len() - 2
            gravado = obtener_gravado(linea_split)  # linea.len() - 3
            no_gravado = obtener_no_gravado(linea_split)  # linea.len() - 4

            cuit = obtener_cuit(linea_split)  # linea.len() - 4 / linea.len() - 5
            provincia = obtener_provincia(linea_split)  # linea.len() - 5 / linea.len() - 6
            razon_social = obtener_razon_social(linea_split)

            nro_comprobante = obtener_nro_comprobante(linea_split)  # linea[4]
            punto_venta = obtener_punto_venta(linea_split)  # linea[3]
            tipo_comprobante = obtener_tipo_comprobante(linea_split)  # linea[2]
            nombre_comprobante = obtener_nombre_comprobante(linea_split)  # linea[1]
            fecha = obtener_fecha(linea_split)  # linea[0]

            outline = Linea()
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
            outline.provincia_ret_perc = provincia
            outline.tasa_iva = '21'
            outline.iva_liquidado = iva_linea
            outline.debito_fiscal = iva_linea
            outline.total = total_linea
            outline.condicion_fiscal_cliente = calcular_condicion_fiscal(tipo_comprobante, cuit)
            outline.cuit_cliente = cuit
            outline.nombre_cliente = razon_social
            outline.domicilio_cliente = ''
            outline.codigo_postal = '0'
            outline.provincia = provincia
            outline.tipo_doc_cliente = calcular_tipo_doc_cliente(cuit)
            outline.moneda = ''
            outline.tipo_cambio = '0'
            outline.cai_cae = ''

            # if int(nro_comprobante) == 59790: #(len(cuit) < 11 or len(cuit) > 13) and len(cuit) > 0 :
            # print(linea_split)
            i += 1
            # print(((4 - len(str(i))) * '0' + str(i)) + ': ' + str(fecha) + ' | ' + str(nombre_comprobante)
            #       + ' | ' + str(tipo_comprobante) + ' | '
            #       + str(punto_venta) + ' | ' + str(nro_comprobante) + ' | ' + str(razon_social) + ' | '
            #       + str(provincia) + ' | ' + str(cuit) + ' | ' + str(no_gravado) + ' | ' + str(gravado)
            #       + ' | ' + str(iva_linea) + ' | ' + str(total_linea))
            print(outline)
            # salida.write(str(outline) + '\n')

    entrada.close()
    salida.close()
    os.remove(path_salida)

# Cuerpo Principal
if __name__ == '__main__':
    main()

