# 値段の一覧を与えられた表示幅で出力する

width = int(input('表示幅を入力して下さい： '))

price_width = 20
item_width  = width - price_width


#ここでまず最初のフォーマットに入力される
#{:10}{:>20}
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt        = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
print('@' * width)
print(header_fmt.format('Item', 'Price'))
print("{:10}{:>20}".format('Item', 'Price'))