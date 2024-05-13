import os
import sys

from PyQt6.QtWidgets import QPushButton

import usb
import command_bush as cmd_b
from communication2 import Com
from PyQt6 import QtCore,QtWidgets,QtSerialPort, uic

start_byte = b'\xaa'

com_bus = Com(baudRate=115200, portName='/dev/ttyACM0', serialPort=QtSerialPort.QSerialPort())
com_bush = Com(baudRate=115200, portName='/dev/ttyUSB0', serialPort=QtSerialPort.QSerialPort())
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
port_list = Com.com_list()

# path = os.path.dirname(os.path.abspath(__file__))
# uiFile = os.path.join(path, 'Main_1.ui')
# WindowTemplate, TemplateBaseClass = pg.Qt.loadUiType(uiFile)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("MainWindow.ui", self)
        # self.usb1_radio_btn_on.clicked.connect(self.turn_on_1)
        # self.usb1_radio_btn_off.clicked.connect(self.turn_off_1)
        # self.usb2_radio_btn_on.clicked.connect(self.turn_on_2)
        # self.usb2_radio_btn_off.clicked.connect(self.turn_off_2)
        # self.usb3_radio_btn_on.clicked.connect(self.turn_on_3)
        # self.usb3_radio_btn_off.clicked.connect(self.turn_off_3)
        # self.usb4_radio_btn_on.clicked.connect(self.turn_on_4)
        # self.usb4_radio_btn_off.clicked.connect(self.turn_off_4)
        # self.usb5_radio_btn_on.clicked.connect(self.turn_on_5)
        # self.usb5_radio_btn_off.clicked.connect(self.turn_off_5)
        # self.usb6_radio_btn_on.clicked.connect(self.turn_on_6)
        # self.usb6_radio_btn_off.clicked.connect(self.turn_off_6)
        # self.usb_all_radio_btn_on.clicked.connect(self.turn_on_all)
        # self.usb_all_radio_btn_off.clicked.connect(self.turn_off_all)

        self.comboBox_sbz.addItems(port_list)
        self.comboBox_she.addItems(port_list)

        self.pushButton_sbz.clicked.connect(self.on_toggled_bus)
        self.pushButton_she.clicked.connect(self.on_toggled_bush)

        self.bus = com_bus.serial
        self.bus.readyRead.connect(lambda: self.receive_bus(4))

        self.bush = com_bush.serial
        self.bush.readyRead.connect(lambda: self.receive_bush(4))

        self.radio_she_on.clicked.connect(self.fn_send_bush_close)
        self.radio_she_off.clicked.connect(self.fn_send_bush_open)




    # def turn_on_0(self):
    #     print(usb.turn_on_1())
    # def turn_off_0(self):
    #     print(usb.turn_off_1())
    # def turn_on_1(self):
    #     print(usb.turn_on_1())
    # def turn_off_1(self):
    #     print(usb.turn_off_1())
    #
    # def turn_on_2(self):
    #     print(usb.turn_on_2())
    # def turn_off_2(self):
    #     print(usb.turn_off_2())
    # def turn_on_3(self):
    #     print(usb.turn_on_3())
    # def turn_off_3(self):
    #     print(usb.turn_off_3())
    # def turn_on_4(self):
    #     print(usb.turn_on_4())
    # def turn_off_4(self):
    #     print(usb.turn_off_4())
    # def turn_on_5(self):
    #     print(usb.turn_on_5())
    # def turn_off_5(self):
    #     print(usb.turn_off_5())
    # def turn_on_6(self):
    #     print(usb.turn_on_6())
    # def turn_off_6(self):
    #     print(usb.turn_off_6())
    # def turn_on_all(self):
    #     print(usb.turn_on_all())
    # def turn_off_all(self):
    #     print(usb.turn_off_all())

    @QtCore.pyqtSlot()
    def receive_bush(self, size):
        #print(com_bush.receive(size))
        print(cmd_b.receive(com_bush,size))

    @QtCore.pyqtSlot()
    def receive_bus(self, size):
        print(com_bus.receive(size))

    def fn_send_bush_close(self):
        cmd_b.fn_send(serial=com_bush,op_code='05', data='FF')
        cmd_b.fn_send(serial=com_bush, op_code='07', data='FF')
        # cmd_b.fn_send(self, serial=com_bush, op_code='01', data='00') #тзапрос состояния
        #cmd_b.fn_send(serial=com_bush, op_code='02', data='90')

    def fn_send_bush_open(self):
        cmd_b.fn_send(serial=com_bush, op_code='05', data='00')
        cmd_b.fn_send(serial=com_bush, op_code='07', data='00')
        cmd_b.fn_send(serial=com_bush, op_code='01', data='00')

    @QtCore.pyqtSlot(bool)
    def on_toggled_bush(self, checked):
        com_bush.on_toggled(checked)
        #t = cmd_b.fn_in(serial=com_bush,size=4)
        #print(t)

        self.pushButton_she.setText("Disconnect" if checked else "Connect")

    @QtCore.pyqtSlot(bool)
    def on_toggled_bus(self, checked):
        com_bus.on_toggled(checked)
        self.pushButton_sbz.setText("Disconnect" if checked else "Connect")




app=QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



