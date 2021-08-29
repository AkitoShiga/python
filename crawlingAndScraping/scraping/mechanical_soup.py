import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
browser.open('https://www.google.co.jp/')

browser.select_form('form[action="/search"]')
browser['q'] = 'Python'
browser.submit_selected()

page = browser.get_current_page()
for a in page.select('h3 > a'):
    print('hoi')
    print(a.text)
    print(browser.absolute_url(a.get('href')))
