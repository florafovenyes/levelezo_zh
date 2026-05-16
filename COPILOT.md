# COPILOT - Beszélgetési előzmények (kivonat)

Generálva: 2026-05-16

Ez a fájl a jelenlegi munkamenet főbb promptjait és a kapcsolódó instrukciókat rögzíti (elsősorban a rendszer-, fejlesztő- és felhasználói üzenetek).

## Rendszerüzenet (röviden)
- Tudásvágási dátum: 2024-06
- Aktuális dátum a munkamenetben: 2026-05-16
- Készen álló AI asszisztens munkavégzésre a megadott eszközök használatával.

## Fejlesztői instrukciók (összefoglaló)
- Viselkedj mint egy haladó szintű programozási asszisztens (GitHub Copilot jellegű).
- Kövesd a megadott eszközhasználati szabályokat: fájlok szerkesztéséhez `apply_patch` vagy `create_file` használata, olvasáshoz `read_file`, kereséshez `semantic_search`/`grep_search` stb.
- Előforduló szabályok kiemelve: mindig törekedj a teljes megoldásra, ne fejezd be a kört addig, amíg minden feladat nincs kijavítva; módosítások után ellenőrizd a hibákat `get_errors`-szel (ha alkalmazható).
- Ha új fájlt hozol létre, használd a `create_file` eszközt a munkaterületen.
- Amikor fájlokat szerkesztesz, adj rövid magyarázatot a változtatásról.

## Felhasználói (user) promptok és kapcsolódó mellékletek
1) Feladat: Implementálandó funkcionalitás (részlet a `4_uj_programresz_implementalasa.py` fájlból)
- 5. szurt_csv_mentes(adatok, fajlnev, minimum_szint)
  - Mentsd ki egy új CSV fájlba azokat a sorokat, ahol: szennyezettseg_szint >= minimum_szint
  - A kimeneti fájl első sora legyen a fejléc: varos,ev,szennyezettseg_szint,vizszennyezettseg

(Mellékelt fájl: `feladatok/4_uj_programresz_implementalasa.py` tartalom kivonattal.)

2) A felhasználó jelezte, hogy szeretné a választ magyarul: "magyarul"

3) Kérése a felhasználónak (aktuális):
- "Generálj egy COPILOT.md nevű fájlt, melybe a jelenlegi beszélgetés tartalma, elsősorban a promptok kerüljenek rögzítésre."

## Megjegyzés a projekt fájlokról
- Projektfa: `levelezo_zh/` tartalmazza a `feladatok/` mappát, és a `4_uj_programresz_implementalasa.py` fájlt, amelyben a `szurt_csv_mentes` függvény már szerepel és működőnek tűnik.

---

Ha szeretnéd, bővítem a fájlt a teljes beszélgetés teljes szövegével (asszisztens üzenetekkel és eszközhívások naplózásával), vagy létrehozok egy részletesebb változatot időbélyegzéssel.

