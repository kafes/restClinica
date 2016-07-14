from PyQt4 import QtGui
from frm.frmIngresoNuevo import Ui_FormIngresoDetalle
from frm.frmPrincipal import Ui_MainWindow
from frm.editar_ingreso import Ui_FormEditarIngreso
from frm.nuevo_ingreso_detalle import Ui_NuevoDetalleIngreso
from frm.editar_ingreso_detalle import Ui_EditarIngresoDetalle


class frmPrincipal(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.btnNuevoIngreso.clicked.connect(self.btnNuevo_ingreso_was_clicked)
        self.btnEditarIngreso.clicked.connect(self.btnEditar_ingreso_was_clicked)
        self.btnNuevoIngresoDetalle.clicked.connect(self.btnNuevo_ingreso_detalle_was_clicked)
        self.btnEditarIngresoDetalle.clicked.connect(self.btnEditar_ingreso_detalle_was_clicked)

    def btnNuevo_ingreso_was_clicked(self):
        self.frmIngresoNuevo = frmNuevoIngreso()
        self.frmIngresoNuevo.btnEnviar.clicked.connect(self.refrescar_ingresos)
        self.frmIngresoNuevo.show()

    def btnEditar_ingreso_was_clicked(self):
        row = self.tblIngreso.currentRow()
        item = self.tblIngreso.item(row, 0).text()
        idIngreso = str(item)
        self.editar_ingreso = frmEditarIngreso(idIngreso)
        self.editar_ingreso.btnEnviar.clicked.connect(self.refrescar_ingresos)
        self.editar_ingreso.show()

    def btnNuevo_ingreso_detalle_was_clicked(self):
        row = self.tblIngreso.currentRow()
        item = self.tblIngreso.item(row, 0).text()
        idIngreso = str(item)
        self.nuevo_ingreso_detalle = frmNuevoIngresoDetalle(idIngreso)
        self.nuevo_ingreso_detalle.btnEnviar.clicked.connect(self.refrescar_ingresos_detalles)
        self.nuevo_ingreso_detalle.show()

    def btnEditar_ingreso_detalle_was_clicked(self):
        row = self.tblIngresoDetalle.currentRow()
        item = self.tblIngresoDetalle.item(row, 0).text()
        idIngreso = str(item)
        item = self.tblIngresoDetalle.item(row, 5).text()
        idAPCA = str(item)
        item = self.tblIngresoDetalle.item(row, 6).text()
        idTurno = str(item)
        item = self.tblIngresoDetalle.item(row, 7).text()
        idACE = str(item)

        self.editar_ingreso_detalle = frmEditarIngresoDetalle(idIngreso, idAPCA, idTurno, idACE)
        self.editar_ingreso_detalle.btnEnviar.clicked.connect(self.refrescar_ingresos_detalles)
        self.editar_ingreso_detalle.show()


class frmNuevoIngreso(QtGui.QWidget, Ui_FormIngresoDetalle):
    def __init__(self):
        QtGui.QWidget.__init__(self, None)
        self.setupUi(self)


class frmEditarIngreso(QtGui.QWidget, Ui_FormEditarIngreso):
    def __init__(self, idIngreso):
        QtGui.QWidget.__init__(self, None)
        self.setupUi(self, idIngreso)


class frmNuevoIngresoDetalle(QtGui.QWidget, Ui_NuevoDetalleIngreso):
    def __init__(self, idIngreso ):
        QtGui.QWidget.__init__(self, None)
        self.setupUi(self, idIngreso)


class frmEditarIngresoDetalle(QtGui.QWidget, Ui_EditarIngresoDetalle):
    def __init__(self, idIngreso, idAPCA, idTurno, idACE):
        QtGui.QWidget.__init__(self, None)
        self.setupUi(self, idIngreso, idAPCA, idTurno, idACE)


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = frmPrincipal()
    MainWindow.show()
    sys.exit(app.exec_())
