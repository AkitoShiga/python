import os
import logging
import mechanicalsoup

COOKPAD_LOGIN = 'garcy0303@gmail.com'
COOKPAD_PASSWORD = 'tamanoi123'

def main():
    browser = mechanicalsoup.StatefulBrowser()
    logging.info('Navigating...')
    browser.open('https://cookpad.com/recipe/history')

    # ログインページにリダイレクトされているか確認
    assert '/login' in browser.get_url()

    browser.select_form('.login_form form')
    browser['login'] = COOKPAD_LOGIN
    browser['password'] = COOKPAD_PASSWORD

    logging.info('Signing in')
    browser.submit_selected()

    assert '最近見たレシピ' in browser.get_current_page().title.string


    for a in browser.get_current_page().select('#main a.recipe-title'):
        print(a.text)
        print(browser.absolute_url(a.get('href')))


if __name__ == '__main__':
    main()
