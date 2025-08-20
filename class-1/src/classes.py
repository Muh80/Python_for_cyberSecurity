class Cars:
    wheels = 4

    def __init__(self, color, hsp):
        self.color = color
        self.hsp = hsp

    def print_color(self):
        print(self.color)
    
    @staticmethod
    def _print_hsp():
        print("the is static method")


samsung = Cars("black", 16)
kia = Cars("white", 20)

# samsung.print_color()


from dataclasses import dataclass
from datetime import datetime
from typing import Any

@dataclass(frozen=True)
class LogEntry:
    ts:datetime
    host: str
    program: str
    msg: str


class IOCMatcher:
    """this is class to holds bad IPs"""
    # this is
    def __init__(self, ips: set[str] | None = None, domains: set[str] | None = None):
        self.ips = ips
        self.domains = domains

    def match_msg(self, msg: str):
        return any(ip in msg for ip in self.ips) or any(d in msg for d in self.domains)
    
my_ips = {"192.168.1.10","203.0.113.45","198.51.100.23"}
my_domains = {"google.com", "yahoo.com", "duckduckgo.com"}
matcher = IOCMatcher(my_ips, my_domains)

# print(matcher.match_msg("192.168.1.10"))

from ipaddress import ip_address
class Device:
    def __init__(self, name: str, ip: str):
        self.name = name
        self.ip = ip_address(ip)

    def print_ip(self):
        print(self.ip)

class Firewall(Device):
    def __init__(self, name: str, ip: str, vendor: str):
        super().__init__(name, ip)
        self.vendor = vendor

    


d = Device("NSA", "192.168.1.10")
d.print_ip
print(d.name)
f = Firewall("CIA", "203.0.113.45", "USA")
f.print_ip