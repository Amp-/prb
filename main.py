import sys
from PyQt6 import QtCore, QtWidgets, QtSerialPort, uic

import usb
import command_bush as cmd_b
from serial_communication import Com

# Константы
START_BYTE = b'\xaa'

# Инициализация портов
com_bus = Com(baudRate=115200, portName='/dev/ttyACM0', serialPort=QtSerialPort.QSerialPort())
com_bush = Com(baudRate=115200, portName='/dev/ttyUSB0', serialPort=QtSerialPort.QSerialPort())

# Получение списка портов
port_list = Com.com_list()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("MainWindow.ui", self)

        # Центрируем окно на экране
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()  # Получаем доступную область экрана
        window_geometry = self.frameGeometry()  # Получаем геометрию окна

        # Вычисляем координаты центра экрана
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

        # Подключаем кнопки
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

        # Добавляем доступные COM-порты в выпадающие списки
        self.comboBox_sbz.addItems(port_list)
        self.comboBox_she.addItems(port_list)

        # Подключаем обработчики кнопок
        self.pushButton_sbz.clicked.connect(self.on_toggled_bus)
        self.pushButton_she.clicked.connect(self.on_toggled_bush)

        # Инициализируем соединения
        self.bus = com_bus.serial
        self.bus.readyRead.connect(lambda: self.receive_bus(4))

        self.bush = com_bush.serial
        self.bush.readyRead.connect(lambda: self.receive_bush(4))

        # Радио кнопки управления
        self.radio_sbz_on.clicked.connect(self.send_bus_close)
        self.radio_sbz_off.clicked.connect(self.send_bus_open)

        self.radio_she_on.clicked.connect(self.send_bush_close)
        self.radio_she_off.clicked.connect(self.send_bush_open)

        # Методы для включения/выключения портов через usb.py
    def turn_on_0(self):
        usb.set_port_status(1, True)
        print("Port 1 turned ON")

    def turn_off_0(self):
        usb.set_port_status(1, False)
        print("Port 1 turned OFF")

    def turn_on_1(self):
        usb.set_port_status(2, True)
        print("Port 2 turned ON")

    def turn_off_1(self):
        usb.set_port_status(2, False)
        print("Port 2 turned OFF")

    def turn_on_2(self):
        usb.set_port_status(3, True)
        print("Port 3 turned ON")

    def turn_off_2(self):
        usb.set_port_status(3, False)
        print("Port 3 turned OFF")

    def turn_on_3(self):
        usb.set_port_status(4, True)
        print("Port 4 turned ON")

    def turn_off_3(self):
        usb.set_port_status(4, False)
        print("Port 4 turned OFF")

    def turn_on_4(self):
        usb.set_port_status(5, True)
        print("Port 5 turned ON")

    def turn_off_4(self):
        usb.set_port_status(5, False)
        print("Port 5 turned OFF")

    def turn_on_5(self):
        usb.set_port_status(6, True)
        print("Port 6 turned ON")

    def turn_off_5(self):
        usb.set_port_status(6, False)
        print("Port 6 turned OFF")

    def turn_on_6(self):
        usb.set_port_status(7, True)
        print("Port 7 turned ON")

    def turn_off_6(self):
        usb.set_port_status(7, False)
        print("Port 7 turned OFF")

    def turn_on_all(self):
        usb.set_all_ports(True)
        print("All ports turned ON")

    def turn_off_all(self):
        usb.set_all_ports(False)
        print("All ports turned OFF")

    @QtCore.pyqtSlot()
    def receive_bush(self, size):
        """Обработка данных от устройства bush."""
        #print(cmd_b.receive(com_bush, size))
        data = com_bush.receive(size)
        if cmd_b.check_data(data):
            parsed = cmd_b.fn_parse(data)
            #print(parsed)

    @QtCore.pyqtSlot()
    def receive_bus(self, size):
        """Обработка данных от устройства bus."""
        print(com_bus.receive(size))

    def send_bush_close(self):
        """Закрыть bush."""
        cmd_b.send(serial=com_bush, op_code='05', data='FF')
        cmd_b.send(serial=com_bush, op_code='07', data='FF')

    def send_bush_open(self):
        """Открыть bush."""
        cmd_b.send(serial=com_bush, op_code='05', data='00')
        cmd_b.send(serial=com_bush, op_code='07', data='00')
        cmd_b.send(serial=com_bush, op_code='01', data='00')

    def send_bus_close(self):
        """Закрыть bus."""
        com_bus.receive(b'\xC0')

    def send_bus_open(self):
        """Открыть bus."""
        com_bus.receive(b'\x00')

    @QtCore.pyqtSlot(bool)
    def on_toggled_bush(self, checked):
        """Переключение bush соединения."""
        com_bush.on_toggled(checked)
        self.pushButton_she.setText("Disconnect" if checked else "Connect")

    @QtCore.pyqtSlot(bool)
    def on_toggled_bus(self, checked):
        """Переключение bus соединения."""
        com_bus.on_toggled(checked)
        self.pushButton_sbz.setText("Disconnect" if checked else "Connect")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
