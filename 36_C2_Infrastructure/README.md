# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 📡 Project 36: Custom C2 Infrastructure

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Library](https://img.shields.io/badge/Lib-Socket-yellow?style=flat-square)
![Category](https://img.shields.io/badge/Category-C2_Framework-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a projekt egy saját fejlesztésű **Command & Control (C2)** szerver alapjait fekteti le. A modern kiberbűnözésben a C2 szerverek "karmesterként" irányítják a fertőzött gépek (botnet) hálózatát. Ez a kód demonstrálja, hogyan épül fel a kommunikációs csatorna a támadó és az áldozat között.

## 🛠️ Funkciók
* **Multi-Client Handling:** Képes több "fertőzött" kliens egyidejű kezelésére (Threading).
* **Heartbeat Protocol:** Folyamatos kapcsolatellenőrzés (Keep-Alive jelek), hogy tudjuk, melyik bot aktív.
* **Remote Shell:** Parancsok küldése és a kimenet fogadása valós időben.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Protokoll:** TCP Socket Stream
* **Architektúra:** Server-Client modell

## 🚀 Használat
```bash
python c2_server.py
