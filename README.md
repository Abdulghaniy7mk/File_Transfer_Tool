---

# 📁 File\_Transfer\_Tool

**File\_Transfer\_Tool** is a secure, obfuscated file-sharing system built by **Abdul Ghaniy**. It encrypts files using **AES-256**, disguises IP and port using a custom encoder, and transfers securely over LAN or WAN.

Designed for command-line users, it works smoothly on **Termux**, **Linux**, and **Windows** platforms.

---

## ⚙️ Features

* ✅ AES-256 encryption with unique initialization vector
* ✅ Obfuscated IP and Port for enhanced privacy
* ✅ Encrypted file sharing over terminal
* ✅ Real-time download progress bar
* ✅ Clean UI with colorful banner and messages
* ✅ Cross-platform support (Termux/Linux/Windows)

---

## 📦 Requirements

* Python 3.8+
* Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📲 Installation

### 📱 Termux

```bash
pkg update && pkg upgrade
pkg install python git
pip install -r requirements.txt

git clone https://github.com/Abdulghaniy7mk/File_Transfer_Tool.git
cd File_Transfer_Tool
```

### 🖥️ Windows

1. Install Python from [python.org](https://www.python.org/downloads/)
2. Open CMD or PowerShell:

```bash
git clone https://github.com/Abdulghaniy7mk/File_Transfer_Tool.git
cd File_Transfer_Tool
pip install -r requirements.txt
```

### 🐧 Linux

```bash
sudo apt update && sudo apt install python3 git
pip install -r requirements.txt

git clone https://github.com/Abdulghaniy7mk/File_Transfer_Tool.git
cd File_Transfer_Tool
```

---

## 🚀 How to Use

### 1. Start the File Server

```bash
python file_server.py --file your_file.mp4 --port 8080
```

Example:

```
🔐 Sharing: my_secret_file.zip
🌐 Obfuscated: gjsXaXaXg:tata
📡 Listening on 127.0.0.1:8080
```

### 2. Download the File via Client

```bash
python file_client.py
```

Enter:

* Obfuscated IP (e.g., `gjsXaXaXg`)
* Obfuscated Port (e.g., `tata`)

✅ The file will be downloaded and auto-decrypted to your `downloads/Termux_file_transfer_tool/` directory.

---

## 🛠️ Troubleshooting

### "Connection Refused"

* Ensure the server is running and the port is open.

### "Permission Denied" in Termux

```bash
termux-setup-storage
chmod +x file_*.py
```

### "Broken Pipe" or "Decryption Error"

* Ensure client and server use the same `config.py` with matching AES key and encoding logic.

---

## 📁 File Structure

```
File_Transfer_Tool/
├── file_server.py           # 🔼 Sends encrypted file via obfuscated IP/Port
├── file_client.py           # 🔽 Connects and downloads + decrypts file
├── config.py                # 🔐 AES encryption logic, IP/Port obfuscation maps
├── ui_utils.py              # 🎨 Colors, banner, clear_screen()
├── requirements.txt         # 📦 Dependencies (pycryptodome, etc.)
├── __pycache__/             # 🧠 Python cache (ignore this)
└── README.md                # 📖 Documentation (this file)
```

---

## 📝 License

This project is licensed under the **MIT License**.

Made with 💙 by **Abdul Ghaniy**

---
