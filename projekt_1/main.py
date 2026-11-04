ukoly = []


def hlavni_menu():
    while True:
        print("\nSprávce úkolů")
        print("1 - Přidat úkol")
        print("2 - Zobrazit úkoly")
        print("3 - Odstranit úkol")
        print("4 - Konec")

        volba = input("Vyber možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu")
            break
        else:
            print("Neplatná volba, zkus to znovu.")


def pridat_ukol():
    while True:
        nazev = input("Zadej název úkolu: ").strip()
        popis = input("Zadej popis úkolu: ").strip()

        if nazev != "" and popis != "":
            ukoly.append([nazev, popis])
            print("Úkol byl přidán.")
            break

        print("Název ani popis nesmí být prázdný. Zadej oba údaje znovu.")


def zobrazit_ukoly():
    if len(ukoly) == 0:
        print("Žádné úkoly.")
        return

    print("\nSeznam úkolů:")
    for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. {ukol[0]} - {ukol[1]}")


def odstranit_ukol():
    if len(ukoly) == 0:
        print("Žádné úkoly k odstranění.")
        return

    zobrazit_ukoly()
    cislo = input("Zadej číslo úkolu k odstranění: ")

    if not cislo.isdigit():
        print("Musíš zadat číslo.")
        return

    cislo = int(cislo)

    if cislo < 1 or cislo > len(ukoly):
        print("Takový úkol neexistuje.")
        return

    ukoly.pop(cislo - 1)
    print("Úkol byl odstraněn.")


if __name__ == "__main__":
    hlavni_menu()