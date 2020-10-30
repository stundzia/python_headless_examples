import asyncio

import pyppeteer


PROXY_HOST = '51.81.82.175'
PROXY_PORT = 80
PROXY_USERNAME = ''
PROXY_PASSWORD = ''


async def main():
    args = [
        '--start-maximized',
        '--no-sandbox',
        f'--proxy-server={PROXY_HOST}:{PROXY_PORT}',
    ]
    browser = await pyppeteer.launcher.launch(
        args=args,
        options={'headless': False},
    )
    pages = await browser.pages()
    page = pages[0]

    if PROXY_USERNAME and PROXY_PASSWORD:
        await page.authenticate(
            credentials={
                'username': PROXY_USERNAME,
                'password': PROXY_PASSWORD,
            },
        )

    await page.goto('http://httpbin.org/ip')
    await asyncio.sleep(1)
    content = await page.content()
    if PROXY_HOST in content:
        print("Proxy usage success")
    else:
        print("Proxy usage failure")
    await asyncio.sleep(2)
    await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
