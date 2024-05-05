from uhubctl import Hub, Port
import logging
import logging.handlers

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')

my_logger.addHandler(handler)


import uhubctl
#hubs = uhubctl.discover_hubs()

# for hub in hubs:
#     print(f"Found hub: {hub}")
#
#     for port in hub.ports:
#         print(f"   Found port: {port}")


hub = Hub("3-4")
port_list = []
for port in range(1,8):
    port_list.append(hub.add_port(port))

# while True:
#     answ = int(input("On -1, Off-2,Status-5: "))
#     print(answ)
#     if answ == 1:
#         for p in port_list:
#             p.status = True
#     elif answ == 2:
#         for p in port_list:
#             p.status = False
#     elif answ == 3:
#         for p in port_list:
#             p.status = False
#     elif answ == 4:
#         for p in port_list:
#             p.status = False
#     elif answ == 5:
#         for p in port_list:
#             print(p.status)
#     else:
#         break

def turn_on_1():
    port_list[0].status = True
    my_logger.debug('this is debug')
    return port_list[0].status
def turn_off_1():
    port_list[0].status = False
    my_logger.critical('this is nodebug')
    return port_list[0].status
def turn_on_2():
    port_list[1].status = True
    my_logger.debug('this is debug')
    return port_list[1].status
def turn_off_2():
    port_list[1].status = False
    my_logger.critical('this is nodebug')
    return port_list[1].status
def turn_on_3():
    port_list[2].status = True
    my_logger.debug('this is debug')
    return port_list[2].status
def turn_off_3():
    port_list[2].status = False
    my_logger.critical('this is nodebug')
    return port_list[2].status
def turn_on_4():
    port_list[3].status = True
    my_logger.debug('this is debug')
    return port_list[3].status
def turn_off_4():
    port_list[3].status = False
    my_logger.critical('this is nodebug')
    return port_list[3].status
def turn_on_5():
    port_list[4].status = True
    my_logger.debug('this is debug')
    return port_list[4].status
def turn_off_5():
    port_list[4].status = False
    my_logger.critical('this is nodebug')
    return port_list[4].status
def turn_on_6():
    port_list[5].status = True
    my_logger.debug('this is debug')
    return port_list[5].status
def turn_off_6():
    port_list[5].status = False
    my_logger.critical('this is nodebug')
    return port_list[5].status
def turn_on_7():
    port_list[6].status = True
    my_logger.debug('this is debug')
    return port_list[6].status
def turn_off_6():
    port_list[6].status = False
    my_logger.critical('this is nodebug')
    return port_list[6].status
def turn_on_all():
    for p in port_list:
     p.status = True
    my_logger.debug('this is debug')
    return port_list[6].status
def turn_off_all():
    for p in port_list:
        p.status = False
    my_logger.critical('this is nodebug')
    return port_list[6].status

#if __name__ == "__main__":