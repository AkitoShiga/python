while True:
    try:
        x = int(input('first num: '))
        y = int(input('seccond num: '))
        print(x/y)
    except Exception as e:
        print('wrong input', e)
    else:
        break