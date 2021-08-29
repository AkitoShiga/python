import logging
import time
from typing import List
from selenium.webdriver import Chrome, ChromeOptions, Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests

SLACK_INCOMING_WEBHOOK_URL = ''
def main():
    """
    メイン処理
    """
    options = ChromeOptions()
    options.headless = True
    driver = Chrome(options=options)
    navigate(driver)
    contents = scrape_contents(driver)
    logging.info(f'Found {len(contents)}contents.')
    cont = sorted(contents, key=lambda c: c['like'], reverse=True)[0]
    logging.info(f'Notifying to Slack:{cont["url"]}')
    # slackに通知
    requests.post(
                    SLACK_INCOMING_WEBHOOK_URL,
                    json={
                            'text': f':heart: {cont["like"]}{cont["url"]}',
                            'unfurl_links': True,
                    }
                 )

    for content in contents:
        print(content)

    driver.quit()


def navigate(driver: Remote):
    """
    目的のページに移動する
    """
    pass
    logging.info('Navigating...')
    driver.get('https://note.mu/')
    assert 'note' in driver.title
    for _ in range(3):
        # 決め打ち
        driver.execute_script('scroll(0, document.body.scrollHeight)')
        logging.info('Waiting for contents to be loaded...')
        time.sleep(2)

        # 条件指定
        """
        # 現在の要素数 + 10
        n = len(driver.find_elements_by_css_selector('t-timeline > div > .m-largeNoteWrapper__card')) + 10
        driver.execute_script('scroll(0, document.body.scrollHeight)')
        logging.info('Waiting for contents to be loaded..')
        # n番目のコンテンツに対応する要素が表示されるまで待つ
        # タイムアウトの設定
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f'.m-largeNoteWrapper__card:nth-of-type({n})')
        ))
        """

def scrape_contents(driver: Remote) -> List[dict]:
    """
    文章コンテンツのURL、タイトル、概要、スキの数を含むdictのリストを取得する
    """
    contents = []
    for div in driver.find_elements_by_css_selector('.m-largeNoteWrapper__card'):
        a = div.find_element_by_css_selector('a')
        try:
            description = div.find_element_by_css_selector('p').text
        except NoSuchElementException:
            description = ''
        try:
            like = div.find_element_by_css_selector('div[class="m-noteBody__statusLabel"]').text
        except NoSuchElementException:
            like = ''
            
        # URL、タイトル、概要、スキの数を取得してdictに格納
        contents.append({
            'url': a.get_attribute('href'),
            'title': div.find_element_by_css_selector('h3').text,
            'description': description,
            'like': like,
        })

    return contents

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
