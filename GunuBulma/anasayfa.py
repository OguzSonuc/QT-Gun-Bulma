# This Python file uses the following encoding: utf-8
import sys
import datetime
from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_anaSayfa

class anaSayfa(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_anaSayfa()
        self.ui.setupUi(self)

        zaman = datetime.datetime.now()
        self.ui.label_b.setText(str(zaman.strftime("%d/%m/%Y_%A")))

        self.ui.pushButton.clicked.connect(self.gunBul)

    def gunBul(self):
        tarih = datetime.datetime(int(self.ui.lineEdit_yil.text()),int(self.ui.lineEdit_ay.text()),int(self.ui.lineEdit_gun.text()))
        self.ui.label_g.setText("Gün: "+ tarih.strftime("%A"))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = anaSayfa()
    widget.show()
    sys.exit(app.exec())
