# 🛡️ Project 41: DNS Gatekeeper (Sinkhole Protection)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![System](https://img.shields.io/badge/System-DNS_Sinkhole-green?style=flat-square)
![Category](https://img.shields.io/badge/Category-Blue_Team_Capstone-blue?style=flat-square)

## 📌 Áttekintés (Overview)
A **Level 5 Capstone Project** egy védelmi rendszer, amely a **DNS Sinkhole** technológiát valósítja meg. A "Gatekeeper" figyeli a hálózati DNS kéréseket, és összeveti azokat egy ismert kártékony domaineket tartalmazó feketelistával (Blacklist). Ha egy eszköz fertőzött, és megpróbál hazatelefonálni (C2), a Gatekeeper blokkolja a kérést, és átirányítja egy figyelmeztető oldalra (`index.html`).

## 🛠️ Funkciók
* **🚫 Malicious Domain Blocking:** Kártékony domainek (pl. `malware.com`, `c2-server.ru`) szűrése.
* **🕳️ Traffic Sinkholing:** A veszélyes kérések átirányítása egy biztonságos belső IP-re (a valódi szerver helyett).
* **🚨 User Alerting:** Egy `index.html` alapú figyelmeztető oldal megjelenítése a felhasználónak ("Az oldalt biztonsági okokból blokkoltuk").
* **📝 Incident Logging:** A blokkolt kérések naplózása elemzés céljából.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Mechanizmus:** DNS Proxy / Interceptor
* **Felhasználás:** Vállalati hálózatvédelem, Malware kommunikáció megállítása.

## 🚀 Használat
1. **Konfiguráció:** Állítsd be a `BLOCK_LIST` listát a kódban.
2. **Indítás:**
   ```bash
   python dns_gatekeeper.py
