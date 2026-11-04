
import os
import pytest
import mysql.connector
import main


@pytest.fixture
def db():
    spojeni = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="spravce_ukolu_test"
    )

    main.vytvoreni_tabulky(spojeni)

    kurzor = spojeni.cursor()
    kurzor.execute("DELETE FROM ukoly")
    spojeni.commit()
    kurzor.close()

    yield spojeni

    kurzor = spojeni.cursor()
    kurzor.execute("DELETE FROM ukoly")
    spojeni.commit()
    kurzor.close()
    spojeni.close()


def vytvor_testovaci_ukol(db):
    kurzor = db.cursor()
    kurzor.execute(
        "INSERT INTO ukoly (nazev, popis) VALUES (%s, %s)",
        ("Testovací úkol", "Testovací popis")
    )
    db.commit()

    id_ukolu = kurzor.lastrowid
    kurzor.close()

    return id_ukolu


def test_pridat_ukol_pozitivni(db, monkeypatch):
    odpovedi = iter(["Nakoupit", "Koupit chleba"])
    monkeypatch.setattr("builtins.input", lambda _: next(odpovedi))

    main.pridat_ukol(db)

    kurzor = db.cursor()
    kurzor.execute("SELECT nazev, popis, stav FROM ukoly")
    ukol = kurzor.fetchone()
    kurzor.close()

    assert ukol == ("Nakoupit", "Koupit chleba", "Nezahájeno")


def test_pridat_ukol_negativni(db, monkeypatch, capsys):
    odpovedi = iter(["", "Koupit chleba", "Nakoupit", "Koupit chleba"])
    monkeypatch.setattr("builtins.input", lambda _: next(odpovedi))

    main.pridat_ukol(db)

    vystup = capsys.readouterr().out

    kurzor = db.cursor()
    kurzor.execute("SELECT COUNT(*) FROM ukoly")
    pocet = kurzor.fetchone()[0]
    kurzor.close()

    assert "nesmí být prázdné" in vystup
    assert pocet == 1


def test_aktualizovat_ukol_pozitivni(db, monkeypatch):
    id_ukolu = vytvor_testovaci_ukol(db)

    odpovedi = iter([str(id_ukolu), "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(odpovedi))

    main.aktualizovat_ukol(db)

    kurzor = db.cursor()
    kurzor.execute(
        "SELECT stav FROM ukoly WHERE id = %s",
        (id_ukolu,)
    )
    stav = kurzor.fetchone()[0]
    kurzor.close()

    assert stav == "Hotovo"


def test_aktualizovat_ukol_negativni(db, monkeypatch, capsys):
    id_ukolu = vytvor_testovaci_ukol(db)

    odpovedi = iter(["0", str(id_ukolu), "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(odpovedi))

    main.aktualizovat_ukol(db)

    vystup = capsys.readouterr().out

    kurzor = db.cursor()
    kurzor.execute(
        "SELECT stav FROM ukoly WHERE id = %s",
        (id_ukolu,)
    )
    stav = kurzor.fetchone()[0]
    kurzor.close()

    assert "Takový úkol neexistuje" in vystup
    assert stav == "Probíhá"


def test_odstranit_ukol_pozitivni(db, monkeypatch):
    id_ukolu = vytvor_testovaci_ukol(db)

    odpovedi = iter([str(id_ukolu), "ano"])
    monkeypatch.setattr("builtins.input", lambda _: next(odpovedi))

    main.odstranit_ukol(db)

    kurzor = db.cursor()
    kurzor.execute(
        "SELECT id FROM ukoly WHERE id = %s",
        (id_ukolu,)
    )
    ukol = kurzor.fetchone()
    kurzor.close()

    assert ukol is None


def test_odstranit_ukol_negativni(db, monkeypatch, capsys):
    id_ukolu = vytvor_testovaci_ukol(db)

    odpovedi = iter(["0", str(id_ukolu), "ne"])
    monkeypatch.setattr("builtins.input", lambda _: next(odpovedi))

    main.odstranit_ukol(db)

    vystup = capsys.readouterr().out

    kurzor = db.cursor()
    kurzor.execute(
        "SELECT id FROM ukoly WHERE id = %s",
        (id_ukolu,)
    )
    ukol = kurzor.fetchone()
    kurzor.close()

    assert "Takový úkol neexistuje" in vystup
    assert ukol is not None
