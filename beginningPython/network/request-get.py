import requests
webpage = requests.get("https://www.python.org")

print(f"ステータスコード ={webpage.status_code}")
print(f"エンコーディング ={webpage.encoding}")
print(f"コンテントタイプ ={webpage.headers['content-type']}")
print(f"コンテントの長さ ={webpage.headers['Content-Length']}")

html = webpage.text
print(f"----HTMLコード(先頭100文字)\n{html[0:100]}")

import re
#pattern = re.compile(r'<a href="([^"]+)', re.MULTILINE)

# [<a href="] に続く文字列を"の前まで抽出、そのあと>about</a>がある
# re.IGNORECASE は大文字小文字を無視する
match = re.search('<a href="([^"]+)".*?>about</a>', html, re.IGNORECASE)

print(f"\nABOUTのページのURL={match.group(1)}")

# bodyタグ内の文字列を検索
match = re.search('(<body (.|\s)*</body>)', html, re.IGNORECASE)

print("\n---------body tag")
print(f"{match.group(1)[0:100]}")

print("\n---------body tag")
print(f"{match.group(1)[-100:]}")