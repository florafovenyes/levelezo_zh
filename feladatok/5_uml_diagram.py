"""
5. feladat – UML tevékenységdiagram készítése (5 pont)

TODO:
Készíts egy UML tevékenységdiagramot az alábbi oldalon:
https://app.diagrams.net/

A diagram témája:
Kávéautomata működése

A folyamat:

1. START
2. Ital kiválasztása
3. Ellenőrzés: Van kávé az automatában?
   - NEM → Hibaüzenet: ez a fajta kávé elfogyott (END)
   - IGEN → továbblépés
4. Pénz bedobása
5. Döntés: Elég pénz érkezett?
   - NEM → további pénz bedobása (ciklus)
   - IGEN → kávé elkészítése
6. Ital kiadása
7. END

Minimális követelmények:
- Legalább 1 ciklus
- Legalább 1 külön elágazás (if-else)
- START és END csomópont
- Minimum 3 aktivitás

Használandó elemek:
- Oval → START / END
- Rectangle → aktivitások
- Diamond → döntések
- Arrow → kapcsolatok

Feladatok:
1. Nyisd meg a https://app.diagrams.net/ oldalt.
2. Készíts új diagramot (üres canvas).
3. Használj Flowchart elemeket.
4. Jelöld az IGEN / NEM ágakat.
5. Mentsd el .drawio vagy .png formátumban.
6. A kész képet töltsd fel GitHub-ra (a feladatok mellé) VAGY küldd el emailben az oktató címére.

Pontozás:
- START és END: 1 pont
- Ciklus helyes használata: 1 pont
- Elágazás helyes használata: 1 pont
- Minimum 3 aktivitás: 1 pont
- Helyes folyamatlogika: 1 pont
"""