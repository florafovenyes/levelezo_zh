"""
4. feladat – Új programrész implementálása (5 pont)

Feladat:
Készíts egy CSV fájlt feldolgozó programot, amely környezetvédelmi adatokat kezel.

A CSV fájl szerkezete a következő:
- varos (szöveg)
- ev (szám)
- szennyezettseg_szint (0–100 közötti szám)
- vizszennyezettseg (igen/nem)

Minden függvény 1 pontot ér.

---

1. adatok_beolvasasa(fajlnev)
- Olvasd be a megadott CSV fájl tartalmát (az első sor fejléc).
- A visszatérési érték egy lista legyen, amely sorokat tartalmaz.
  Minden sor egy szótár (dict) az oszlopokkal vagy lista az oszlopok értékeivel.
- Hiba esetén térj vissza üres listával.

---

2. szures_varos_szerint(adatok, varos_nev)
- Szűrd ki azokat a sorokat, amelyek a megadott városhoz tartoznak.
- Példa:
  szures_varos_szerint(adatok, "Budapest") → csak a budapesti sorok

---

3. atlag_szennyezettseg(adatok)
- Számold ki a szennyezettseg_szint értékek átlagát.
- A visszatérési érték egy szám legyen (pl. 45.5).
- Ügyelj arra, hogy az értékeket számként kezeld.

---

4. vizszennyezetseg_statisztika(adatok)
- Számold meg, hány "igen" és hány "nem" szerepel a vizszennyezettseg oszlopban.
- A visszatérési érték egy szótár legyen:
  {"igen": 3, "nem": 5}

---

5. szurt_csv_mentes(adatok, fajlnev, minimum_szint)
- Mentsd ki egy új CSV fájlba azokat a sorokat, ahol:
  szennyezettseg_szint >= minimum_szint
- A kimeneti fájl első sora legyen a fejléc:
  varos,ev,szennyezettseg_szint,vizszennyezettseg

---

"""
import csv

def adatok_beolvasasa(fajlnev):
    try:
        adatok = []

        with open(fajlnev, mode="r", encoding="utf-8") as fajl:
            olvaso = csv.DictReader(fajl)

            for sor in olvaso:
                adatok.append(sor)

        return adatok

    except:
        return []
def szures_varos_szerint(adatok, varos_nev):
    eredmeny = []

    for sor in adatok:
        if sor["varos"] == varos_nev:
            eredmeny.append(sor)

    return eredmeny


def atlag_szennyezettseg(adatok):
    if not adatok:
        return 0

    osszeg = 0

    for sor in adatok:
        osszeg += float(sor["szennyezettseg_szint"])

    return osszeg / len(adatok)


def vizszennyezetseg_statisztika(adatok):
    statisztika = {
        "igen": 0,
        "nem": 0
    }

    for sor in adatok:
        ertek = sor["vizszennyezettseg"].lower()

        if ertek == "igen":
            statisztika["igen"] += 1
        elif ertek == "nem":
            statisztika["nem"] += 1

    return statisztika


def szurt_csv_mentes(adatok, fajlnev, minimum_szint):
    with open(fajlnev, mode="w", newline="", encoding="utf-8") as fajl:

        mezok = [
            "varos",
            "ev",
            "szennyezettseg_szint",
            "vizszennyezettseg"
        ]

        iro = csv.DictWriter(fajl, fieldnames=mezok)

        # fejléc írása
        iro.writeheader()

        # szűrt adatok mentése
        for sor in adatok:
            if float(sor["szennyezettseg_szint"]) >= minimum_szint:
                iro.writerow(sor)


if __name__ == "__main__":

    # példa használat
    adatok = adatok_beolvasasa("kornyezet.csv")

    print("Összes adat:")
    print(adatok)

    print("\nBudapesti adatok:")
    print(szures_varos_szerint(adatok, "Budapest"))

    print("\nÁtlag szennyezettség:")
    print(atlag_szennyezettseg(adatok))

    print("\nVízszennyezettség statisztika:")
    print(vizszennyezetseg_statisztika(adatok))

    # mentés
    szurt_csv_mentes(adatok, "szurt_adatok.csv", 50)

    print("\nA szűrt fájl mentése megtörtént.")