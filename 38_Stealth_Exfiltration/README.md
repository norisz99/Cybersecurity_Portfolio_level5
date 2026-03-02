# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 📡 Project 38: DNS Data Exfiltration

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-Scapy%2FDNS-red?style=flat-square)
![Category](https://img.shields.io/badge/Category-Covert_Channel-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez az eszköz a **DNS Tunneling** technikát demonstrálja adatok kicsempészésére. Mivel a DNS forgalmat (UDP 53) a tűzfalak ritkán blokkolják, a támadók gyakran ebbe rejtik az ellopott adatokat. A program az adatokat Base64 kódolással aldomainekké alakítja (pl. `titkosadat.attacker.com`), és DNS lekérdezésnek álcázva juttatja ki a szervezetből.

## 🛠️ Funkciók
* **📦 Data Chunking:** A nagy fájlok feldarabolása kisebb DNS kérésekre.
* **B64 Encoding:** Az adatok átalakítása URL-barát formátumba.
* **👂 DNS Sniffer:** A szerver oldali komponens, ami "hallgatózik" és visszafejti a beérkező "kamu" domaineket eredeti fájllá.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `scapy` (Sniffer), `dnspython` (Sender)
* **Protokoll:** DNS (UDP/53)

## 🚀 Használat
1. **Szerver (Hallgatózás):** `python dns_sniffer.py`
2. **Kliens (Küldés):** `python dns_sender.py --file "titkos.txt"`
