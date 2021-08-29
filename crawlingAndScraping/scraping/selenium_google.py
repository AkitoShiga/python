from selenium.webdriver import Chrome, ChromeOptions,Remote
from selenium.webdriver.common.keys import Keys

options = ChromeOptions()
# ヘッドレスモードの有効化
# options.headless = True
driver = Chrome(options=options)

driver.get('https://www.google.co.jp/')
assert 'Google' in driver.title

input_element = driver.find_element_by_name('q')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

assert 'Python' in driver.title

driver.save_screenshot('search_results.png')

for h3 in driver.find_elements_by_css_selector('a > h3'):
    a = h3.find_element_by_xpath('..')
    print(h3.text)
    print(a.get_attribute('href'))

driver.quit()
