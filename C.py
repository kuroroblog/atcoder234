# 標準入力を受け付ける。
K = int(input())

# Kを2進数表記にする。
# 2進数表記したKの値の、1の部分を2に変更する。
# 参考 : https://note.nkmk.me/python-bin-oct-hex-int-format/
print(str(bin(K)[2:]).replace('1', '2'))
