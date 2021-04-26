import ipaddress
import threading
from socket import *


class PortScanner:

    def __init__(self, addr_range):
        self.ip_addr = addr_range
        self.ip_addr_list = []

    def list_of_addr(self):
        addresses = ipaddress.ip_network(self.ip_addr)
        for host in addresses.hosts():
            self.ip_addr_list.append(str(host))
        return self.ip_addr_list

    def port_scan(self, host, port):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.5)
        try:
            connection = s.connect((host, port))
            print(f'{host} {int(port)} OPEN')
            connection.close()
        except:
            pass


if __name__ == '__main__':
    ip_address = input("Введите адрес: ")
    scanner = PortScanner(addr_range=ip_address)
    list_of_ports = [80, 443, 22, 21, 25]
    list_of_ip = scanner.list_of_addr()
    for ip in list_of_ip:
        for port in list_of_ports:
            t = threading.Thread(target=scanner.port_scan, args=(ip, port))
            t.start()
