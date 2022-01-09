import math

# 標準入力を受け付ける。
N = int(input())

position_list = []
for _ in range(N):
    x, y = map(int, input().split())
    position_list.append((x, y))

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        x1, y1 = position_list[i]
        x2, y2 = position_list[j]
        # ある2点間の距離を求める。
        ans = max(ans, math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

# 最大値を出力する。
print(ans)
