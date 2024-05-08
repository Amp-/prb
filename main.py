import os
import sys
import usb
from communication2 import Com
from PyQt6 import QtCore,QtWidgets,QtSerialPort, uic

com_bus = Com(baudRate=19200, portName='/dev/ttyUSB0', serialPort=QtSerialPort.QSerialPort())
com_bush = Com(baudRate=115200, portName='/dev/ttyUSB1', serialPort=QtSerialPort.QSerialPort())
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
port_list = QtSerialPort.QSerialPortInfo.availablePorts()
for port in port_list:
    print(port.portName())

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    for t in port_list:
        print(t.portName())

# path = os.path.dirname(os.path.abspath(__file__))
# uiFile = os.path.join(path, 'Main_1.ui')
# WindowTemplate, TemplateBaseClass = pg.Qt.loadUiType(uiFile)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("MainWindow.ui", self)
        self.usb1_radio_btn_on.clicked.connect(self.turn_on_1)
        self.usb1_radio_btn_off.clicked.connect(self.turn_off_1)
        self.usb2_radio_btn_on.clicked.connect(self.turn_on_2)
        self.usb2_radio_btn_off.clicked.connect(self.turn_off_2)
        self.usb3_radio_btn_on.clicked.connect(self.turn_on_3)
        self.usb3_radio_btn_off.clicked.connect(self.turn_off_3)
        self.usb4_radio_btn_on.clicked.connect(self.turn_on_4)
        self.usb4_radio_btn_off.clicked.connect(self.turn_off_4)
        self.usb5_radio_btn_on.clicked.connect(self.turn_on_5)
        self.usb5_radio_btn_off.clicked.connect(self.turn_off_5)
        self.usb6_radio_btn_on.clicked.connect(self.turn_on_6)
        self.usb6_radio_btn_off.clicked.connect(self.turn_off_6)
        self.usb_all_radio_btn_on.clicked.connect(self.turn_on_all)
        self.usb_all_radio_btn_off.clicked.connect(self.turn_off_all)

    def turn_on_0(self):
        print(usb.turn_on_1())
        print_hi
    def turn_off_0(self):
        print(usb.turn_off_1())
    def turn_on_1(self):
        print(usb.turn_on_1())
    def turn_off_1(self):
        print(usb.turn_off_1())

    def turn_on_2(self):
        print(usb.turn_on_2())
    def turn_off_2(self):
        print(usb.turn_off_2())
    def turn_on_3(self):
        print(usb.turn_on_3())
    def turn_off_3(self):
        print(usb.turn_off_3())
    def turn_on_4(self):
        print(usb.turn_on_4())
    def turn_off_4(self):
        print(usb.turn_off_4())
    def turn_on_5(self):
        print(usb.turn_on_5())
    def turn_off_5(self):
        print(usb.turn_off_5())
    def turn_on_6(self):
        print(usb.turn_on_6())
    def turn_off_6(self):
        print(usb.turn_off_6())
    def turn_on_all(self):
        print(usb.turn_on_all())
    def turn_off_all(self):
        print(usb.turn_off_all())


app=QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



