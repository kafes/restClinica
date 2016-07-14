from PyQt4 import QtGui
from jsonFormato import json_formato
import datetime

jsonFormato = json_formato()


class frm_formato:
    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def fecha_texto_plano_formato(self, fecha):
        fecha = jsonFormato.serializar_datetime(
            datetime.datetime(year=int(fecha[0:4]), month=int(fecha[5:7]), day=int(fecha[8:10])))
        fecha = fecha[1:-1]
        return fecha

    def hora_texto_plano_formato(self, hora):
        hora = jsonFormato.serializar_datetime(
            datetime.datetime(2000, 1, 1, hour=int(hora[11:13]), minute=int(hora[14:16]), second=int(hora[17:19])))
        hora = hora[1:-1]
        return hora

    def fecha_date_edit_formato(self, fecha):
        fecha = jsonFormato.serializar_datetime(fecha)
        fecha = fecha[1:-1]
        fecha = jsonFormato.serializar_datetime(
            datetime.datetime(year=int(fecha[0:4]), month=int(fecha[5:7]), day=int(fecha[8:10]) + 1))
        fecha = fecha[1:-1]
        return fecha

    def hora_date_edit_formato(self, hora):
        hora = jsonFormato.serializar_datetime(hora)
        hora = hora[1:-1]
        hora = jsonFormato.serializar_datetime(
            datetime.datetime(2000, 1, 1, hour=int(hora[11:13]) + 6, minute=int(hora[14:16]), second=int(hora[17:19])))
        hora = hora[1:-1]
        return hora

    def set_date(self, fecha):
        y = int(fecha[0:4])
        m = int(fecha[5:7])
        d = int(fecha[8:10])
        return datetime.datetime(year=y, month=m, day=d)

    def set_hora(self, hora):
        h = int(hora[11:13])
        mi = int(hora[14:16])
        s = int(hora[17:19])
        return datetime.datetime(2000, 1, 1, hour=h, minute=mi, second=s)