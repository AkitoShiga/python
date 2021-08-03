def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested # 値をそのまま返す
# nested が flattenの戻り値になってそれを elementとなる。 それをまた親のflattenに渡してる

for num in flatten([[[1], 2], 3, 4, [5, [6, 7]]]):
    print(num)

fl = list(flatten([[[1], 2], 3, 4, [5, [6, 7]]]))
print(fl)
