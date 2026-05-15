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