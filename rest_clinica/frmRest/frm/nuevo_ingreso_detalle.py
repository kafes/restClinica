from PyQt4 import QtCore, QtGui
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


class Ui_NuevoDetalleIngreso(object):
    def setupUi(self, Form, idIngreso):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(641, 508)
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lblAPCA_2 = QtGui.QLabel(Form)
        self.lblAPCA_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAPCA_2.setObjectName(_fromUtf8("lblAPCA_2"))
        self.verticalLayout_5.addWidget(self.lblAPCA_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.tblAPCA_2 = QtGui.QTableWidget(Form)
        self.tblAPCA_2.setMinimumSize(QtCore.QSize(450, 0))
        self.tblAPCA_2.setMaximumSize(QtCore.QSize(5000, 400))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tblAPCA_2.setFont(font)
        self.tblAPCA_2.setFrameShape(QtGui.QFrame.Box)
        self.tblAPCA_2.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblAPCA_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblAPCA_2.setCornerButtonEnabled(False)
        self.tblAPCA_2.setObjectName(_fromUtf8("tblAPCA_2"))
        self.tblAPCA_2.setColumnCount(6)
        self.tblAPCA_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblAPCA_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblAPCA_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblAPCA_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblAPCA_2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblAPCA_2.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tblAPCA_2.setHorizontalHeaderItem(5, item)
        self.tblAPCA_2.horizontalHeader().setDefaultSectionSize(168)
        self.tblAPCA_2.horizontalHeader().setHighlightSections(False)
        self.tblAPCA_2.verticalHeader().setVisible(False)
        self.tblAPCA_2.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_4.addWidget(self.tblAPCA_2)
        spacerItem1 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.lblIngreso = QtGui.QLabel(Form)
        self.lblIngreso.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblIngreso.setFont(font)
        self.lblIngreso.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblIngreso.setObjectName(_fromUtf8("lblIngreso"))
        self.horizontalLayout_11.addWidget(self.lblIngreso)
        self.txtIngresoDetalle = QtGui.QTextEdit(Form)
        self.txtIngresoDetalle.setMaximumSize(QtCore.QSize(190, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtIngresoDetalle.setFont(font)
        self.txtIngresoDetalle.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtIngresoDetalle.setReadOnly(True)
        self.txtIngresoDetalle.setObjectName(_fromUtf8("txtIngresoDetalle"))
        self.horizontalLayout_11.addWidget(self.txtIngresoDetalle)
        self.lblDoctor = QtGui.QLabel(Form)
        self.lblDoctor.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblDoctor.setFont(font)
        self.lblDoctor.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblDoctor.setObjectName(_fromUtf8("lblDoctor"))
        self.horizontalLayout_11.addWidget(self.lblDoctor)
        self.txtPersonal = QtGui.QTextEdit(Form)
        self.txtPersonal.setMaximumSize(QtCore.QSize(300, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtPersonal.setFont(font)
        self.txtPersonal.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtPersonal.setReadOnly(True)
        self.txtPersonal.setObjectName(_fromUtf8("txtPersonal"))
        self.horizontalLayout_11.addWidget(self.txtPersonal)
        self.verticalLayout_16.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.lblArea = QtGui.QLabel(Form)
        self.lblArea.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblArea.setFont(font)
        self.lblArea.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblArea.setObjectName(_fromUtf8("lblArea"))
        self.horizontalLayout_10.addWidget(self.lblArea)
        self.txtArea = QtGui.QTextEdit(Form)
        self.txtArea.setMaximumSize(QtCore.QSize(190, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtArea.setFont(font)
        self.txtArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtArea.setReadOnly(True)
        self.txtArea.setObjectName(_fromUtf8("txtArea"))
        self.horizontalLayout_10.addWidget(self.txtArea)
        self.lblCentro = QtGui.QLabel(Form)
        self.lblCentro.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblCentro.setFont(font)
        self.lblCentro.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblCentro.setObjectName(_fromUtf8("lblCentro"))
        self.horizontalLayout_10.addWidget(self.lblCentro)
        self.txtCentro = QtGui.QTextEdit(Form)
        self.txtCentro.setMaximumSize(QtCore.QSize(300, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtCentro.setFont(font)
        self.txtCentro.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtCentro.setReadOnly(True)
        self.txtCentro.setObjectName(_fromUtf8("txtCentro"))
        self.horizontalLayout_10.addWidget(self.txtCentro)
        self.verticalLayout_16.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lblFechaDetalle = QtGui.QLabel(Form)
        self.lblFechaDetalle.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lblFechaDetalle.setFont(font)
        self.lblFechaDetalle.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblFechaDetalle.setObjectName(_fromUtf8("lblFechaDetalle"))
        self.horizontalLayout_6.addWidget(self.lblFechaDetalle)
        self.fechaDetalle = QtGui.QDateEdit(Form)
        self.fechaDetalle.setMinimumSize(QtCore.QSize(170, 26))
        self.fechaDetalle.setMaximumSize(QtCore.QSize(180, 26))
        self.fechaDetalle.setFrame(False)
        self.fechaDetalle.setCalendarPopup(True)
        self.fechaDetalle.setObjectName(_fromUtf8("fechaDetalle"))
        self.horizontalLayout_6.addWidget(self.fechaDetalle)
        spacerItem3 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.lblHoraDetalle = QtGui.QLabel(Form)
        self.lblHoraDetalle.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblHoraDetalle.setObjectName(_fromUtf8("lblHoraDetalle"))
        self.horizontalLayout_6.addWidget(self.lblHoraDetalle)
        self.horaDetalle = QtGui.QTimeEdit(Form)
        self.horaDetalle.setMinimumSize(QtCore.QSize(170, 26))
        self.horaDetalle.setMaximumSize(QtCore.QSize(180, 26))
        self.horaDetalle.setFrame(False)
        self.horaDetalle.setCalendarPopup(True)
        self.horaDetalle.setObjectName(_fromUtf8("horaDetalle"))
        self.horizontalLayout_6.addWidget(self.horaDetalle)
        self.verticalLayout_16.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_16)
        spacerItem4 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblObservaciones = QtGui.QLabel(Form)
        self.lblObservaciones.setMaximumSize(QtCore.QSize(141, 26))
        self.lblObservaciones.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblObservaciones.setObjectName(_fromUtf8("lblObservaciones"))
        self.horizontalLayout_2.addWidget(self.lblObservaciones)
        self.txtObservaciones = QtGui.QPlainTextEdit(Form)
        self.txtObservaciones.setMaximumSize(QtCore.QSize(500, 60))
        self.txtObservaciones.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtObservaciones.setObjectName(_fromUtf8("txtObservaciones"))
        self.horizontalLayout_2.addWidget(self.txtObservaciones)
        spacerItem5 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.btnEnviar = QtGui.QPushButton(Form)
        self.btnEnviar.setObjectName(_fromUtf8("btnEnviar"))
        self.horizontalLayout.addWidget(self.btnEnviar)
        self.btnCancelar = QtGui.QPushButton(Form)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout.addWidget(self.btnCancelar)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form, idIngreso)
        QtCore.QObject.connect(self.tblAPCA_2, QtCore.SIGNAL(_fromUtf8("itemSelectionChanged()")),
                               self.apca_row_was_clicked)
        QtCore.QObject.connect(self.btnEnviar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.crear_ingreso_detalle)
        QtCore.QObject.connect(self.btnCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.tblAPCA_2.setColumnHidden(3, True)
        self.tblAPCA_2.setColumnHidden(4, True)
        self.tblAPCA_2.setColumnHidden(5, True)
        self = frm_formato.center(self)

    def retranslateUi(self, Form, idIngreso):
        Form.setWindowTitle(_translate("Form", "Nuevo Ingreso Detalle", None))
        self.lblAPCA_2.setText(_translate("Form", "APCA", None))
        item = self.tblAPCA_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Area", None))
        item = self.tblAPCA_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Centro", None))
        item = self.tblAPCA_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Personal", None))
        item = self.tblAPCA_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "idAreaCentroEspacio", None))
        item = self.tblAPCA_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "idAsignacionPersonalCentroArea", None))
        item = self.tblAPCA_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "idTurno", None))
        self.lblIngreso.setText(_translate("Form", "Ingreso:", None))
        self.lblDoctor.setText(_translate("Form", "Personal:", None))
        self.lblArea.setText(_translate("Form", "Area:", None))
        self.lblCentro.setText(_translate("Form", "Centro:", None))
        self.lblFechaDetalle.setText(_translate("Form", "Fecha Detalle:", None))
        self.lblHoraDetalle.setText(_translate("Form", "Hora Detalle:", None))
        self.horaDetalle.setDisplayFormat(_translate("Form", "h:mm ", None))
        self.lblObservaciones.setText(_translate("Form", "Observaciones:", None))
        self.btnEnviar.setText(_translate("Form", "Enviar", None))
        self.btnCancelar.setText(_translate("Form", "Cancelar", None))
        self.txtIngresoDetalle.setText(str(idIngreso))
        self.refrescar_APCA()

    def refrescar_APCA(self):
        entidad = "AsignacionPersonalCentroAreaEspacio"
        datos = get(entidad)
        self.tblAPCA_2.setRowCount(len(datos))
        i = 0
        for elemento in datos:
            self.tblAPCA_2.setItem(i, 0, QtGui.QTableWidgetItem(
                elemento['asignacionPersonalCentroArea']['idAreaCentro']['idArea']['nombre']))
            self.tblAPCA_2.setItem(i, 1, QtGui.QTableWidgetItem(
                elemento['asignacionPersonalCentroArea']['idAreaCentro'][
                    'idCentro']['nombreCorto']))
            self.tblAPCA_2.setItem(i, 2, QtGui.QTableWidgetItem(
                elemento['asignacionPersonalCentroArea']['idPersonal']['nombres'] + " " +
                elemento['asignacionPersonalCentroArea']['idPersonal']['apellidos']))
            self.tblAPCA_2.setItem(i, 3, QtGui.QTableWidgetItem(
                str(elemento['asignacionPersonalCentroAreaEspacioPK']['idAreaCentroEspacio'])))
            self.tblAPCA_2.setItem(i, 4, QtGui.QTableWidgetItem(
                str(elemento['asignacionPersonalCentroAreaEspacioPK']['idAsignacionPersonalCentroArea'])))
            self.tblAPCA_2.setItem(i, 5, QtGui.QTableWidgetItem(
                str(elemento['asignacionPersonalCentroAreaEspacioPK']['idTurno'])))
            i += 1

    def apca_row_was_clicked(self):
        self.limpiar_apca()
        row = self.tblAPCA_2.currentRow()
        if row != -1:
            item = self.tblAPCA_2.item(row, 0)
            self.txtArea.setText(item.text())
            item = self.tblAPCA_2.item(row, 1)
            self.txtCentro.setText(item.text())
            item = self.tblAPCA_2.item(row, 2)
            self.txtPersonal.setText(item.text())

    def crear_ingreso_detalle(self):
        # 1 - ESTABLECER ASIGNACION_PERSONAL_CENTRO_AREA_ESPACIO
        entidad = "AsignacionPersonalCentroAreaEspacio"
        row = self.tblAPCA_2.currentRow()
        idACE = str(self.tblAPCA_2.item(row, 3).text())
        idAPCA = str(self.tblAPCA_2.item(row, 4).text())
        idTurno = str(self.tblAPCA_2.item(row, 5).text())
        responseAPCAE = recurso.get(entidad + "/" + idAPCA + "/" + idACE + "/" + idTurno)
        dataAPCAE = jsonFormato.deserializar(responseAPCAE)

        # 2 - ESTBLECER INGRESO
        entidad = "Ingreso"
        idIngreso = str(self.txtIngresoDetalle.toPlainText())
        responseIngreso = recurso.get(entidad + "/" + idIngreso)
        dataIngreso = jsonFormato.deserializar(responseIngreso)

        # 3 - ESTABLECER FECHAS Y HORAS
        fechaDet = self.fechaDetalle.dateTime().toPyDateTime()
        fechaDet = formato.fecha_date_edit_formato(fechaDet)
        horaDet = self.horaDetalle.dateTime().toPyDateTime()
        horaDet = formato.hora_date_edit_formato(horaDet)

        # 4 - OBTENER OBSERVACIONES
        observaciones = self.txtObservaciones.toPlainText()

        # 5 - SERIALIZAR A JSON
        json_base = {}
        json_base["asignacionPersonalCentroAreaEspacio"] = dataAPCAE
        json_base["ingreso"] = dataIngreso
        json_base["fechaDetalle"] = fechaDet
        json_base["horaDetalle"] = horaDet
        json_base["ingresoDetallePK"] = dict(idIngreso=idIngreso, idAreaCentroEspacio=idACE,
                                             idAsignacionPersonalCentroArea=idAPCA, idTurno=idTurno)
        json_base["observaciones"] = observaciones
        jsonVar = jsonFormato.serializar(json_base)

        # 5 - HACER POST
        entidad = "IngresoDetalle"
        response = recurso.post(entidad, jsonVar)
        self.close()

    def limpiar_apca(self):
        self.txtArea.setText("")
        self.txtCentro.setText("")
        self.txtPersonal.setText("")


def get(entidad):
    response = recurso.get(entidad)
    data = jsonFormato.deserializar(response)
    return data
