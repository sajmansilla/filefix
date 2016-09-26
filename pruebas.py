import tkinter as tk
import os
import codecs
import model as modelo
import view as vista
import control as ctrl

a = 0
fields = [("a", 1), ("c", 2), ("e", 3)]


class clsApp(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("FileFix")
        # #Labels##
        self.rootLabel = tk.Label(
            self.root, text="Seleccione los archivos", padx=100)
        self.aLabel = tk.Label(self.root, text=a, padx=100)
        # #Buttons##
        self.BtExit = tk.Button(
            self.root, text="Salir", command=self.root.quit)
        # ##self.BtNewWindow=tk.Button(self.root, text ="Edit",
        # command=lambda:self.clsNewWindow(self.root, self.aLabel).run())
        self.BtNewField = tk.Button(
            self.root, text="Convertir", padx=30,
            command=lambda: self.tratarLinea().run())

    def grid(self):
        self.rootLabel.pack()
        self.aLabel.pack()
        self.fckPackFields()
        self.BtNewField.pack()
        self.BtExit.pack(side="left")
        # ##self.BtNewWindow.pack(side="right")

    def fckPackFields(self):
        if fields:
            for field in fields:
                # #create labels##
                row = tk.Frame(self.root)
                nameLabel = tk.Label(row, text=field[0], width=20, anchor="w")
                valueLabel = tk.Label(row, text=field[1], width=5)
                # #pack labels##
                row.pack(side="top", fill="x", padx=5, pady=5)
                nameLabel.pack(side="left")
                valueLabel.pack(side="right", expand=True, fill="x")

    def run(self):
        self.grid()
        self.root.mainloop()
        self.root.destroy()

    class tratarLinea(object):
        def run(self):
            """Main"""
            path_entrada = vista.Vista().file_open()
            path_temp = './salida.prn'
            path_salida = vista.Vista().file_save()

            entrada = ctrl.preparar_archivo(path_entrada, path_temp)
            salida = codecs.open(path_salida, 'w', 'utf-8')

            for line in entrada:
                if line[0].isdigit() and line[1] == "/":
                    line = '0' + line

                if len(line) > 1 and (line[1] == "/" or line[2] == "/"):
                    linea_split = ctrl.tratar_linea(line)
                    total_linea = ctrl.obtener_total(linea_split)  # linea.len() - 1
                    iva_linea = ctrl.obtener_iva(linea_split)  # linea.len() - 2
                    gravado = ctrl.obtener_gravado(linea_split)  # linea.len() - 3
                    no_gravado = ctrl.obtener_no_gravado(linea_split)  # linea.len() - 4

                    cuit = ctrl.obtener_cuit(linea_split)  # linea.len() - 4/- 5
                    provincia = ctrl.obtener_provincia(linea_split)  # linea.len()-5/-6
                    razon_social = ctrl.obtener_razon_social(linea_split)

                    nro_comprobante = ctrl.obtener_nro_comprobante(linea_split)  # linea[4]
                    punto_venta = ctrl.obtener_punto_venta(linea_split)  # linea[3]
                    tipo_comprobante = ctrl.obtener_tipo_comp(linea_split)  # linea[2]
                    nombre_comprobante = ctrl.obtener_nombre_comp(linea_split)  # linea[1]
                    fecha = ctrl.obtener_fecha(linea_split)  # linea[0]

                    outline = modelo.Linea()
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
                    outline.condicion_fiscal_cliente = ctrl.calcular_cond_fiscal(
                        tipo_comprobante, cuit)
                    outline.cuit_cliente = cuit
                    outline.nombre_cliente = razon_social
                    outline.domicilio_cliente = ''
                    outline.codigo_postal = '0'
                    outline.provincia = provincia
                    outline.tipo_doc_cliente = ctrl.calcular_tipo_doc_cliente(cuit)
                    outline.moneda = ''
                    outline.tipo_cambio = '0'
                    outline.cai_cae = ''

                    salida.write(str(outline) + '\n')

            entrada.close()
            salida.close()
            os.remove(path_temp)

    class clsNewFields(object):

        def __init__(self, Parent):

            self.parent = Parent
            # #Window##
            self.top = tk.Toplevel()
            self.top.title("Add Fields")
            # #Labels##
            self.enterNameLabel = tk.Label(
                self.top, text="Enter fieldname", padx=10)
            self.enterValueLabel = tk.Label(
                self.top, text="Enter value", padx=10)
            # #Entryfields##
            self.EntryName = tk.Entry(self.top)
            self.EntryValue = tk.Entry(self.top)
            # #Buttons##
            self.BtADD = tk.Button(
                self.top, text="ADD", command=lambda: self.fckAddField(
                    self.EntryName, self.EntryValue))
            self.BtClose = tk.Button(
                self.top, text="Close", command=self.top. quit)

        def grid(self):
            self.enterNameLabel.pack()
            self.enterValueLabel.pack()
            self.EntryName.pack()
            self.EntryValue.pack()
            self.BtADD.pack()
            self.BtClose.pack()

        def fckAddField(self, Name, Value):
            self.name = Name.get()
            self.value = Value.get()
            global fields
            fields.append((self.name, self.value))
            print(fields)
            self.parent.update

        def run(self):
            self.grid()
            self.top.mainloop()
            self.top.destroy()


clsApp().run()
