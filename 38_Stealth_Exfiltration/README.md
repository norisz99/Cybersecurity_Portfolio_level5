# 🕵️‍♂️ Project 38: Stealth DNS Exfiltration

**Focus:** Network Evasion, DNS Tunneling, Traffic Obfuscation, Firewall Bypassing

## 📌 Áttekintés
A legtöbb tűzfal blokkolja az ismeretlen TCP kapcsolatokat, de a DNS forgalmat (UDP 53) átengedi. Ez a projekt demonstrálja a **DNS Tunneling** technikát, amellyel adatokat csempészhetünk ki egy szigorúan védett hálózatból.
Az adatokat Base64 kódolással "aldomainekbe" rejtjük (pl. `TITKOSADAT.microsoft.com`), így a hálózati monitorok számára legitim forgalomnak tűnik.

## 🛠 Fájlok
* `dns_sniffer.py`: A szerver oldal. Figyeli a bejövő UDP csomagokat, és kicsomagolja belőlük a rejtett üzenetet.
* `dns_sender.py`: A kliens oldal. Titkosítja az adatot, és DNS kérésnek álcázva elküldi.

## 🚀 Használat
1.  Indítsd el a Sniffert (Szerver):
    ```bash
    python dns_sniffer.py
    ```
2.  Indítsd el a Küldőt (Kliens):
    ```bash
    python dns_sender.py
    ```
3.  Eredmény: A szerver ablakában megjelenik a dekódolt, titkos üzenet, miközben a hálózaton csak domain lekérdezések látszanak.

## 🧠 Mit tanultam?
* Hogyan működik az UDP protokoll a TCP-vel szemben.
* Miért nehéz detektálni a DNS alapú adatlopást.
* Hogyan használható a Base64 kódolás adatátvitelre.

---
**⚠️ Disclaimer:** Valós hálózatokon a DNS Tunneling használata engedély nélkül illegális behatolásnak minősül.