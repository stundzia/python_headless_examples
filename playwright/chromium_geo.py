import asyncio

from playwright import async_playwright as playwright


async def main():
    async with playwright() as p:
        browser = await p.chromium.launch(headless=False)
        iphone_11 = p.devices['iPhone 11 Pro']
        context = await browser.newContext(
            **iphone_11,
            locale='en-US',
            geolocation={'longitude': 54.3773438, 'latitude': 24.453884},  # Abu Dhabi
            permissions=['geolocation']
        )
        page = await context.newPage()

        # Working geo example
        await page.goto('https://whatmylocation.com/')
        await asyncio.sleep(3.0)
        await page.screenshot(path='iphone-abu-dhabi-whatmylocation.png')

        # Google failing example (geo is not browser geo)
        await page.goto('https://www.google.com/search?q=nearest+bar')
        await asyncio.sleep(1)
        await page.click('text="Sutinku"')

        await asyncio.sleep(5)
        await page.screenshot(path='iphone-abu-dhabi-google.png')
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
