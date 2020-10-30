import asyncio

from playwright import async_playwright as playwright


F1LT_USER = 'user'
F1LT_PASSWORD = 'password'


async def login():
    async with playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.newPage()
        await page.goto('https://www.f-1.lt/')
        await asyncio.sleep(1.0)
        # Click login button
        await page.click('css=#navbar > ul.nav.navbar-nav > li:nth-child(8) > a')
        await asyncio.sleep(0.5)
        # Enter username
        await page.fill('input#login-username', F1LT_USER)
        await asyncio.sleep(1.0)
        # Enter password
        await page.fill('css=input#login-password', F1LT_PASSWORD)
        await asyncio.sleep(1.0)
        # Click login button
        await page.click('button#login-button')
        await asyncio.sleep(4.5)
        await browser.close()


async def get_team_standings():
    async with playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.newPage()
        await page.goto('https://www.f-1.lt/')
        await page.click('"Komandos (10)"')
        await asyncio.sleep(1.0)
        await page.click('ul#komandos >> text="Išskleisti "')
        await asyncio.sleep(2.5)
        await browser.close()


async def main():
    await get_team_standings()
    await login()

if __name__ == '__main__':
    asyncio.run(main())
