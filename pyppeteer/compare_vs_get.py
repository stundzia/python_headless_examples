import asyncio
import requests

import pyppeteer


TARGET_URL = (
    'https://www.google.com/flights?hl=en#flt=/m/07_kq./m/'
    '01f62.2020-11-13*/m/01f62./m/07_kq.2020-11-17;c:EUR;e:1;sd:1;t:f'
)
HEADERS_DESKTOP = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
}


async def get_content_headless(url: str) -> str:
    browser = await pyppeteer.launcher.launch(options={'headless': False})
    pages = await browser.pages()
    page = pages[0]
    await page.goto(url)
    await asyncio.sleep(4)

    # This xpath only exists once inspect is used.
    if els := await page.xpath('.//div[@id="introAgreeButton"]'):
        await els[0].click(
            options={
                'delay': 88,
                'button': 'left',
                'clickCount': 1,
            }
        )
        await asyncio.sleep(2)

    await page.keyboard.press('Tab')
    await asyncio.sleep(0.1)
    await page.keyboard.press('Tab')
    await asyncio.sleep(0.1)
    await page.keyboard.press('Enter')

    await asyncio.sleep(2)

    content = await page.content()
    await browser.close()
    return content


async def main():
    content_headless = await get_content_headless(url=TARGET_URL)
    with open('headless.html', 'w') as f:
        f.write(content_headless)
    print(f"Len headless: {len(content_headless)}")
    res = requests.get(url=TARGET_URL, headers=HEADERS_DESKTOP)
    with open('regular.html', 'w') as f:
        f.write(res.text)
    print(f"Len regular: ", len(res.text))


if __name__ == '__main__':
    asyncio.run(main())
