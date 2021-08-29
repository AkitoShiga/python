import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    # ヘッドレスモードの解除
    browser = await launch(headless=False)
    page = await browser.newPage()

    await page.goto('https://www.google.co.jp/')

    assert 'Google' in (await page.title())

    input_element = await page.querySelector('[name="q"]')
    await input_element.type('Python')

    # Enterを押下してページ遷移が終わるまで待つ
    await asyncio.wait([
                            input_element.press('Enter'),
                            page.waitForNavigation(),
                      ])

    # タイトルにパイソンがあるか？
    assert 'Python' in (await page.title())

    await page.screenshot({'path': 'search_results.png'})
    for h3 in await page.querySelectorAll('a > h3'):
        # page.evaluteは第2引数のオブジェクトを引数に渡して第一引数の関数をJavascriptとして実行する
        text = await page.evaluate('(e)       = > e.textContent', h3)
        print(text)
        a    = await page.evaluateHandle('(e) = > e.parentElement', h3)
        url  = await page.evaluate('(e)       = > e.href', a)
        print(url)

    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

