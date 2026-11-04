# Testovací případy – Správce úkolů

**Testovaný soubor:** `main.py`  
**Způsob testování:** Manuální testování v terminálu VS Code  
**Počet testů:** 14  
**Výsledek:** 14 PASS, 0 FAIL

Testy byly provedeny ručním zadáváním hodnot do programu. U každého testu jsem porovnal očekávaný výsledek se skutečným výsledkem.

## Funkce hlavni_menu()

### Test 1 – Platná volba v menu

- **Popis:** Ověření, že možnost 2 zobrazí úkoly.
- **Předpoklady:** Seznam úkolů je prázdný.
- **Postup:** Spustit program, v menu zadat `2` a potom `4`.
- **Očekávaný výsledek:** Zobrazí se zpráva „Žádné úkoly.“ a program se ukončí.
- **Skutečný výsledek:** Zobrazily se zprávy „Žádné úkoly.“ a „Konec programu“.
- **Stav:** PASS
- **Poznámky:** Ověřena platná volba a návrat do menu.

### Test 2 – Neplatná volba v menu

- **Popis:** Ověření reakce na neplatnou volbu.
- **Předpoklady:** Program je spuštěný.
- **Postup:** V menu zadat `8` a potom `4`.
- **Očekávaný výsledek:** Program upozorní na neplatnou volbu a zobrazí menu znovu.
- **Skutečný výsledek:** Vypsalo se „Neplatná volba, zkus to znovu.“ a menu se zobrazilo znovu.
- **Stav:** PASS
- **Poznámky:** Ověřen chybný vstup.

### Test 3 – Ukončení programu

- **Popis:** Ověření ukončení programu.
- **Předpoklady:** Program je spuštěný.
- **Postup:** V menu zadat `4`.
- **Očekávaný výsledek:** Program vypíše „Konec programu“ a ukončí se.
- **Skutečný výsledek:** Zpráva se zobrazila a program se ukončil.
- **Stav:** PASS
- **Poznámky:** Ověřeno správné ukončení programu.

## Funkce pridat_ukol()

### Test 4 – Přidání platného úkolu

- **Popis:** Přidání úkolu s vyplněným názvem i popisem.
- **Předpoklady:** Seznam úkolů je prázdný.
- **Postup:** V menu vybrat `1`, zadat název `Domácí úkol` a popis `Dokončit cvičení`. Potom vybrat `2`.
- **Očekávaný výsledek:** Úkol se uloží do seznamu a zobrazí se potvrzení.
- **Skutečný výsledek:** Program vypsal „Úkol byl přidán.“ a úkol se zobrazil v seznamu.
- **Stav:** PASS
- **Poznámky:** Ověřeno správné přidání úkolu.

### Test 5 – Prázdný název

- **Popis:** Ověření, že prázdný název není přijat.
- **Předpoklady:** Seznam úkolů je prázdný.
- **Postup:** V menu vybrat `1`, nechat název prázdný a zadat popis `Dokončit cvičení`. Potom znovu zadat název `Domácí úkol` a popis `Dokončit cvičení`.
- **Očekávaný výsledek:** Program upozorní na prázdný údaj a požádá o oba údaje znovu.
- **Skutečný výsledek:** Program zobrazil upozornění a po opětovném zadání přidal právě jeden úkol.
- **Stav:** PASS
- **Poznámky:** Ověřeno opakované zadávání.

### Test 6 – Prázdný popis

- **Popis:** Ověření, že prázdný popis není přijat.
- **Předpoklady:** Seznam úkolů je prázdný.
- **Postup:** V menu vybrat `1`, zadat název `Domácí úkol` a popis nechat prázdný. Potom zadat oba údaje správně.
- **Očekávaný výsledek:** Program upozorní na prázdný údaj a požádá o oba údaje znovu.
- **Skutečný výsledek:** Program zobrazil upozornění a po opětovném zadání přidal právě jeden úkol.
- **Stav:** PASS
- **Poznámky:** Ověřeno opakované zadávání.

## Funkce zobrazit_ukoly()

### Test 7 – Prázdný seznam

- **Popis:** Zobrazení seznamu bez uložených úkolů.
- **Předpoklady:** Seznam úkolů je prázdný.
- **Postup:** Spustit program a v menu vybrat `2`.
- **Očekávaný výsledek:** Program vypíše „Žádné úkoly.“
- **Skutečný výsledek:** Zobrazilo se „Žádné úkoly.“
- **Stav:** PASS
- **Poznámky:** Ověřen prázdný seznam.

### Test 8 – Zobrazení dvou úkolů

- **Popis:** Ověření zobrazení více úkolů.
- **Předpoklady:** V seznamu jsou úkoly `Úklid – Pokoj` a `Škola – Úkol`.
- **Postup:** Pomocí možnosti `1` přidat oba úkoly. Potom v menu vybrat `2`.
- **Očekávaný výsledek:** Zobrazí se oba úkoly očíslované od 1.
- **Skutečný výsledek:** Program vypsal `1. Úklid - Pokoj` a `2. Škola - Úkol`.
- **Stav:** PASS
- **Poznámky:** Ověřeno správné číslování úkolů.

## Funkce odstranit_ukol()

### Test 9 – Odstranění existujícího úkolu

- **Popis:** Odstranění prvního úkolu ze dvou.
- **Předpoklady:** V seznamu jsou úkoly `Úklid – Pokoj` a `Škola – Úkol`.
- **Postup:** V menu vybrat `3`, zadat číslo `1` a potom vybrat `2` pro kontrolu seznamu.
- **Očekávaný výsledek:** První úkol se odstraní a druhý zůstane.
- **Skutečný výsledek:** Program vypsal „Úkol byl odstraněn.“ a v seznamu zůstal pouze úkol `Škola – Úkol`.
- **Stav:** PASS
- **Poznámky:** Ověřeno odstranění správného úkolu.

### Test 10 – Odstranění z prázdného seznamu

- **Popis:** Pokus odstranit úkol, když žádný není uložený.
- **Předpoklady:** Seznam úkolů je prázdný.
- **Postup:** Spustit program a v menu vybrat `3`.
- **Očekávaný výsledek:** Program upozorní, že nejsou žádné úkoly k odstranění.
- **Skutečný výsledek:** Zobrazilo se „Žádné úkoly k odstranění.“
- **Stav:** PASS
- **Poznámky:** Program nepožadoval číslo úkolu.

### Test 11 – Neexistující číslo úkolu

- **Popis:** Pokus odstranit úkol mimo rozsah seznamu.
- **Předpoklady:** V seznamu je jeden úkol `Úklid – Pokoj`.
- **Postup:** V menu vybrat `3`, zadat číslo `5` a potom vybrat `2`.
- **Očekávaný výsledek:** Program upozorní, že úkol neexistuje, a seznam nezmění.
- **Skutečný výsledek:** Zobrazilo se „Takový úkol neexistuje.“ a úkol zůstal uložený.
- **Stav:** PASS
- **Poznámky:** Ověřeno číslo mimo rozsah.

### Test 12 – Text místo čísla

- **Popis:** Pokus zadat nečíselný vstup.
- **Předpoklady:** V seznamu je jeden úkol `Úklid – Pokoj`.
- **Postup:** V menu vybrat `3`, zadat `abc` a potom vybrat `2`.
- **Očekávaný výsledek:** Program upozorní na neplatný vstup a úkol neodstraní.
- **Skutečný výsledek:** Zobrazilo se „Musíš zadat číslo.“ a úkol zůstal uložený.
- **Stav:** PASS
- **Poznámky:** Ověřen textový vstup.

### Test 13 – Mezery místo čísla

- **Popis:** Pokus zadat pouze mezery.
- **Předpoklady:** V seznamu je jeden úkol `Úklid – Pokoj`.
- **Postup:** V menu vybrat `3`, místo čísla zadat tři mezery a potom vybrat `2`.
- **Očekávaný výsledek:** Program odmítne vstup a úkol neodstraní.
- **Skutečný výsledek:** Zobrazilo se „Musíš zadat číslo.“ a úkol zůstal uložený.
- **Stav:** PASS
- **Poznámky:** Ověřen hraniční vstup.

### Test 14 – Záporné číslo

- **Popis:** Pokus zadat záporné číslo úkolu.
- **Předpoklady:** V seznamu je jeden úkol `Úklid – Pokoj`.
- **Postup:** V menu vybrat `3`, zadat `-1` a potom vybrat `2`.
- **Očekávaný výsledek:** Program odmítne vstup a úkol neodstraní.
- **Skutečný výsledek:** Zobrazilo se „Musíš zadat číslo.“ a úkol zůstal uložený.
- **Stav:** PASS
- **Poznámky:** Program záporné číslo odmítá při kontrole `isdigit()`.

## Závěr

Bylo provedeno 14 manuálních testů, které pokrývají všechny čtyři funkce programu.

Všechny testy skončily výsledkem **PASS**. Program správně reagoval na platné i neplatné vstupy.

Při testování nebyla nalezena žádná chyba.