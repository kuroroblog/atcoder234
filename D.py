import heapq

# 標準入力を受け付ける。
N, K = map(int, input().split())

P = list(map(int, input().split()))

H = []
for i in range(K):
    heapq.heappush(H, P[i])

# P0~PK項のうち、K番目に大きい値を格納する。
ans = [str(H[0])]
for i in range(K, N):
    heapq.heappush(H, P[i])
    # 配列の個数を毎度K個にする。
    # K番目以下の値を取り除く。
    heapq.heappop(H)
    # P0~Pi項のうち、K番目に大きい値を格納する。
    ans.append(str(H[0]))

print("\n".join(ans))
