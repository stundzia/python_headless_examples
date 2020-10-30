import asyncio

import pyppeteer


async def main():
    browser = await pyppeteer.launcher.launch(options={'headless': False})
    pages = await browser.pages()
    page = pages[0]
    await page.goto('https://www.whatismybrowser.com/detect/what-is-my-user-agent')
    await asyncio.sleep(5)
    await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
