#!/Users/insightshiga/.pyenv/shims/python

import sqlite3
conn = sqlite3.connect('top_cities.db')

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS cities')

c.execute("""
    create table cities (
        rank integer,
        ctiy text,
        population integer
    )
""")

# executeは生のSQL第2引数はSQLのパラメーターのリストを指定できる
# パラメーターで置き換える場所は?で指定
c.execute('INSERT INTO cities VALUES(?, ?, ?)', (1, '上海', 2415000))

# パラメーターを辞書にもできる、プレースホルダはkeyにする
c.execute('INSERT INTO cities VALUES(:rank, :city, :population)',{'rank': 2, 'city': 'カラチ', 'population': 2350000})

# 複数の値の指定はexecutemany
c.executemany('INSERT INTO cities VALUES(:rank, :city, :population)', [
    {'rank': 3, 'city': '北京', 'population': 2222222},
    {'rank': 4, 'city': '転身', 'population': 3333333},
    {'rank': 5, 'city': 'イスタンブル', 'population': 444444}]
)

conn.commit()

c.execute('SELECT * FROM cities')
for row in c.fetchall():
    print(row)

conn.close()
