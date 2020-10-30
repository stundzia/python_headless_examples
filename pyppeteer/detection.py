import asyncio

import pyppeteer
from pyppeteer_stealth import stealth


TEST_URL = "https://arh.antoinevastel.com/bots/areyouheadless"


async def main():
    # NOTE: even without stealth applied pyppeteer will not get detected if
    # running in headful mode.
    browser = await pyppeteer.launcher.launch(options={'headless': True})
    pages = await browser.pages()
    page = pages[0]

    await page.goto(TEST_URL)
    await asyncio.sleep(3)
    # Save page screenshot to unstealthed_status.png
    await page.screenshot({'path': 'unstealthed_status.png', 'fullPage': 'true'})

    page = await browser.newPage()
    # Should not get caught with stealth.
    await stealth(page)

    await page.goto(TEST_URL)
    await asyncio.sleep(3)
    # Save page screenshot to stealthed_status.png
    await page.screenshot({'path': 'stealthed_status.png', 'fullPage': 'true'})
    await browser.close()


if __name__ == '__main__':
    asyncio.run(main())




