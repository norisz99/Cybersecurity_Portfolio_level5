import socket
from dnslib import DNSRecord, DNSHeader, RR, A, QTYPE

# --- A TE HÁLÓZATI ADATAID ---
MY_IP = "192.168.2.100"   # A Te Fix IP-d
ROUTER_IP = "192.168.2.1" # A ONE Router címe

def start_dns_server():
    # Létrehozunk egy UDP szervert az 53-as porton
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Fontos: Ehhez a parancssort Rendszergazdaként (Admin) kell futtatni!
        sock.bind((MY_IP, 53))
        print(f"--- [ TWITCH GATEKEEPER AKTÍV ] ---")
        print(f"[*] Figyelem a hálózati forgalmat itt: {MY_IP}:53")
        print(f"[*] Csatlakozz a telefonoddal a Wifi-re és próbálj netezni!")
        
        while True:
            data, addr = sock.recvfrom(512)
            try:
                request = DNSRecord.parse(data)
                qname = str(request.q.qname)
                
                # Minden kérdésre (pl. facebook.com) azt hazudjuk: "ITT VAGYOK!"
                reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)
                reply.add_answer(RR(qname, QTYPE.A, rdata=A(MY_IP), ttl=0))
                
                print(f"[+] ELKAPTUK: {addr[0]} -> {qname} -> Átirányítva ide: {MY_IP}")
                
                sock.sendto(reply.pack(), addr)
            except:
                pass
    except PermissionError:
        print("[!] HIBA: Rendszergazdai jogok kellenek az 53-as porthoz!")
    except Exception as e:
        print(f"[!] Hiba: {e}")

if __name__ == "__main__":
    start_dns_server()