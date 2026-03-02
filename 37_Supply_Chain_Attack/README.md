# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 📦 Project 37: Supply Chain Attack Simulation

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Technique](https://img.shields.io/badge/Technique-Code_Injection-orange?style=flat-square)
![Category](https://img.shields.io/badge/Category-Advanced_Threat-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt a **Supply Chain (Ellátási lánc)** támadások működését szimulálja. A forgatókönyv szerint a támadó nem közvetlenül az áldozatot töri fel, hanem egy megbízható szoftvert (itt: `legit_calculator.py`) módosít, elrejtve benne egy hátsó kaput (`malicious_client`). Amikor a felhasználó elindítja a "számológépet", a háttérben a kártevő is lefut.

## 🛠️ Funkciók
* **🎭 Trojanized Software:** Egy működő számológép, ami alatt rejtett folyamat fut.
* **🧵 Thread Injection:** A kártékony kód külön szálon indul, így a főprogram (számológép) nem fagy le, és a felhasználó nem gyanakszik.
* **🔄 Silent Execution:** A háttérfolyamat láthatatlan marad a felhasználói felületen.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtár:** `threading`, `subprocess`
* **Módszer:** Backdooring legitimate scripts.

## 🚀 Használat
```bash
python legit_calculator.py
