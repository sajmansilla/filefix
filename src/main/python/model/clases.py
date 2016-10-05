# /usr/bin/env  python     # Linea de inicializacion
# -*- coding: UTF-8 -*-

# Declaracion de Clase Linea


class Linea:
    """
        Clase Linea
        Esta clase incluye todos los campos que necesita una línea
        del pnr de Holistor.
    """

    def __init__(self):
        return None

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
        value = (4 - len(value)) * '0' + str(value)
        self._punto_venta = value

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
        # print("Llamada a setter de provincia_ret_perc")
        value = (5 - len(value)) * ' ' + str(value)
        self._provincia_ret_perc = value

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
        value = (15 - len(str(value))) * ' ' + str(value)
        self._total = value

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
    def nombre_cliente(self, value):
        # print("Llamada a setter de nombre_cliente")
        value = str(value) + (30 - len(value)) * ' '
        self._nombre_cliente = value

    @nombre_cliente.deleter
    def nombre_cliente(self):
        # print("Llamada a deleter de nombre_cliente")
        del self._nombre_cliente

    @property
    def domicilio_cliente(self):
        """
        Tasa I.V.A.
        Puede utilizarse cualquier separador (coma, punto, etc.) No interesa si tiene o no el símbolo %.
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
    def provincia(self, value):
        # print("Llamada a setter de provincia")
        value = (4 - len(value)) * ' ' + str(value)
        self._provincia = value

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
        # formato impresion
        # cadena = self.nombre_comprobante + ', ' + self.tipo_comprobante + ', ' + self.punto_venta + ', ' \
        #          + self.nro_comprobante + ', ' + self.fecha + ', ' + self.codigo_neto_gravado + ', ' \
        #          + str(self.neto_gravado) + ', ' + self.cod_concepto_no_gravado + ', ' \
        #          + str(self.conceptos_no_gravados) + ', ' + self.cod_operacion_exenta + ', ' \
        #          + str(self.operaciones_exentas) + ', ' + self.codigo_perc_ret_pc + ', ' \
        #          + str(self.percepciones) + ', ' + self.provincia_ret_perc + ', ' + str(self.tasa_iva) + ', ' \
        #          + str(self.iva_liquidado) + ', ' + str(self.debito_fiscal) + ', ' + str(self.total) + ', ' \
        #          + self.condicion_fiscal_cliente + ', ' + str(self.cuit_cliente) + ', ' + self.nombre_cliente + ', ' \
        #          + self.domicilio_cliente + ', ' + str(self.codigo_postal) + ', ' + self.provincia + ', ' \
        #          + self.tipo_doc_cliente + ', ' + str(self.moneda) + ', ' + str(self.tipo_cambio) + ', ' \
        #          + str(self.cai_cae)
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