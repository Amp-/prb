from PyQt6 import QtCore, QtSerialPort
from PyQt6.QtCore import QIODevice


class Com():

    def __init__(self,portName, baudRate, serialPort):
        self.serial = serialPort
        self.serial.setPortName(portName)
        self.serial.setBaudRate(baudRate)
        self.portList = []


    @QtCore.pyqtSlot()
    def receive(self,size):
        text = self.serial.read(size)
        return text

    @QtCore.pyqtSlot()
    def send(self,text):
        #t = bytes.fromhex(text)
        self.serial.write(text)

    @QtCore.pyqtSlot(bool)
    def on_toggled(self, checked):
        if checked:
            print(self.serial.isOpen())
            if not self.serial.isOpen():
                if not self.serial.open(QIODevice.OpenModeFlag.ReadWrite):
                    #self.button.setChecked(False)
                    print('test')
        else:
            self.serial.close()
            print('text')
            return False

    @classmethod
    def com_list(cls):
        comPortList = []
        comList = QtSerialPort.QSerialPortInfo.availablePorts()
        for com in comList:
            comPortList.append(com.portName())
        return  comPortList
