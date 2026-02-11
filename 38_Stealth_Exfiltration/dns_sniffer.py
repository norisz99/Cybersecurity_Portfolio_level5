import socket
import base64

# --- KONFIGURÁCIÓ ---
# Localhoston tesztelünk, UDP porton (A DNS mindig UDP!)
LISTEN_IP = "127.0.0.1"
LISTEN_PORT = 10053  # Az igazi DNS az 53, de ahhoz Admin jog kellene, így teszthez eltoljuk.

def start_sniffer():
    # UDP Socket létrehozása (SOCK_DGRAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((LISTEN_IP, LISTEN_PORT))
    
    print(f"--- [ PROJECT 38: DNS TUNNEL LISTENER ] ---")
    print(f"[*] Figyelem a titkosított csatornát: {LISTEN_IP}:{LISTEN_PORT}")
    
    while True:
        try:
            # Adat fogadása
            data, addr = sock.recvfrom(1024)
            message = data.decode().strip()
            
            # Szimuláció: A vírus így küldi: "KÓDOLT_ADAT.microsoft.com"
            # Minket csak az eleje érdekel.
            if "." in message:
                encoded_part = message.split(".")[0]
                
                # Visszafejtés (Base64)
                try:
                    decoded = base64.b64decode(encoded_part).decode()
                    print(f"[+] ADAT ELKAPVA ({addr}): {decoded}")
                except:
                    print(f"[?] Ismeretlen forgalom: {message}")
                    
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"[-] Hiba: {e}")

if __name__ == "__main__":
    start_sniffer()