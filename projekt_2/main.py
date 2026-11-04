import os
import mysql.connector


def pripojeni_db():
    try:
        spojeni = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("MYSQL_PASSWORD"),
            database="spravce_ukolu"
        )

        print("Připojení k databázi proběhlo úspěšně.")
        return spojeni

    except mysql.connector.Error as chyba:
        print("Chyba při připojení:", chyba)
        return None


def vytvoreni_tabulky(spojeni):
    kurzor = spojeni.cursor()

    kurzor.execute("""
        CREATE TABLE IF NOT EXISTS ukoly (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nazev VARCHAR(255) NOT NULL,
            popis TEXT NOT NULL,
            stav VARCHAR(20) DEFAULT 'Nezahájeno',
            datum_vytvoreni TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    kurzor.close()
    print("Tabulka ukoly je připravena.")

def pridat_ukol(spojeni):
    while True:
        nazev = input("Zadej název úkolu: ").strip()
        popis = input("Zadej popis úkolu: ").strip()

        if nazev != "" and popis != "":
            break

        print("Název a popis nesmí být prázdné. Zadej je znovu.")

    kurzor = spojeni.cursor()

    sql = "INSERT INTO ukoly (nazev, popis) VALUES (%s, %s)"
    kurzor.execute(sql, (nazev, popis))

    spojeni.commit()
    kurzor.close()

    print("Úkol byl přidán.")

def zobrazit_ukoly(spojeni):
    kurzor = spojeni.cursor()

    kurzor.execute("""
        SELECT id, nazev, popis, stav
        FROM ukoly
        WHERE stav = 'Nezahájeno' OR stav = 'Probíhá'
    """)

    ukoly = kurzor.fetchall()
    kurzor.close()

    if len(ukoly) == 0:
        print("Žádné aktivní úkoly.")
        return

    print("\nSeznam úkolů:")

    for ukol in ukoly:
        print(f"{ukol[0]}. {ukol[1]} - {ukol[2]} - {ukol[3]}")

def aktualizovat_ukol(spojeni):
    kurzor = spojeni.cursor()

    kurzor.execute("SELECT id, nazev, stav FROM ukoly")
    ukoly = kurzor.fetchall()

    if len(ukoly) == 0:
        print("Žádné úkoly k aktualizaci.")
        kurzor.close()
        return

    print("\nSeznam úkolů:")
    for ukol in ukoly:
        print(f"{ukol[0]}. {ukol[1]} - {ukol[2]}")

    while True:
        cislo = input("Zadej ID úkolu: ")

        if not cislo.isdigit():
            print("Musíš zadat číslo.")
            continue

        kurzor.execute(
            "SELECT id FROM ukoly WHERE id = %s",
            (int(cislo),)
        )

        if kurzor.fetchone() is not None:
            break

        print("Takový úkol neexistuje. Zkus to znovu.")

    print("1 - Probíhá")
    print("2 - Hotovo")

    while True:
        volba = input("Vyber nový stav: ")

        if volba == "1":
            stav = "Probíhá"
            break
        elif volba == "2":
            stav = "Hotovo"
            break
        else:
            print("Neplatná volba.")

    kurzor.execute(
        "UPDATE ukoly SET stav = %s WHERE id = %s",
        (stav, int(cislo))
    )

    spojeni.commit()
    kurzor.close()

    print("Stav úkolu byl změněn.")
def odstranit_ukol(spojeni):
    kurzor = spojeni.cursor()

    kurzor.execute("SELECT id, nazev, stav FROM ukoly")
    ukoly = kurzor.fetchall()

    if len(ukoly) == 0:
        print("Žádné úkoly k odstranění.")
        kurzor.close()
        return

    print("\nSeznam úkolů:")
    for ukol in ukoly:
        print(f"{ukol[0]}. {ukol[1]} - {ukol[2]}")

    while True:
        cislo = input("Zadej ID úkolu k odstranění: ")

        if not cislo.isdigit():
            print("Musíš zadat číslo.")
            continue

        kurzor.execute(
            "SELECT id FROM ukoly WHERE id = %s",
            (int(cislo),)
        )

        if kurzor.fetchone() is not None:
            break

        print("Takový úkol neexistuje. Zkus to znovu.")

    potvrzeni = input("Opravdu chceš úkol odstranit? (ano/ne): ")

    if potvrzeni.lower() == "ano":
        kurzor.execute(
            "DELETE FROM ukoly WHERE id = %s",
            (int(cislo),)
        )
        spojeni.commit()
        print("Úkol byl odstraněn.")
    else:
        print("Odstranění bylo zrušeno.")

    kurzor.close()


def hlavni_menu(spojeni):
    while True:
        print("\nSprávce úkolů")
        print("1 - Přidat úkol")
        print("2 - Zobrazit úkoly")
        print("3 - Aktualizovat úkol")
        print("4 - Odstranit úkol")
        print("5 - Ukončit program")

        volba = input("Vyber možnost (1-5): ")

        if volba == "1":
            pridat_ukol(spojeni)
        elif volba == "2":
            zobrazit_ukoly(spojeni)
        elif volba == "3":
            aktualizovat_ukol(spojeni)
        elif volba == "4":
            odstranit_ukol(spojeni)
        elif volba == "5":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkus to znovu.")




if __name__ == "__main__":
    spojeni = pripojeni_db()

    if spojeni is not None:
        vytvoreni_tabulky(spojeni)
        hlavni_menu(spojeni)
        spojeni.close()