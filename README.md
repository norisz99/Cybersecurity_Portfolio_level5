# 📡 Cybersecurity & Python Portfolio - Level 5

**Author:** [Paczok Norisz]  
**Focus:** Command & Control (C2), Infrastructure, Data Exfiltration, Network Implants

---

## 📌 Overview

Ez a repozitórium a portfólió **ötödik, infrastruktúra-fókuszú szintje**. Itt a hangsúly az egyedi gépekről áttevődik a **teljes hálózat irányítására**.

A projektek bemutatják, hogyan épül fel egy **Command & Control (C2)** szerver, hogyan történik az adatok rejtett kimenekítése (Exfiltration), és hogyan lehet fizikai hálózati eszközökkel (pl. Rogue Router / Captive Portal) manipulálni a forgalmat.

---

## 📂 Project Catalog

### 🌐 C2 Infrastructure & Communication

| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[36_C2_Infrastructure](./36_C2_Infrastructure)** | A központi "Mothership" szerver és a kliensek közötti titkosított kommunikációs csatorna kiépítése (Multi-threaded Server). | `socket`, `threading`, Encryption (AES) |
| **[37_Supply_Chain_Attack](./37_Supply_Chain_Attack)** | Szoftverellátási lánc elleni támadás szimulációja: hogyan juthat be kód megbízhatónak tűnő frissítésekbe vagy csomagokba. | Package Manipulation, Code Injection |
| **[38_Stealth_Exfiltration](./38_Stealth_Exfiltration)** | Adatok kicsempészése a hálózatból rejtett csatornákon (pl. DNS Tunneling, HTTP fejlécbe rejtett adatok). | `dnslib`, `requests`, Steganography |
| **[39_Multimedia_Surveillance](./39_Multimedia_Surveillance)** | Távoli megfigyelés: Képkészítés webkamerával és hangrögzítés mikrofonnal, majd az adatok streamelése a szerverre. | `opencv`, `pyaudio`, Stream Handling |
| **[40_C2_Dashboard](./40_C2_Dashboard)** | Vezérlőpult (Dashboard) a zombihálózat (Botnet) menedzselésére, parancsok kiadására és a státuszok figyelésére. | UI Design (CLI/Web), Database Mgmt |

### 🏆 Level 5 Capstone Project

| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[41_Capstone_Project](./41_Capstone_Project)** | **"The Gatekeeper" (Captive Portal & DNS Spoofing):** Egy hálózati elfogó eszköz, amely egy köztes router/szerver segítségével DNS kéréseket térít el, és a felhasználókat egy hamis bejelentkező oldalra irányítja (Twitch/Social Login Phishing szimuláció). | `dnslib`, `http.server`, Network Traffic Manipulation, DNS Poisoning |

---

## 🛠 Technologies Used

* **Language:** Python 3.10+
* **Networking:** `socket`, `dnslib`, `requests`
* **Multimedia:** `opencv-python`, `pyaudio`
* **Concurrency:** `threading`, `multiprocessing`
* **Environment:** Kali Linux (Server side), Windows 10/11 (Client side), Custom Router Configs

---

## ⚠️ Jogi Nyilatkozat (Disclaimer)

A repozitóriumban található kódok kizárólag **oktatási és etikus kiberbiztonsági kutatási** célokat szolgálnak. A szoftverek bármilyen engedély nélküli, rosszindulatú használata illegális és súlyos jogi következményeket vonhat maga után. A készítő nem vállal felelősséget a kódok nem rendeltetésszerű használatáért.
