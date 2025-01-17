# 일차원 좌표 점 n개와 선분 m개
# 각각의 선분 위에 입력으로 주어진 점이 몇 개인지 구하여라
import bisect

n, m = map(int,input().split())
dot_list = list(map(int,input().split()))

dot_list.sort()

for _ in range(m):
    start, end = map(int,input().split())
    
    left = bisect.bisect_left(dot_list, start)
    right = bisect.bisect_right(dot_list, end)
    
    result = right - left
    print(result)
    