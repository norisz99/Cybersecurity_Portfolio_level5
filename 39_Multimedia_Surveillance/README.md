# 📸 Project 39: Multimedia Surveillance (The Eye)

**Focus:** Binary Data Transmission, Custom Protocols, Spyware Capabilities

## 📌 Áttekintés
A szöveges parancsokon túl egy modern RAT (Remote Access Trojan) képes multimédiás adatok megszerzésére is. Ez a projekt bemutatja, hogyan lehet képernyőképet készíteni az áldozat gépén, és azt bináris adatfolyamként átküldeni a hálózaton.
A projekt egyedi protokollt implementál a fájlméret és az adatstruktúra kezelésére, biztosítva a képfájlok sérülésmentes átvitelét.

## 🛠 Fájlok
* `screenshot_server.py`: Fogadja a bináris adatfolyamot és visszaállítja `.png` képpé.
* `screenshot_client.py`: A `pyautogui` könyvtárat használva képet készít, és elküldi a szervernek.

## 🚀 Használat
1.  Telepítsd a függőséget: `pip install pyautogui`
2.  Indítsd el a szervert:
    ```bash
    python screenshot_server.py
    ```
3.  Futtasd a klienst.
4.  Ellenőrizd a szerver mappáját: Megjelenik a `victim_screen.png`.

## 🧠 Mit tanultam?
* Bináris fájlok (képek) kezelése Socket kapcsolaton keresztül.
* Egyedi hálózati protokoll tervezése (Header + Payload).
* A `pyautogui` könyvtár használata automatizációra és megfigyelésre.

---
**⚠️ Disclaimer:** Ez a szoftver a kémprogramok működési elvét demonstrálja. Mások megfigyelése beleegyezésük nélkül súlyos bűncselekmény.