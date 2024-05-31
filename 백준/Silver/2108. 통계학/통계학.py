import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []

for _ in range(n):
    x = int(sys.stdin.readline())
    a.append(x)
a.sort()

# 산술평균
print(round(sum(a)/n))

# 중앙값
print(a[round(n//2)])

# 최빈값
cnt = Counter(a).most_common()
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

# 범위
print(max(a)-min(a))