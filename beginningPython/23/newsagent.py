from nntplib import NNTP

# サーバー名の指定
# serever name = 'news.foo.bar'
servername = 'nntp.aioe.org'

# news group の指定
# group = 'comp.lang.python.announce'
group = 'alt.math.undergrad'

# サーバーの指定
server = NNTP(servername)
howmany = 10
resp, count, first, last, name = server.group(group)

start = last - howmany + 1

# over() メッセージの概要を返却する
resp, overviews = server.over((start, last))

for id, over in overviews:

    subject = over['subject']
    resp, info = server.body(id)
    print(subject)
    print('-' * len(subject))

    for line in info.lines:
        print(line.decode( 'latin1' ))
    print()

server.quit()