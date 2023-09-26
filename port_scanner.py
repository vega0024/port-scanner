import socket
import time
from colorama import init, Fore, Style

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  # Set a timeout value for the connection attempt

    try:
        sock.connect((ip, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()

def print_green(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

def print_red(text):
    print(Fore.RED + text + Style.RESET_ALL)


init()

target_ip = input("Enter target IP address: ")

while True:
    for port in range(1, 65536):
        if check_port(target_ip, port):
            print_green(f"The port {port} is open on {target_ip}.>>>>>>>>>>>>>>>>>>>>>>>OPEN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        else:
            print_red(f"The port {port} is closed on {target_ip}.")

    time.sleep(1)
