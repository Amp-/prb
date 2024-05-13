from PyQt6 import QtCore,QtWidgets,QtSerialPort, uic
from PyQt6.QtCore import QIODevice

start_byte = b'\xaa'
class Com:
    @QtCore.pyqtSlot()
    def receive(self):
        #while self.serial.canReadLine():
            #text = self.serial.readLine().data()#.decode()
            text = self.serial.read(4)
            if text.startswith(start_byte):
                print('ok')
            else:
                print('not ok')
            # text = text.rstrip('\r\n')
            # print(b'text')
            self.output_te.append(str(text))

    @QtCore.pyqtSlot()
    def send(self):
        self.serial.write(self.message_le.text().encode())
        print(self.serial.isOpen())

    @QtCore.pyqtSlot(bool)
    def on_toggled(self, checked):
        self.button.setText("Disconnect" if checked else "Connect")
        print(self.serial.isOpen())
        if checked:
            print(self.serial.isOpen())
            if not self.serial.isOpen():
                print(self.serial.isOpen())
                if not self.serial.open(QIODevice.OpenModeFlag.ReadWrite):
                    self.button.setChecked(False)
        else:
            self.serial.close()

