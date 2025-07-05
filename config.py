import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 🔐 AES Configuration
KEY = hashlib.sha256(b"ghaniykey").digest()  # 32-byte AES-256 key
IV = b"1234567890123456"  # 16-byte IV (static for now, can be randomized for advanced use)

# 🔒 AES Encryption
def encrypt_file_bytes(data: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    encrypted = cipher.encrypt(pad(data, AES.block_size))
    return encrypted

# 🔓 AES Decryption
def decrypt_file_bytes(data: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decrypted = unpad(cipher.decrypt(data), AES.block_size)
    return decrypted

# 🔁 IP & Port Obfuscation Maps
ENCODE_MAP = {
    '0': 'a', '1': 'g', '2': 'j', '3': 'k',
    '4': 'm', '5': 'p', '6': 'r', '7': 's',
    '8': 't', '9': 'u', '.': 'X'
}

DECODE_MAP = {v: k for k, v in ENCODE_MAP.items()}

# 🔠 Encode IP (e.g. 127.0.0.1 → gsrXagXagXg)
def encode_ip(ip: str) -> str:
    return ''.join(ENCODE_MAP.get(c, c) for c in ip)

# 🔠 Decode IP
def decode_ip(encoded: str) -> str:
    try:
        return ''.join(DECODE_MAP[c] for c in encoded)
    except KeyError as e:
        raise KeyError(f"Invalid character in encoded IP: '{e.args[0]}'")

# 🔠 Encode Port (e.g. 8080 → tutu)
def encode_port(port: int) -> str:
    return ''.join(ENCODE_MAP[d] for d in str(port))

# 🔠 Decode Port
def decode_port(encoded: str) -> int:
    try:
        return int(''.join(DECODE_MAP[c] for c in encoded))
    except KeyError as e:
        raise KeyError(f"Invalid character in encoded Port: '{e.args[0]}'")

