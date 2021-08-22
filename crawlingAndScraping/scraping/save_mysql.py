#!/Users/insightshiga/.pyenv/shims/python

import MySQLdb

conn = MySQLdb.connect(
            db='scraping',
            user='scraper',
            passwd='password',
            charset='utf8mb4'
       )

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS `cities`')
c.execute("""
    CREATE TABLE `cities`(
        `rank` integer,
        `city` text,
        `population` integer
    )
""")
c.execute("""
    INSERT INTO
        `cities`
    VALUES(%s, %s, %s)
""", (1, '上海', 2415000))

# 辞書型で入れる場合は若干わかりにくい
c.execute('INSERT INTO `cities` VALUES(%(rank)s, %(city)s, %(population)s)',
          {'rank': 2, 'city': 'カラチ', 'population': 2350000})

c.executemany('INSERT INTO `cities` VALUES(%(rank)s, %(city)s, %(population)s)',
              [
                {'rank': 3, 'city': '北京', 'population': 2350000},
                {'rank': 4, 'city': '天津', 'population': 2350000},
                {'rank': 5, 'city': 'イスタンブル', 'population': 2350000}
              ]
              )
conn.commit()

c.execute('SELECT * FROM `cities`')
# fetchallで結果を取得する
for row in c.fetchall():
    print(row)

conn.close()
