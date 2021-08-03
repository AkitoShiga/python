try:
    1/0
except ZeroDivisionError:
    raise ValueError
#    raise ValueError from None # ZeroDivisionError(コンテキスト)を抑制