#!/Users/insightshiga/Documents/sandbox/python/crawlingAndScraping/scraping/bin/python

import csv
import json

with open('top_cities.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['rank', 'city', 'population'])
    writer.writerows([
        [1, '上海', 20000],
        [2, '上海', 20000],
        [3, '上海', 20000],
        [4, '上海', 20000],
        [5, '上海', 20000]
    ])

# 辞書型
with open('top_cities2.csv', 'w', newline='') as f:
    # ここまでで1セット
    writer = csv.DictWriter(f, ['rank', 'city', 'population'])
    writer.writeheader()

    dict = [
        {'rank': 1, 'city': '上海', 'population':  20000},
        {'rank': 2, 'city': '上海', 'population':  20000},
        {'rank': 3, 'city': '上海', 'population':  20000},
        {'rank': 4, 'city': '上海', 'population':  20000},
        {'rank': 5, 'city': '上海', 'population':  20000}
    ]
    writer.writerows(dict)

# json
print(json.dumps(dict, ensure_ascii=False, indent=2))
