from PyQt5 import QtCore, QtWidgets, QtSerialPort
start_byte = b'\xaa'
from communication2 import Com
com = Com(baudRate=19200, portName='/dev/ttyUSB0', serialPort=QtSerialPort.QSerialPort())
class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.message_le = QtWidgets.QLineEdit()
        self.send_btn = QtWidgets.QPushButton(
            text="Send",
            clicked=self.send
        )
        self.output_te = QtWidgets.QTextEdit(readOnly=True)
        self.button = QtWidgets.QPushButton(
            text="Connect",
            checkable=True,
            toggled=self.on_toggled
        )
        lay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        hlay.addWidget(self.message_le)
        hlay.addWidget(self.send_btn)
        lay.addLayout(hlay)
        lay.addWidget(self.output_te)
        lay.addWidget(self.button)

        self.serial = com.serial
        self.serial.readyRead.connect(lambda: self.receive())

    @QtCore.pyqtSlot()
    def receive(self):
        print(com.receive())


    @QtCore.pyqtSlot()
    def send(self):
        msg = self.message_le.text()
        com.send(msg)

    @QtCore.pyqtSlot(bool)
    def on_toggled(self, checked):
        com.on_toggled(checked)
        self.button.setText("Disconnect" if checked else "Connect")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())