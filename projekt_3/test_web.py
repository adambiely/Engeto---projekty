
import re
from playwright.sync_api import Page, expect


def test_hlavni_stranka(page: Page):
    page.goto("https://engeto.cz/")

    expect(page).to_have_title(re.compile("ENGETO", re.IGNORECASE))
    expect(page.locator("h1")).to_be_visible()
    expect(page).to_have_url("https://engeto.cz/")


def test_python_akademie(page: Page):
    page.goto("https://engeto.cz/python-akademie/")

    expect(page.locator("h1")).to_contain_text("Python Akademie")

    expect(
        page.get_by_role("heading", name="Průběh Python kurzu")
    ).to_be_visible()

    expect(
        page.get_by_role("link", name="Průběh Python kurzu")
    ).to_be_visible()


def test_terminy_kurzu(page: Page):
    page.goto("https://engeto.cz/terminy/")

    expect(page.locator("h1")).to_contain_text("Termíny kurzů")

    expect(
        page.get_by_role("checkbox", name="Python Python")
    ).to_be_visible()

    expect(
        page.get_by_role("checkbox", name="Testování softwaru Testování softwaru")
    ).to_be_visible()
