import logging
from logging.handlers import SysLogHandler
from uhubctl import Hub

# Настройка логгирования
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)
handler = SysLogHandler(address='/dev/log')
logger.addHandler(handler)

# Инициализация хаба и портов
hub = Hub("3-4")
port_list = [hub.add_port(port) for port in range(1, 8)]

def log_action(port_num, action):
    message = f"Port {port_num}: {'ON' if action else 'OFF'}"
    log_func = logger.debug if action else logger.critical
    log_func(message)

def set_port_status(port_num, status: bool):
    """Включает или выключает указанный порт (1-7)."""
    if 1 <= port_num <= len(port_list):
        port_list[port_num - 1].status = status
        log_action(port_num, status)
        return port_list[port_num - 1].status
    else:
        raise IndexError("Недопустимый номер порта")

def set_all_ports(status: bool):
    """Включает или выключает все порты."""
    for idx, port in enumerate(port_list, start=1):
        port.status = status
        log_action(idx, status)
    return [port.status for port in port_list]

# Примеры использования:
# set_port_status(1, True)  # Включить порт 1
# set_port_status(2, False) # Выключить порт 2
# set_all_ports(True)       # Включить все порты
# set_all_ports(False)      # Выключить все порты
