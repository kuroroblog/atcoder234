# f(x) = xの2乗 + 2x + 3を求める関数を用意する。
def func(x):
    return x * x + 2 * x + 3

# 標準入力を受け付ける。
t = int(input())
# f(f(f(t) + t) + f(f(t)))の結果を出力する。
print(func(func(func(t) + t) + func(func(t))))
