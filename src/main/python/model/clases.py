# /usr/bin/env  python     # Linea de inicializacion
# -*- coding: UTF-8 -*-

# Declaracion de Clase Linea


class Linea:
    """
        Clase Linea
        Esta clase incluye todos los campos que necesita una línea
        del pnr de Holistor.
    """

    provincias = {
        'C': 0, 'B': 1, 'K': 2, 'X': 3, 'W': 4,
        'E': 5, 'Y': 6, 'M': 7, 'F': 8, 'A': 9,
        'J': 10, 'D': 11, 'S': 12, 'G': 13, 'T': 14,
        'H': 16, 'U': 17, 'P': 18, 'N': 19, 'Q': 20,
        'L': 21, 'R': 22, 'Z': 23, 'V': 24}

    @staticmethod
    def calcular_tipo_doc_cliente(cuit):
        if int(cuit) > 0:
            tipo_doc_cliente = '80'
        else:
            tipo_doc_cliente = '99'
        return tipo_doc_cliente

    def calcular_cond_fiscal(self,tipo, cuit):
        if int(cuit) > 0:
            if tipo == 'A':
                condic_fiscal = 'RI'
            else:
                condic_fiscal = 'MT'
        else:
            condic_fiscal = 'CF'
        return condic_fiscal

    def calcular_cuit_cli(self, valores):
        if self.no_gravado: # El total es no gravado
            salida = valores[len(valores) - 1]
        elif self.todo_gravado: # No hay no gravado
            salida = valores[len(valores) - 2]
        else:
            salida = valores[len(valores) - 3]
        if len(salida) > 10:
            salida = salida.replace('-')
            salida = salida.replace('.')
        else:
            salida = ''
        cuit = salida
        return cuit

    def calcular_valores(self, valores):
        # TODO: Esto está andando mal
        total = (valores[0].replace('.','')).replace(',','.')
        total = float(total)
        valores_corregidos = [total]
        control = 0
        for valor in valores[1:]:
            try:
                monto = valor
                monto = monto.replace('.','')
                monto = monto.replace(',','.')
                monto = float(monto)
            except ValueError:
                if len(monto) > 1:
                    print("Es un CUIT")
                else:
                    print("Es una provincia")
                break
            control += monto
            if total >= control:
                valores_corregidos.append(monto)
            else:
                print("El total es menor a la suma.")
                break
        if len(valores_corregidos) == 2: # No Gravado
            valores_corregidos.append(0,0)
            valores_corregidos.append(1, 0)
            self.no_gravado = True
        elif len(valores_corregidos) == 3: # Gravado 100%
            valores_corregidos.append(0)
            self.todo_gravado = True
        return valores_corregidos

    def __init__(self, linea):
        self.no_gravado = False
        self.todo_gravado = False
        self.nro_comprobante = linea[4]
        self.nombre_comprobante = linea[1]
        self.tipo_comprobante = linea[2]
        self.punto_venta = linea[3]
        self.fecha = linea[0]
        # Esto haría la distribucion de montos
        valores = linea[len(linea) - 4:len(linea)]
        valores.reverse()
        self.salida = self.calcular_valores(valores)
        self.total = self.salida[0]
        iva_linea = self.salida[1]
        self.codigo_neto_gravado = 'VTA'
        self.neto_gravado = self.salida[2]
        self.cod_concepto_no_gravado = 'NG'
        self.conceptos_no_gravados = self.salida[3]
        self.cod_operacion_exenta = 'EXV'
        self.operaciones_exentas = '0'
        self.codigo_perc_ret_pc = 'P01'
        self.percepciones = '0'
        self.tasa_iva = '21'
        self.iva_liquidado = iva_linea
        self.debito_fiscal = iva_linea
        cuit_cli = self.calcular_cuit_cli(linea[len(linea) - 5:len(linea)- 3])
        self.nombre_cliente = linea[5:]
        self.cuit_cliente = cuit_cli
        cond_fiscal = self.calcular_cond_fiscal(self.tipo_comprobante,
                                                self.cuit_cliente,
                                                self.nombre_cliente)
        self.condicion_fiscal_cliente = cond_fiscal
        self.domicilio_cliente = ''
        self.codigo_postal = '0'
        self.provincia = linea
        self.tipo_doc_cliente = self.calcular_tipo_doc_cliente(cuit_cli)
        self.moneda = ''
        self.tipo_cambio = '0'
        self.cai_cae = ''


    @property
    def nombre_comprobante(self):
        """
        Nombre del Comprobante. Ej: Factura, Nota de Credito, Nota de Debito
        """
        # print("Llamada a getter de nombre_comprobante")
        return self._nombre_comprobante

    @nombre_comprobante.setter
    def nombre_comprobante(self, value):
        # print("Llamada a setter de nombre_comprobante")
        value = str(value) + (20 - len(value)) * ' '
        self._nombre_comprobante = value

    @nombre_comprobante.deleter
    def nombre_comprobante(self):
        # print("Llamada a deleter de nombre_comprobante")
        del self._nombre_comprobante

    @property
    def tipo_comprobante(self):
        """
        Tipo del Comprobante. Ej: A, B
        """
        # print("Llamada a getter de tipo_comprobante")
        return self._tipo_comprobante

    @tipo_comprobante.setter
    def tipo_comprobante(self, value):
        # print("Llamada a setter de tipo_comprobante")
        self._tipo_comprobante = value

    @tipo_comprobante.deleter
    def tipo_comprobante(self):
        # print("Llamada a deleter de tipo_comprobante")
        del self._tipo_comprobante

    @property
    def punto_venta(self):
        """
        Punto de Venta. Formato 0000
        """
        # print("Llamada a getter de punto_venta")
        return self._punto_venta

    @punto_venta.setter
    def punto_venta(self, value):
        # print("Llamada a setter de punto_venta")
        pto_vta = value
        pto_vta = (4 - len(pto_vta)) * '0' + str(pto_vta)
        self._punto_venta = pto_vta

    @punto_venta.deleter
    def punto_venta(self):
        # print("Llamada a deleter de punto_venta")
        del self._punto_venta

    @property
    def nro_comprobante(self):
        """
        Numero de Comprobante. Formato 00000000
        """
        # print("Llamada a getter de nro_comprobante")
        return self._nro_comprobante

    @nro_comprobante.setter
    def nro_comprobante(self, value):
        # print("Llamada a setter de nro_comprobante")
        value = (8 - len(value)) * '0' + str(value)
        self._nro_comprobante = value

    @nro_comprobante.deleter
    def nro_comprobante(self):
        # print("Llamada a deleter de nro_comprobante")
        del self._nro_comprobante

    @property
    def fecha(self):
        """
        Fecha de Comprobante. Formato dd/mm/yyyy
        """
        # print("Llamada a getter de fecha")
        return self._fecha

    @fecha.setter
    def fecha(self, value):
        # print("Llamada a setter de fecha")
        self._fecha = value

    @fecha.deleter
    def fecha(self):
        # print("Llamada a deleter de fecha")
        del self._fecha

    @property
    def codigo_neto_gravado(self):
        """
        Codigo Neto Gravado.
        El código puede ser alfanumérico. De no existir este dato, el sistema utilizará el Código Auxiliar por Defecto.
        """
        # print("Llamada a getter de codigo_neto_gravado")
        return self._codigo_neto_gravado

    @codigo_neto_gravado.setter
    def codigo_neto_gravado(self, value):
        # print("Llamada a setter de codigo_neto_gravado")
        value = (5 - len(value)) * ' ' + str(value)
        self._codigo_neto_gravado = value

    @codigo_neto_gravado.deleter
    def codigo_neto_gravado(self):
        # print("Llamada a deleter de codigo_neto_gravado")
        del self._codigo_neto_gravado

    @property
    def neto_gravado(self):
        """
        Neto Gravado. Puede utilizarse cualquier separador (coma, punto, etc.) Formato 0.00
        """
        # print("Llamada a getter de neto_gravado")
        return self._neto_gravado

    @neto_gravado.setter
    def neto_gravado(self, value):
        # print("Llamada a setter de neto_gravado")
        value = (15 - len(value)) * ' ' + str(value)
        self._neto_gravado = value

    @neto_gravado.deleter
    def neto_gravado(self):
        # print("Llamada a deleter de neto_gravado")
        del self._neto_gravado

    @property
    def cod_concepto_no_gravado(self):
        """
        Cód. Concepto no Gravado.
        El código puede ser alfanumérico. De no existir este dato, el sistema utilizará el Código Auxiliar por Defecto.
        """
        # print("Llamada a getter de cod_concepto_no_gravado")
        return self._cod_concepto_no_gravado

    @cod_concepto_no_gravado.setter
    def cod_concepto_no_gravado(self, value):
        # print("Llamada a setter de cod_concepto_no_gravado")
        value = (5 - len(value)) * ' ' + str(value)
        self._cod_concepto_no_gravado = value

    @cod_concepto_no_gravado.deleter
    def cod_concepto_no_gravado(self):
        # print("Llamada a deleter de cod_concepto_no_gravado")
        del self._cod_concepto_no_gravado

    @property
    def conceptos_no_gravados(self):
        """
        Conceptos no Gravados.
        Puede utilizarse cualquier separador (coma, punto, etc.)
        """
        # print("Llamada a getter de conceptos_no_gravados")
        return self._conceptos_no_gravados

    @conceptos_no_gravados.setter
    def conceptos_no_gravados(self, value):
        # print("Llamada a setter de conceptos_no_gravados")
        value = (15 - len(value)) * ' ' + str(value)
        self._conceptos_no_gravados = value

    @conceptos_no_gravados.deleter
    def conceptos_no_gravados(self):
        # print("Llamada a deleter de conceptos_no_gravados")
        del self._conceptos_no_gravados

    @property
    def cod_operacion_exenta(self):
        """
        Cód. Operación Exenta.
        El código puede ser alfanumérico. De no existir este dato, el sistema utilizará el Código Auxiliar por Defecto.
        """
        # print("Llamada a getter de cod_operacion_exenta")
        return self._cod_operacion_exenta

    @cod_operacion_exenta.setter
    def cod_operacion_exenta(self, value):
        # print("Llamada a setter de cod_operacion_exenta")
        value = (5 - len(value)) * ' ' + str(value)
        self._cod_operacion_exenta = value

    @cod_operacion_exenta.deleter
    def cod_operacion_exenta(self):
        # print("Llamada a deleter de cod_operacion_exenta")
        del self._cod_operacion_exenta

    @property
    def operaciones_exentas(self):
        """
        Operaciones Exentas.
        Puede utilizarse cualquier separador (coma, punto, etc.)
        """
        # print("Llamada a getter de operaciones_exentas")
        return self._operaciones_exentas

    @operaciones_exentas.setter
    def operaciones_exentas(self, value):
        # print("Llamada a setter de operaciones_exentas")
        value = (15 - len(value)) * ' ' + str(value)
        self._operaciones_exentas = value

    @operaciones_exentas.deleter
    def operaciones_exentas(self):
        # print("Llamada a deleter de operaciones_exentas")
        del self._operaciones_exentas

    @property
    def codigo_perc_ret_pc(self):
        """
        Código Perc./Ret./P.C.
        El código puede ser alfanumérico.
        """
        # print("Llamada a getter de codigo_perc_ret_pc")
        return self._codigo_perc_ret_pc

    @codigo_perc_ret_pc.setter
    def codigo_perc_ret_pc(self, value):
        # print("Llamada a setter de codigo_perc_ret_pc")
        value = (5 - len(value)) * ' ' + str(value)
        self._codigo_perc_ret_pc = value

    @codigo_perc_ret_pc.deleter
    def codigo_perc_ret_pc(self):
        # print("Llamada a deleter de codigo_perc_ret_pc")
        del self._codigo_perc_ret_pc

    @property
    def percepciones(self):
        """
        Percepciones
        Puede utilizarse cualquier separador (coma, punto, etc.)
        """
        # print("Llamada a getter de percepciones")
        return self._percepciones

    @percepciones.setter
    def percepciones(self, value):
        # print("Llamada a setter de percepciones")
        value = (15 - len(value)) * ' ' + str(value)
        self._percepciones = value

    @percepciones.deleter
    def percepciones(self):
        # print("Llamada a deleter de percepciones")
        del self._percepciones

    @property
    def provincia_ret_perc(self):
        """
        Provincia Ret. Perc.
        No obligatorio. Es importante incluirla para determinar la jurisdicción en Convenio Multilateral, cuando la
        provincia a la que corresponde la retención o percepción es distinta a la del comprobante, o cuando dentro de
        un mismo comprobante se incluyen retenciones/percepciones correspondientes a distintas provincias.
        """
        # print("Llamada a getter de provincia_ret_perc")
        return self._provincia_ret_perc

    @provincia_ret_perc.setter
    def provincia_ret_perc(self, value):
        # print("Llamada a setter de provincia_ret_perc"
        if len(value[len(value) - 3]) > 9 or len(value[len(value) - 5]) > 9:
            falta_cuit = False
        else:
            falta_cuit = True
        if self.no_gravado and falta_cuit:
            provincia = value[len(value) - 3]
        elif self.no_gravado and not falta_cuit:
            provincia = value[len(value) - 4]
        elif falta_cuit and not self.no_gravado:
            provincia = value[len(value) - 5]
        else:
            provincia = value[len(value) - 6]

        try:
            provincia = '00' + str(self.provincias[provincia])
            provincia = provincia[len(provincia) - 2:]
        except KeyError:
            print("Error en comprobante nro: " + str(self.nro_comprobante))
            print("Intenta ingresar como Razón Social: " + str(self.nombre_cliente))
            provincia = (5 - len(provincia)) * ' ' + str(provincia)
        self._provincia_ret_perc = provincia

    @provincia_ret_perc.deleter
    def provincia_ret_perc(self):
        # print("Llamada a deleter de provincia_ret_perc")
        del self._provincia_ret_perc

    @property
    def tasa_iva(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de tasa_iva")
        return self._tasa_iva

    @tasa_iva.setter
    def tasa_iva(self, value):
        # print("Llamada a setter de tasa_iva")
        value = (5 - len(value)) * ' ' + str(value)
        self._tasa_iva = value

    @tasa_iva.deleter
    def tasa_iva(self):
        # print("Llamada a deleter de tasa_iva")
        del self._tasa_iva

    @property
    def iva_liquidado(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de iva_liquidado")
        return self._iva_liquidado

    @iva_liquidado.setter
    def iva_liquidado(self, value):
        # print("Llamada a setter de iva_liquidado")
        value = (15 - len(value)) * ' ' + str(value)
        self._iva_liquidado = value

    @iva_liquidado.deleter
    def iva_liquidado(self):
        # print("Llamada a deleter de iva_liquidado")
        del self._iva_liquidado

    @property
    def debito_fiscal(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de debito_fiscal")
        return self._debito_fiscal

    @debito_fiscal.setter
    def debito_fiscal(self, value):
        # print("Llamada a setter de debito_fiscal")
        value = (15 - len(value)) * ' ' + str(value)
        self._debito_fiscal = value

    @debito_fiscal.deleter
    def debito_fiscal(self):
        # print("Llamada a deleter de debito_fiscal")
        del self._debito_fiscal

    @property
    def total(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de total")
        return self._total

    @total.setter
    def total(self, value):
        # print("Llamada a setter de total")
        total = value
        total = total.replace('.', '')
        total = total.replace(',', '')
        total = (15 - len(str(total))) * ' ' + str(total)
        self._total = total

    @total.deleter
    def total(self):
        # print("Llamada a deleter de total")
        del self._total

    @property
    def condicion_fiscal_cliente(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de condicion_fiscal_cliente")
        return self._condicion_fiscal_cliente

    @condicion_fiscal_cliente.setter
    def condicion_fiscal_cliente(self, value):
        # print("Llamada a setter de condicion_fiscal_cliente")
        value = (5 - len(value)) * ' ' + str(value)
        self._condicion_fiscal_cliente = value

    @condicion_fiscal_cliente.deleter
    def condicion_fiscal_cliente(self):
        # print("Llamada a deleter de condicion_fiscal_cliente")
        del self._condicion_fiscal_cliente

    @property
    def cuit_cliente(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de cuit_cliente")
        return self._cuit_cliente

    @cuit_cliente.setter
    def cuit_cliente(self, value):
        # print("Llamada a setter de cuit_cliente")
        primer_num = value[0:2]
        segund_num = value[2:len(value)-1]
        tercer_num = value[len(value)-1]
        value = str(primer_num) + str(segund_num) + str(tercer_num)
        self._cuit_cliente = value

    @cuit_cliente.deleter
    def cuit_cliente(self):
        # print("Llamada a deleter de cuit_cliente")
        del self._cuit_cliente

    @property
    def nombre_cliente(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de nombre_cliente")
        return self._nombre_cliente

    @nombre_cliente.setter
        # print("Llamada a setter de nombre_cliente")
    def nombre_cliente(self, linea):
        if len(linea[len(linea) - 5]) == 1:
            posicion = 5
        elif len(linea[len(linea) - 6]) == 1:
            posicion = 6
        else:
            posicion = 0

        razon_social = linea[:len(linea) - posicion]
        razon_social = ' '.join(razon_social) + '                         '
        razon_social = razon_social[0:29]
        razon_social = str(razon_social) + (30 - len(razon_social)) * ' '

        try:
            self._nombre_cliente = razon_social
        except KeyError:
            print("Error en comprobante nro: " + str(self.nro_comprobante))
            print("Intenta ingresar como Razón Social: " + str(razon_social))


    @nombre_cliente.deleter
    def nombre_cliente(self):
        # print("Llamada a deleter de nombre_cliente")
        del self._nombre_cliente

    @property
    def domicilio_cliente(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si
        tiene o no el símbolo %.
        """
        # print("Llamada a getter de domicilio_cliente")
        return self._domicilio_cliente

    @domicilio_cliente.setter
    def domicilio_cliente(self, value):
        # print("Llamada a setter de domicilio_cliente")
        value = str(value) + (50 - len(value)) * ' '
        self._domicilio_cliente = value

    @domicilio_cliente.deleter
    def domicilio_cliente(self):
        # print("Llamada a deleter de domicilio_cliente")
        del self._domicilio_cliente

    @property
    def codigo_postal(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de codigo_postal")
        return self._codigo_postal

    @codigo_postal.setter
    def codigo_postal(self, value):
        # print("Llamada a setter de codigo_postal")
        value = (10 - len(value)) * ' ' + str(value)
        self._codigo_postal = value

    @codigo_postal.deleter
    def codigo_postal(self):
        # print("Llamada a deleter de codigo_postal")
        del self._codigo_postal

    @property
    def provincia(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de provincia")
        return self._provincia

    @provincia.setter
    def provincia(self, linea):
        # print("Llamada a setter de provincia")
        if len(linea[len(linea) - 5]) == 1:
            provincia = linea[len(linea) - 5]
        elif len(linea[len(linea) - 6]) == 1:
            provincia = linea[len(linea) - 6]
        else:
            provincia = ''

        try:
            provincia = '00' + str(self.provincias[provincia])
            provincia = provincia[len(provincia) - 2:]
            value = (4 - len(provincia)) * ' ' + str(provincia)
            self._provincia = value
        except KeyError:
            print("Error en comprobante nro: " + str(self.nro_comprobante))
            print("Intenta ingresar como Provincia: " + str(provincia))
            # TODO: Tengo que escapar de la ejecución aquí

    @provincia.deleter
    def provincia(self):
        # print("Llamada a deleter de provincia")
        del self._provincia

    @property
    def tipo_doc_cliente(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de tipo_doc_cliente")
        return self._tipo_doc_cliente

    @tipo_doc_cliente.setter
    def tipo_doc_cliente(self, value):
        # print("Llamada a setter de tipo_doc_cliente")
        value = (3 - len(value)) * ' ' + str(value)
        self._tipo_doc_cliente = value

    @tipo_doc_cliente.deleter
    def tipo_doc_cliente(self):
        # print("Llamada a deleter de tipo_doc_cliente")
        del self._tipo_doc_cliente

    @property
    def moneda(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de moneda")
        return self._moneda

    @moneda.setter
    def moneda(self, value):
        # print("Llamada a setter de moneda")
        value = (3 - len(value)) * ' ' + str(value)
        self._moneda = value

    @moneda.deleter
    def moneda(self):
        # print("Llamada a deleter de moneda")
        del self._moneda

    @property
    def Tipo_cambio(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de Tipo_cambio")
        return self._Tipo_cambio

    @Tipo_cambio.setter
    def Tipo_cambio(self, value):
        # print("Llamada a setter de Tipo_cambio")
        value = (15 - len(value)) * ' ' + str(value)
        self._Tipo_cambio = value

    @Tipo_cambio.deleter
    def Tipo_cambio(self):
        # print("Llamada a deleter de Tipo_cambio")
        del self._Tipo_cambio

    @property
    def cai_cae(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
        """
        # print("Llamada a getter de cai_cae")
        return self._cai_cae

    @cai_cae.setter
    def cai_cae(self, value):
        # print("Llamada a setter de cai_cae")
        value = (14 - len(value)) * ' ' + str(value)
        self._cai_cae = value

    @cai_cae.deleter
    def cai_cae(self):
        # print("Llamada a deleter de cai_cae")
        del self._cai_cae


    def __str__(self):
        cadena = \
                    str(self.nombre_comprobante) + str(self.tipo_comprobante) + str(self.punto_venta) \
                 + str(self.nro_comprobante) + str(self.fecha) + str(self.codigo_neto_gravado) \
                 + str(self.neto_gravado) + str(self.cod_concepto_no_gravado) \
                 + str(self.conceptos_no_gravados) + str(self.cod_operacion_exenta) \
                 + str(self.operaciones_exentas) + str(self.codigo_perc_ret_pc) \
                 + str(self.percepciones) + str(self.provincia_ret_perc) + str(self.tasa_iva) \
                 + str(self.iva_liquidado) + str(self.debito_fiscal) + str(self.total) \
                 + str(self.condicion_fiscal_cliente) + str(self.cuit_cliente) + str(self.nombre_cliente) \
                 + str(self.domicilio_cliente) + str(self.codigo_postal) + str(self.provincia) \
                 + str(self.tipo_doc_cliente) + str(self.moneda) + str(self.tipo_cambio) \
                 + str(self.cai_cae)
        return cadena