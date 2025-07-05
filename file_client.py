import socket
import os
import base64
from config import decode_ip, decrypt_file_bytes
from ui_utils import print_banner, clear_screen, BOLD, RESET, GREEN, RED, CYAN, YELLOW

def download_file(encoded_ip, encoded_port):
    try:
        ip = decode_ip(encoded_ip)
        port = int(decode_ip(encoded_port))
    except Exception as e:
        print(f"{RED}❌ Invalid encoded IP or port: {e}{RESET}")
        return

    print(f"\n{CYAN}🌍 Connecting to {ip}:{port}...{RESET}")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))

            # Receive header (filename and size)
            header = b''
            while b'\n' not in header or header.count(b'\n') < 2:
                header += s.recv(1024)

            lines = header.decode().splitlines()
            file_name = lines[0].strip()
            file_size = int(lines[1].strip())

            print(f"{GREEN}⬇️  Receiving '{file_name}' ({file_size} bytes encrypted)...{RESET}")

            # Create folder if not exists
            output_dir = os.path.expanduser("~/storage/downloads/Termux_file_transfer_tool")
            os.makedirs(output_dir, exist_ok=True)

            received_data = b''
            while len(received_data) < file_size:
                chunk = s.recv(4096)
                if not chunk:
                    break
                received_data += chunk
                percent = (len(received_data) / file_size) * 100
                print(f"{YELLOW}📥 Downloaded: {percent:.2f}%{RESET}", end='\r')

            print()

        # Decrypt and save
        try:
            decrypted = decrypt_file_bytes(base64.b64decode(received_data))
        except Exception as e:
            print(f"{RED}❌ Decryption failed: {e}{RESET}")
            return

        output_path = os.path.join(output_dir, "decrypted_" + file_name)
        with open(output_path, 'wb') as f:
            f.write(decrypted)

        print(f"{GREEN}✅ File saved as {output_path}{RESET}")

    except Exception as e:
        print(f"{RED}❌ Error: {e}{RESET}")

if __name__ == "__main__":
    clear_screen()
    print_banner()

    encoded_ip = input(f"{BOLD}Enter Obfuscated IP: {RESET}").strip()
    encoded_port = input(f"{BOLD}Enter Obfuscated Port: {RESET}").strip()
    download_file(encoded_ip, encoded_port)

