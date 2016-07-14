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


class Ui_EditarIngresoDetalle(object):
    def setupUi(self, Form, id_ingreso, id_apca, id_turno, id_ace):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(857, 243)
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        self.id_ace = id_ace
        self.id_apca = id_apca
        self.id_turno = id_turno
        self.id_ingreso = id_ingreso
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
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
        self.txtIngresoDetalle.setMaximumSize(QtCore.QSize(250, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtIngresoDetalle.setFont(font)
        self.txtIngresoDetalle.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtIngresoDetalle.setReadOnly(True)
        self.txtIngresoDetalle.setObjectName(_fromUtf8("txtIngresoDetalle"))
        self.horizontalLayout_11.addWidget(self.txtIngresoDetalle)
        spacerItem = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
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
        self.txtArea.setMaximumSize(QtCore.QSize(250, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtArea.setFont(font)
        self.txtArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtArea.setReadOnly(True)
        self.txtArea.setObjectName(_fromUtf8("txtArea"))
        self.horizontalLayout_10.addWidget(self.txtArea)
        spacerItem1 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
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
        self.fechaDetalle.setMinimumSize(QtCore.QSize(200, 26))
        self.fechaDetalle.setMaximumSize(QtCore.QSize(600, 26))
        self.fechaDetalle.setFrame(False)
        self.fechaDetalle.setCalendarPopup(True)
        self.fechaDetalle.setObjectName(_fromUtf8("fechaDetalle"))
        self.horizontalLayout_6.addWidget(self.fechaDetalle)
        spacerItem2 = QtGui.QSpacerItem(150, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.lblHoraDetalle = QtGui.QLabel(Form)
        self.lblHoraDetalle.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblHoraDetalle.setObjectName(_fromUtf8("lblHoraDetalle"))
        self.horizontalLayout_6.addWidget(self.lblHoraDetalle)
        self.horaDetalle = QtGui.QTimeEdit(Form)
        self.horaDetalle.setMinimumSize(QtCore.QSize(200, 26))
        self.horaDetalle.setMaximumSize(QtCore.QSize(600, 26))
        self.horaDetalle.setFrame(False)
        self.horaDetalle.setObjectName(_fromUtf8("horaDetalle"))
        self.horizontalLayout_6.addWidget(self.horaDetalle)
        spacerItem3 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_16.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_16)
        spacerItem4 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblObservaciones = QtGui.QLabel(Form)
        self.lblObservaciones.setMaximumSize(QtCore.QSize(150, 26))
        self.lblObservaciones.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblObservaciones.setObjectName(_fromUtf8("lblObservaciones"))
        self.horizontalLayout_2.addWidget(self.lblObservaciones)
        self.txtObservaciones = QtGui.QPlainTextEdit(Form)
        self.txtObservaciones.setMaximumSize(QtCore.QSize(500, 60))
        self.txtObservaciones.setFrameShape(QtGui.QFrame.NoFrame)
        self.txtObservaciones.setObjectName(_fromUtf8("txtObservaciones"))
        self.horizontalLayout_2.addWidget(self.txtObservaciones)
        spacerItem5 = QtGui.QSpacerItem(160, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtGui.QSpacerItem(40, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem6)
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
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btnEnviar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actualizar_ingreso_detalle)
        QtCore.QObject.connect(self.btnCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self = frm_formato.center(self)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Editar Ingreso Detalle", None))
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
        self.datos_ingreso_detalle()

    def datos_ingreso_detalle(self):
        self.txtIngresoDetalle.setText(str(self.id_ingreso))
        entidad = "IngresoDetalle"
        responseIngreso = recurso.get(
            entidad + "/" + str(self.id_ingreso) + "/" + str(self.id_apca) + "/" + str(self.id_ace) + "/" + str(
                self.id_turno))
        responseIngreso = jsonFormato.deserializar(responseIngreso)
        self.txtArea.setText(
            responseIngreso['asignacionPersonalCentroAreaEspacio']['asignacionPersonalCentroArea']['idAreaCentro'][
                'idArea']['nombre'])
        self.txtCentro.setText(
            responseIngreso['asignacionPersonalCentroAreaEspacio']['asignacionPersonalCentroArea']['idAreaCentro'][
                'idCentro']['nombreCorto'])
        self.txtPersonal.setText(
            responseIngreso['asignacionPersonalCentroAreaEspacio']['asignacionPersonalCentroArea']['idPersonal'][
                'nombres'] + " " +
            responseIngreso['asignacionPersonalCentroAreaEspacio']['asignacionPersonalCentroArea']['idPersonal'][
                'apellidos'])
        if responseIngreso.get('observaciones') != None:
            self.txtObservaciones.setPlainText(responseIngreso['observaciones'])
        if responseIngreso.get('fechaDetalle') != None:
            fecha = responseIngreso['fechaDetalle']
            fecha = formato.set_date(fecha)
            self.fechaDetalle.setDateTime(fecha)
        if responseIngreso.get('horaDetalle') != None:
            hora = responseIngreso['horaDetalle']
            hora = formato.set_hora(hora)
            self.horaDetalle.setDateTime(hora)

    def actualizar_ingreso_detalle(self):
        # 1 - ESTABLECER ASIGNACION_PERSONAL_CENTRO_AREA_ESPACIO
        entidad = "AsignacionPersonalCentroAreaEspacio"
        responseAPCAE = recurso.get(
            entidad + "/" + str(self.id_apca) + "/" + str(self.id_ace) + "/" + str(self.id_turno))
        dataAPCAE = jsonFormato.deserializar(responseAPCAE)
        # 2 - ESTALECER INGRESO
        entidad = "Ingreso"
        idIngreso = str(self.txtIngresoDetalle.toPlainText())
        responseIngreso = recurso.get(entidad + "/" + str(self.id_ingreso))
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
        json_base["ingresoDetallePK"] = dict(idIngreso=str(self.id_ingreso), idAreaCentroEspacio=str(self.id_ace),
                                             idAsignacionPersonalCentroArea=str(self.id_apca),
                                             idTurno=str(self.id_turno))
        json_base["observaciones"] = observaciones
        jsonVar = jsonFormato.serializar(json_base)
        # 5 - HACER PUT
        entidad = "IngresoDetalle"
        response = recurso.put(entidad, jsonVar)
        self.close()
