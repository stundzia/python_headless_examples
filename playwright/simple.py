import asyncio

from playwright import async_playwright as playwright


HEADLESS = False
WAIT_TIME = 3.5


async def main():
    async with playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch(headless=HEADLESS)
            page = await browser.newPage()

            # Get user agent screenshot
            await page.goto('http://whatsmyuseragent.org/')
            await page.screenshot(path=f'ua-{browser_type.name}.png')
            await asyncio.sleep(WAIT_TIME)

            # Check bot status screenshot
            await page.goto(
                'https://arh.antoinevastel.com/bots/areyouheadless',
            )
            await page.screenshot(path=f'headless-{browser_type.name}.png')
            await asyncio.sleep(WAIT_TIME)

            # Check other bot status
            await page.goto(
                'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html',
            )
            await page.screenshot(path=f'headless2-{browser_type.name}.png')
            await asyncio.sleep(WAIT_TIME)

            await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
