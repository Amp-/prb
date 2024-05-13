import crc_maxim
from communication2 import Com
start_byte = b'\xaa'

def fn_send(serial, op_code, data):
    s_byte = start_byte
    o_code = bytes.fromhex(op_code)  # 04
    d_byte = bytes.fromhex(data)  # 00
    crc = bytes.fromhex(crc_maxim.DallasMaximCRC8(o_code + d_byte))
    send_byte = s_byte + o_code + d_byte + crc
    serial.send(send_byte)

def fn_pasre(data):
    b = str(bin(int.from_bytes(data)))
    print(f'Байт {b} с последним битом {b[-1]}')

def check_data(data):
    b_opt_and_data = data[1:3]
    crc = bytes.fromhex(crc_maxim.DallasMaximCRC8(b_opt_and_data))
    if data.startswith(start_byte) and data.endswith(crc):
        return True
def check_door(data):
    #разобрать строку?
    #проверить статус двери
    pass



def receive(serial,size):
    text = serial.receive(size)
    return text