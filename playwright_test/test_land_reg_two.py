from playwright.async_api import Page, expect
import re
import pathlib

reg = ["ELDRITCH LIMITED",
       "QUEENTON LIMITED",
       "DUNBAR VENTURES CORP.",
       "GESTRUST SA",
       "BARMOUTH LIMITED",
       "DREEMGARROW LIMITED",
       "KAA CONSULTING S.A. BVI"]

url = 'https://find-and-update.company-information.service.gov.uk/'


def test_land_reg_two(page: Page):
    page.goto(url)
    page.get_by_text("Reject analytics cookies").click()
    search_box = page.get_by_placeholder("Start here...")
    for item in reg:
        try:
            search_box.fill(item)
            page.get_by_role("button", name="Search").click()
            search_link = page.get_by_role("link", name=item[:8]).first
            search_content = search_link.text_content()
            if item[:8] in search_content().strip():
                search_link.click()
                title = page.title()
                print(title)
                page.goto(url)
            else:
                page.goto(url)

        except (NameError, TimeoutError) as exception:
            print(f"{exception} found")
            page.goto(url)
    page.close()

