from PyQt6 import QtCore, QtSerialPort
from PyQt6.QtCore import QIODevice

class Com:
    def __init__(self, portName, baudRate, serialPort):
        """Инициализация порта с указанным именем и скоростью передачи данных."""
        self.serial = serialPort
        self.serial.setPortName(portName)
        self.serial.setBaudRate(baudRate)
        self.portList = []

    @QtCore.pyqtSlot()
    def receive(self, size):
        """Чтение данных из последовательного порта."""
        text = self.serial.read(size)
        return text

    @QtCore.pyqtSlot()
    def send(self, text):
        """Отправка данных в последовательный порт."""
        self.serial.write(text)

    @QtCore.pyqtSlot(bool)
    def on_toggled(self, checked):
        """Обработка переключения состояния соединения с последовательным портом."""
        if checked:
            if not self.serial.isOpen():
                # Попытка открыть порт в режиме чтения и записи
                # self.serial.setPortName('COM1')  # Укажите правильный порт
                if not self.serial.open(QIODevice.OpenModeFlag.ReadWrite):
                    print(f'Не удалось открыть порт: {self.serial.portName()}')
                else:
                    print(f'Порт {self.serial.portName()} успешно открыт')
        else:
            if self.serial.isOpen():
                self.serial.close()  # Закрытие порта
                print(f'Порт {self.serial.portName()} закрыт')
            else:
                print('Порт уже закрыт')

    @classmethod
    def com_list(cls):
        """Получение списка доступных COM-портов."""
        comPortList = []
        comList = QtSerialPort.QSerialPortInfo.availablePorts()
        for com in comList:
            comPortList.append(com.portName())
        return comPortList
