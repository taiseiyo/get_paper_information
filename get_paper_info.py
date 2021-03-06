#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import time
import sys


def run(playwright):
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()
    word = sys.argv[1]
    # Open new page
    page = context.new_page()

    # Go to https://ieeexplore.ieee.org/Xplore/home.jsp
    page.goto("https://ieeexplore.ieee.org/Xplore/home.jsp")

    # Click [aria-label="Enter search text"]
    page.click("[aria-label=\"Enter search text\"]")

    # Fill [aria-label="Enter search text"]
    page.fill("[aria-label=\"Enter search text\"]", word)

    # Click [aria-label="Search"]
    page.click("[aria-label=\"Search\"]")
    # assert page.url == "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=graph%20neural%20network"

    # Go to https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=graph%20neural%20network
    page.goto("https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=graph%20neural%20network")

    # Check text=Select All on PageSort By:Sort ByRelevance >> input[type="checkbox"]
    page.check(
        "text=Select All on PageSort By:Sort ByRelevance >> input[type=\"checkbox\"]")

    # Click button:has-text("Export")
    page.click("button:has-text(\"Export\")")

    # Click a[role="tab"]:has-text("Citations")
    page.click("a[role=\"tab\"]:has-text(\"Citations\")")

    # Click label:has-text("Citation & Abstract")
    page.click("label:has-text(\"Citation & Abstract\")")

    # Click :nth-match(input[name="citations-format"], 2)
    page.click(":nth-match(input[name=\"citations-format\"], 2)")

    # Click div[role="tabpanel"] >> text=Export
    with page.expect_popup() as popup_info:
        page.click("div[role=\"tabpanel\"] >> text=Export")
    page1 = popup_info.value
    time.sleep(5)
    print(page1.content())
    # Close page
    page.close()
    # Close page
    page1.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
