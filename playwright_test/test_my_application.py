import re
from playwright.sync_api import Page, expect
import logging


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page, caplog):
    caplog.set_level(logging.INFO)
    page.goto("http://65.21.1.10:9099")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("OrangeHRM"))
    page.get_by_placeholder('username').fill('zubbyik')
    page.get_by_placeholder('password').fill('!1Winner75')
    page.get_by_role('button', name='Login')
    client_banner = page.get_by_role('img', name="client brand banner")
    expect(client_banner).to_be_visible()
    logging.info('This is just info')
    logging.warning('dont try this')
    # create a locator
    # get_started = page.get_by_role("link", name="Get started")
    # Expect an attribute "to be strictly equal" to the value.
    # expect(get_started).to_have_attribute("href", "/docs/intro")

    page.close()
