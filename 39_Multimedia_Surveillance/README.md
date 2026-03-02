# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 📸 Project 39: Multimedia Surveillance (Spyware)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-PyAutoGUI-orange?style=flat-square)
![Category](https://img.shields.io/badge/Category-Spyware-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt egy kémprogram (Spyware) multimédiás képességeit mutatja be. A szoftver képes távolról képernyőmentéseket készíteni az áldozat asztaláról, és azokat automatikusan továbbítani a támadó szerverére.

## 🛠️ Funkciók
* **👀 Desktop Capture:** Teljes felbontású képernyőkép készítése a `pyautogui` segítségével.
* **📤 Auto-Upload:** A képek automatikus feltöltése TCP socketen keresztül.
* **🕵️ Stealth Transfer:** Az adatátvitel bináris streamként történik.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Függőség:** `pyautogui`, `socket`
* **Felhasználás:** Remote Administration Tool (RAT) funkciók demonstrálása.

## 🚀 Használat
1. **Szerver:** `python screenshot_server.py`
2. **Kliens:** `python screenshot_client.py`
