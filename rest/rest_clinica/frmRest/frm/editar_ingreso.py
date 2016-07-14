from PyQt4 import QtCore, QtGui
import datetime
from frmFormato import frm_formato
from jsonFormato import json_formato
from rest import *

jsonFormato = json_formato()
recurso = resources()
lista_tipo_ingreso = ()
formato = frm_formato()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_FormEditarIngreso(object):
    def setupUi(self, Form, idIngreso):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(805, 517)
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        # self.ID_Ingreso = id
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_8.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.lblPacientes = QtGui.QLabel(Form)
        self.lblPacientes.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPacientes.setObjectName(_fromUtf8("lblPacientes"))
        self.verticalLayout_8.addWidget(self.lblPacientes)
        self.tblPacientes = QtGui.QTableWidget(Form)
        self.tblPacientes.setMinimumSize(QtCore.QSize(500, 0))
        self.tblPacientes.setMaximumSize(QtCore.QSize(5000, 400))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tblPacientes.setFont(font)
        self.tblPacientes.setFrameShape(QtGui.QFrame.Box)
        self.tblPacientes.setFrameShadow(QtGui.QFrame.Sunken)
        self.tblPacientes.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblPacientes.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblPacientes.setGridStyle(QtCore.Qt.SolidLine)
        self.tblPacientes.setCornerButtonEnabled(False)
        self.tblPacientes.setObjectName(_fromUtf8("tblPacientes"))
        self.tblPacientes.setColumnCount(3)
        self.tblPacientes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblPacientes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblPacientes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblPacientes.setHorizontalHeaderItem(2, item)
        self.tblPacientes.horizontalHeader().setDefaultSectionSize(225)
        self.tblPacientes.horizontalHeader().setHighlightSections(False)
        self.tblPacientes.horizontalHeader().setMinimumSectionSize(100)
        self.tblPacientes.verticalHeader().setVisible(False)
        self.tblPacientes.verticalHeader().setHighlightSections(False)
        self.verticalLayout_8.addWidget(self.tblPacientes)
        spacerItem = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lblIngreso_2 = QtGui.QLabel(Form)
        self.lblIngreso_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblIngreso_2.setFont(font)
        self.lblIngreso_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblIngreso_2.setObjectName(_fromUtf8("lblIngreso_2"))
        self.horizontalLayout_3.addWidget(self.lblIngreso_2)
        self.txtIngreso = QtGui.QTextEdit(Form)
        self.txtIngreso.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtIngreso.setFont(font)
        self.txtIngreso.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtIngreso.setReadOnly(True)
        self.txtIngreso.setOverwriteMode(False)
        self.txtIngreso.setObjectName(_fromUtf8("txtIngreso"))
        self.horizontalLayout_3.addWidget(self.txtIngreso)
        spacerItem2 = QtGui.QSpacerItem(513, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        spacerItem3 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem3)
        self.lblIDPaciente = QtGui.QLabel(Form)
        self.lblIDPaciente.setMaximumSize(QtCore.QSize(16777215, 26))
        self.lblIDPaciente.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblIDPaciente.setObjectName(_fromUtf8("lblIDPaciente"))
        self.horizontalLayout_21.addWidget(self.lblIDPaciente)
        self.txtIDPaciente = QtGui.QTextEdit(Form)
        self.txtIDPaciente.setMaximumSize(QtCore.QSize(200, 26))
        self.txtIDPaciente.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtIDPaciente.setReadOnly(True)
        self.txtIDPaciente.setObjectName(_fromUtf8("txtIDPaciente"))
        self.horizontalLayout_21.addWidget(self.txtIDPaciente)
        spacerItem4 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem4)
        self.lblCentroAtencion = QtGui.QLabel(Form)
        self.lblCentroAtencion.setMaximumSize(QtCore.QSize(16777215, 26))
        self.lblCentroAtencion.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblCentroAtencion.setObjectName(_fromUtf8("lblCentroAtencion"))
        self.horizontalLayout_21.addWidget(self.lblCentroAtencion)
        self.txtPacienteNombre = QtGui.QTextEdit(Form)
        self.txtPacienteNombre.setMaximumSize(QtCore.QSize(289, 26))
        self.txtPacienteNombre.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtPacienteNombre.setReadOnly(True)
        self.txtPacienteNombre.setObjectName(_fromUtf8("txtPacienteNombre"))
        self.horizontalLayout_21.addWidget(self.txtPacienteNombre)
        self.verticalLayout_11.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblFechaNacimiento = QtGui.QLabel(Form)
        self.lblFechaNacimiento.setMaximumSize(QtCore.QSize(16777215, 26))
        self.lblFechaNacimiento.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblFechaNacimiento.setObjectName(_fromUtf8("lblFechaNacimiento"))
        self.horizontalLayout_2.addWidget(self.lblFechaNacimiento)
        self.txtFechaNacimiento = QtGui.QTextEdit(Form)
        self.txtFechaNacimiento.setMaximumSize(QtCore.QSize(200, 26))
        self.txtFechaNacimiento.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtFechaNacimiento.setReadOnly(True)
        self.txtFechaNacimiento.setObjectName(_fromUtf8("txtFechaNacimiento"))
        self.horizontalLayout_2.addWidget(self.txtFechaNacimiento)
        spacerItem5 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.lblTipoIngreso = QtGui.QLabel(Form)
        self.lblTipoIngreso.setMinimumSize(QtCore.QSize(0, 26))
        self.lblTipoIngreso.setMaximumSize(QtCore.QSize(16777215, 26))
        self.lblTipoIngreso.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblTipoIngreso.setObjectName(_fromUtf8("lblTipoIngreso"))
        self.horizontalLayout_2.addWidget(self.lblTipoIngreso)
        self.cmbTipoIngreso = QtGui.QComboBox(Form)
        self.cmbTipoIngreso.setMinimumSize(QtCore.QSize(289, 0))
        self.cmbTipoIngreso.setMaximumSize(QtCore.QSize(289, 26))
        self.cmbTipoIngreso.setEditable(False)
        self.cmbTipoIngreso.setFrame(False)
        self.cmbTipoIngreso.setObjectName(_fromUtf8("cmbTipoIngreso"))
        self.horizontalLayout_2.addWidget(self.cmbTipoIngreso)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.lblFechaIngreso = QtGui.QLabel(Form)
        self.lblFechaIngreso.setMaximumSize(QtCore.QSize(150, 26))
        self.lblFechaIngreso.setSizeIncrement(QtCore.QSize(0, 0))
        self.lblFechaIngreso.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblFechaIngreso.setObjectName(_fromUtf8("lblFechaIngreso"))
        self.horizontalLayout_23.addWidget(self.lblFechaIngreso)
        self.txtFechaIngreso = QtGui.QTextEdit(Form)
        self.txtFechaIngreso.setMaximumSize(QtCore.QSize(200, 26))
        self.txtFechaIngreso.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtFechaIngreso.setReadOnly(True)
        self.txtFechaIngreso.setObjectName(_fromUtf8("txtFechaIngreso"))
        self.horizontalLayout_23.addWidget(self.txtFechaIngreso)
        spacerItem6 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem6)
        self.lblHoraIngreso = QtGui.QLabel(Form)
        self.lblHoraIngreso.setMaximumSize(QtCore.QSize(150, 26))
        self.lblHoraIngreso.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblHoraIngreso.setObjectName(_fromUtf8("lblHoraIngreso"))
        self.horizontalLayout_23.addWidget(self.lblHoraIngreso)
        self.txtHoraIngreso = QtGui.QTextEdit(Form)
        self.txtHoraIngreso.setMaximumSize(QtCore.QSize(200, 26))
        self.txtHoraIngreso.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtHoraIngreso.setReadOnly(True)
        self.txtHoraIngreso.setObjectName(_fromUtf8("txtHoraIngreso"))
        self.horizontalLayout_23.addWidget(self.txtHoraIngreso)
        spacerItem7 = QtGui.QSpacerItem(89, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        spacerItem8 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem8)
        self.lblFechaEgreso = QtGui.QLabel(Form)
        self.lblFechaEgreso.setMaximumSize(QtCore.QSize(157, 26))
        self.lblFechaEgreso.setSizeIncrement(QtCore.QSize(0, 0))
        self.lblFechaEgreso.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblFechaEgreso.setObjectName(_fromUtf8("lblFechaEgreso"))
        self.horizontalLayout_22.addWidget(self.lblFechaEgreso)
        self.fechaEgreso = QtGui.QDateEdit(Form)
        self.fechaEgreso.setMinimumSize(QtCore.QSize(180, 26))
        self.fechaEgreso.setMaximumSize(QtCore.QSize(16777215, 26))
        self.fechaEgreso.setFrame(False)
        self.fechaEgreso.setCalendarPopup(True)
        self.fechaEgreso.setObjectName(_fromUtf8("fechaEgreso"))
        self.horizontalLayout_22.addWidget(self.fechaEgreso)
        spacerItem9 = QtGui.QSpacerItem(95, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem9)
        self.lblHoraEgreso = QtGui.QLabel(Form)
        self.lblHoraEgreso.setMaximumSize(QtCore.QSize(150, 26))
        self.lblHoraEgreso.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblHoraEgreso.setObjectName(_fromUtf8("lblHoraEgreso"))
        self.horizontalLayout_22.addWidget(self.lblHoraEgreso)
        self.horaEgreso = QtGui.QTimeEdit(Form)
        self.horaEgreso.setEnabled(True)
        self.horaEgreso.setMinimumSize(QtCore.QSize(175, 0))
        self.horaEgreso.setMaximumSize(QtCore.QSize(16777215, 26))
        self.horaEgreso.setFrame(False)
        self.horaEgreso.setObjectName(_fromUtf8("horaEgreso"))
        self.horizontalLayout_22.addWidget(self.horaEgreso)
        spacerItem10 = QtGui.QSpacerItem(112, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem10)
        self.verticalLayout_11.addLayout(self.horizontalLayout_22)
        spacerItem11 = QtGui.QSpacerItem(40, 4, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem11)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblObservaciones = QtGui.QLabel(Form)
        self.lblObservaciones.setMaximumSize(QtCore.QSize(150, 26))
        self.lblObservaciones.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblObservaciones.setObjectName(_fromUtf8("lblObservaciones"))
        self.horizontalLayout.addWidget(self.lblObservaciones)
        self.txtObservaciones = QtGui.QPlainTextEdit(Form)
        self.txtObservaciones.setMaximumSize(QtCore.QSize(500, 60))
        self.txtObservaciones.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtObservaciones.setObjectName(_fromUtf8("txtObservaciones"))
        self.horizontalLayout.addWidget(self.txtObservaciones)
        spacerItem12 = QtGui.QSpacerItem(165, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        spacerItem13 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem13)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.btnEnviar = QtGui.QPushButton(Form)
        self.btnEnviar.setObjectName(_fromUtf8("btnEnviar"))
        self.horizontalLayout_4.addWidget(self.btnEnviar)
        self.btnCancelar = QtGui.QPushButton(Form)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_4.addWidget(self.btnCancelar)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addLayout(self.verticalLayout_11)
        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.retranslateUi(Form, idIngreso)
        QtCore.QObject.connect(self.btnEnviar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actualizar_ingreso)
        QtCore.QObject.connect(self.tblPacientes, QtCore.SIGNAL(_fromUtf8("itemSelectionChanged()")),
                               self.paciente_row_was_clicked)
        QtCore.QObject.connect(self.btnCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self = frm_formato.center(self)

    def retranslateUi(self, Form, idIngreso):
        Form.setWindowTitle(_translate("Form", "Editar Ingreso", None))
        self.lblPacientes.setText(_translate("Form", "Pacientes", None))
        item = self.tblPacientes.horizontalHeaderItem(0)
        item.setText(_translate("Form", "idPaciente", None))
        item = self.tblPacientes.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Paciente", None))
        item = self.tblPacientes.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Fecha Nacimiento", None))
        self.lblIngreso_2.setText(_translate("Form", "Ingreso:", None))
        self.txtIngreso.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt;\"><br /></p></body></html>",
                                           None))
        self.lblIDPaciente.setText(_translate("Form", "ID Paciente:", None))
        self.lblCentroAtencion.setText(_translate("Form", "Paciente:", None))
        self.lblFechaNacimiento.setText(_translate("Form", "Fecha Nacimiento:", None))
        self.lblTipoIngreso.setText(_translate("Form", "Tipo de Ingreso:", None))
        self.lblFechaIngreso.setText(_translate("Form", "Fecha Ingreso: ", None))
        self.lblHoraIngreso.setText(_translate("Form", "  Hora Ingreso: ", None))
        self.lblFechaEgreso.setText(_translate("Form", "Fecha Egreso:", None))
        self.lblHoraEgreso.setText(_translate("Form", "  Hora Egreso:", None))
        self.horaEgreso.setDisplayFormat(_translate("Form", "h:mm ", None))
        self.lblObservaciones.setText(_translate("Form", "Observaciones:", None))
        self.btnEnviar.setText(_translate("Form", "Enviar", None))
        self.btnCancelar.setText(_translate("Form", "Cancelar", None))
        self.txtIngreso.setText(idIngreso)
        self.lista_pacientes()
        self.lista_tipo_ingresos()
        self.datos_paciente()

    def lista_pacientes(self):
        datos = get(entidad="Paciente")
        self.tblPacientes.setRowCount(len(datos))
        IDingreso = str(self.txtIngreso.toPlainText())
        i = 0
        for elemento in datos:
            self.tblPacientes.setItem(i, 0, QtGui.QTableWidgetItem(str(elemento['idPaciente'])))
            self.tblPacientes.setItem(i, 1, QtGui.QTableWidgetItem(elemento['nombres'] + " " + elemento['apellidos']))
            self.tblPacientes.setItem(i, 2, QtGui.QTableWidgetItem(elemento['fechaNacimiento']))
            i += 1

    def datos_paciente(self):
        IDingreso = str(self.txtIngreso.toPlainText())
        url = "Ingreso" + "/" + str(IDingreso)
        datos = get(url)

        self.txtIDPaciente.setText(str(datos['idPaciente']['idPaciente']))
        self.txtPacienteNombre.setText(
            datos['idPaciente']['nombres'] + " " + datos['idPaciente']['apellidos'])
        self.txtFechaNacimiento.setText(datos['idPaciente']['fechaNacimiento'])
        self.txtFechaIngreso.setText(datos['fechaIngreso'])
        self.txtHoraIngreso.setText(datos['horaIngreso'])
        if datos.get('observaciones') != None:
            self.txtObservaciones.setPlainText(datos['observaciones'])
        if datos.get('fechaEgreso') != None:
            fecha = datos['fechaEgreso']
            fecha = formato.set_date(fecha)
            self.fechaEgreso.setDateTime(fecha)

        if datos.get('horaEgreso') != None:
            hora = datos['horaEgreso']
            hora = formato.set_hora(hora)
            self.horaEgreso.setDateTime(hora)

        tipo = datos['idTipoIngreso']['nombre']
        id_tipo = "0"
        for x in self.lista_tipo_ingreso:
            if x['nombre'] == tipo:
                id_tipo = x['idTipoIngreso']
                self.cmbTipoIngreso.setCurrentIndex(id_tipo - 1)

    def lista_tipo_ingresos(self):
        IDingreso = str(self.txtIngreso.toPlainText())
        print("Desde tipo ingresos", str(IDingreso))
        datos = get(entidad="TipoIngreso")
        self.lista_tipo_ingreso = datos
        i = 0
        for elemento in datos:
            self.cmbTipoIngreso.addItem(elemento['nombre'])
            i += 1
        self.idIngreso = str(self.txtIngreso.toPlainText())

    def paciente_row_was_clicked(self):
        self.limpiar_paciente()
        row = self.tblPacientes.currentRow()
        if row != -1:
            item = self.tblPacientes.item(row, 0)
            self.txtIDPaciente.setText(item.text())
            item = self.tblPacientes.item(row, 1)
            self.txtPacienteNombre.setText(item.text())
            item = self.tblPacientes.item(row, 2)
            self.txtFechaNacimiento.setText(item.text())

    def limpiar_paciente(self):
        self.txtIDPaciente.setText("")
        self.txtPacienteNombre.setText("")
        self.txtFechaNacimiento.setText("")

    def actualizar_ingreso(self):
        # PARA PUT DE INGRESO
        idIngreso = self.txtIngreso.toPlainText()
        # 1-FIND BY ID PACIENTE Y LUEGO GENERO EL JSON RESPECTIVO
        entidad = "Paciente"
        row = self.tblPacientes.currentRow()
        id = str(self.tblPacientes.item(row, 0).text())
        responsePaciente = recurso.get(entidad + "/" + id)
        dataPaciente = jsonFormato.deserializar(responsePaciente)

        # 2-FIND BY ID TIPO INGRESO Y LUEGO GENERO EL JSON RESPECTIVO
        entidad = "TipoIngreso"
        tipo = self.cmbTipoIngreso.currentText()
        id_tipo = "0"
        for x in self.lista_tipo_ingreso:
            if x['nombre'] == tipo:
                id_tipo = str(x['idTipoIngreso'])
        responseTipoIngreso = recurso.get(entidad + "/" + id_tipo)
        dataTipoIngreso = jsonFormato.deserializar(responseTipoIngreso)

        # 3-ESTABLECER FECHAS Y HORAS
        # FECHA INGRESO
        fechaIng = self.txtFechaIngreso.toPlainText()
        fechaIng = formato.fecha_texto_plano_formato(fechaIng)

        # HORA INGRESO
        horaIng = self.txtHoraIngreso.toPlainText()
        horaIng = formato.hora_texto_plano_formato(horaIng)

        # FECHA EGRESO
        fechaEgr = self.fechaEgreso.dateTime().toPyDateTime()
        fechaEgr = formato.fecha_date_edit_formato(fechaEgr)

        # HORA EGRESO
        horaEgr = self.horaEgreso.dateTime().toPyDateTime()
        horaEgr = formato.hora_date_edit_formato(horaEgr)
        # 4 - OBSERVACIONES
        observaciones = self.txtObservaciones.toPlainText()
        # 5 - SERIALIZAR A JSON
        json_base = {}
        json_base["fechaIngreso"] = fechaIng
        json_base["horaIngreso"] = horaIng
        json_base["fechaEgreso"] = fechaEgr
        json_base["horaEgreso"] = horaEgr
        json_base["idPaciente"] = dataPaciente
        json_base["idTipoIngreso"] = dataTipoIngreso
        json_base["observaciones"] = observaciones
        json_base["idIngreso"] = idIngreso
        jsonVar = jsonFormato.serializar(json_base)
        entidad = "Ingreso"
        response = recurso.put(entidad, jsonVar)
        self.close()


def get(entidad):
    response = recurso.get(entidad)
    data = jsonFormato.deserializar(response)
    return data


def put(entidad, payload):
    response = recurso.put(entidad, payload)
    print(response)
