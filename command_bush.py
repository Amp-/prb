import crc_maxim
from serial_communication import Com

start_byte = b'\xaa'

def send(serial, op_code, data):
    """Функция отправки данных по сериализации."""
    s_byte = start_byte
    o_code = bytes.fromhex(op_code)  # Операционный код (например, '04')
    d_byte = bytes.fromhex(data)     # Данные (например, '00')
    crc = bytes.fromhex(crc_maxim.DallasMaximCRC8(o_code + d_byte))  # CRC для проверки
    send_byte = s_byte + o_code + d_byte + crc  # Соединяем все байты для отправки
    serial.send(send_byte)

def fn_parse(data):
    """Парсинг и вывод последнего бита данных."""
    b = str(bin(int.from_bytes(data, byteorder='big')))  # Преобразуем в строку двоичного представления
    #print(f'Байт {b} с последним битом {b[-1]}')  # Выводим последний бит


def check_data(data):
    """Проверка данных на корректность с использованием CRC."""
    b_opt_and_data = data[1:3]  # Берем байты с 1 по 3 (исключая start_byte и CRC)

    try:
        # Преобразуем результат CRC в байты
        crc_str = crc_maxim.DallasMaximCRC8(b_opt_and_data)

        # Проверяем, является ли строка валидной для fromhex
        crc = bytes.fromhex(crc_str)
    except ValueError as e:
        # Если произошла ошибка при преобразовании в байты, возвращаем False
        print(f"Ошибка CRC: {e}")
        return False

    if data.startswith(start_byte) and data.endswith(crc):  # Если начало и конец данных корректны
        return True
    return False  # Если проверка не прошла

def check_door(data):
    """Функция для проверки состояния двери (нужна доработка)."""
    # Тут можно будет разобрать строку и проверить статус двери
    pass

def receive(serial, size):
    """Функция для получения данных с устройства."""
    text = serial.receive(size)
    return text
