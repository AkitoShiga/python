try:
    x = int(input('first num: '))
    y = int(input('seccond num: '))
    print( x / y)

    '''
    except ZeroDivisionError:
        print('No seccond number 0')
    except ValueError:
        print('No String')
    '''
# e に エラーを代入できる
except (ZeroDivisionError, ValueError) as e:
    print(e)

# なんでも補足する
except :
    print('Unknown Error')