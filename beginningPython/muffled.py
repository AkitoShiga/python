class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('No zero')
            else:
                raise


mc = MuffledCalculator()
print(mc.calc("5/2"))

# 例外を処理 -> No zero
mc.muffled = True
print(mc.calc("5/0"))


# 例外を処理 -> ZeroDivisionError
mc.muffled = False
print(mc.calc("5/0"))
