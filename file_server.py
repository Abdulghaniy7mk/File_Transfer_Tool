import socket
import argparse
import os
import time
import base64
from config import encrypt_file_bytes, encode_ip
from ui_utils import print_banner, CYAN, GREEN, RESET, clear_screen

def start_file_server(file_path, port):
    clear_screen()
    print_banner()

    if not os.path.exists(file_path):
        print(f"{CYAN}❌ File not found: {file_path}{RESET}")
        return

    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        data = f.read()

    encrypted_data = encrypt_file_bytes(data)
    encoded_data = base64.b64encode(encrypted_data)

    ip = socket.gethostbyname(socket.gethostname())
    encoded_ip = encode_ip(ip)
    encoded_port = encode_ip(str(port))

    print(f"{GREEN}🔐 Sharing: {file_name}{RESET}")
    print(f"{CYAN}🌐 Obfuscated: {encoded_ip}:{encoded_port}{RESET}")
    print(f"{CYAN}📡 Listening on {ip}:{port}{RESET}\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print(f"{GREEN}🔗 Connected by {addr}{RESET}")

            # Send filename and size
            header = f"{file_name}\n{len(encoded_data)}\n"
            conn.sendall(header.encode())
            time.sleep(0.2)  # Ensure client processes header first

            # Send encrypted data
            conn.sendall(encoded_data)

            print(f"{GREEN}✅ File sent successfully.{RESET}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Secure File Server")
    parser.add_argument("--file", required=True, help="Path to file to share")
    parser.add_argument("--port", type=int, required=True, help="Port to host on")
    args = parser.parse_args()

    start_file_server(args.file, args.port)

