# ⚠️ LEGAL DISCLAIMER

**HU:** Ez az eszköz kizárólag **saját rendszerek tesztelésére** vagy a tulajdonos írásos engedélyével rendelkező hálózatokon használható. A szoftver oktatási céllal készült. A szerző (Paczok Norisz) elhárít minden felelősséget a jogellenes használatért vagy károkért.

**EN:** This tool is for **educational purposes and authorized testing only**. The creator (Paczok Norisz) assumes no liability for misuse or any damage caused by this program.

---

# 🎛️ Project 40: C2 Commander Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Interface](https://img.shields.io/badge/Interface-CLI-green?style=flat-square)
![Category](https://img.shields.io/badge/Category-C2_Admin-red?style=flat-square)

## 📌 Áttekintés (Overview)
Ez a modul a **Command & Control** infrastruktúra adminisztrátori felülete. Lehetővé teszi a "Bot Herder" (támadó) számára, hogy kényelmesen, egy központi konzolról irányítsa a fertőzött gépeket, parancsokat adjon ki, és megtekintse a státuszjelentéseket.

## 🛠️ Funkciók
* **📋 Bot List:** Aktív kapcsolatok listázása.
* **📢 Broadcast:** Parancs küldése az összes botnak egyszerre (pl. "DDoS indítása").
* **🎯 Targeted Command:** Parancs küldése egy specifikus ID-vel rendelkező botnak.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Interfész:** Command Line Interface (CLI)
* **Integráció:** A `36_C2_Infrastructure` modullal működik együtt.

## 🚀 Használat
```bash
python c2_commander.py
