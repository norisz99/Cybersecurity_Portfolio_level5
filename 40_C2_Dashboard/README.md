# 👑 Project 40: C2 Dashboard (The Mastermind)

**Focus:** Botnet Management, UI/UX for Hackers, Multi-client Handling, Scalability

## 📌 Áttekintés
A **Level 5** záróprojektje. Ez a script egyesíti az előző leckéket egyetlen, központi vezérlőpultban. A Dashboard lehetővé teszi a támadó számára, hogy egyszerre több fertőzött gépet ("Zombit") kövessen nyomon, listázza őket, és kiválassza, melyiket szeretné irányítani.
Ez a szimulációja egy valódi Botnet vezérlő felületnek.

## 🛠 Fájlok
* `c2_commander.py`: A Fővezérlő. Tartalmazza a szervert (külön szálon), a zombik listáját és a parancssori interfészt (CLI).

## ✨ Funkciók
* **Multi-Client Support:** Egyszerre több gép is csatlakozhat.
* **Target Selection:** A `use <ID>` paranccsal válthatunk a gépek között.
* **Interactive Shell:** Teljes hozzáférés a kiválasztott gép parancssorához.
* **Professional UI:** ASCII Art és strukturált menürendszer.

## 🚀 Használat
1.  Indítsd el a Dashboardot:
    ```bash
    python c2_commander.py
    ```
2.  Indíts el több klienst (pl. `malicious_client.py`) különböző terminálablakokban.
3.  A Dashboardon írd be: `list` (látni fogod a csatlakozott gépeket).
4.  Válassz egyet: `use 1`.
5.  Add ki a parancsokat, majd írd be: `back` a menübe visszalépéshez.

---
**⚠️ Disclaimer:** Ez a projekt a Botnet hálózatok irányításának technikai hátterét mutatja be oktatási céllal.