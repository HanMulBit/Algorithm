# 랜선 자르기
# n개의 랜선 제작필요
# 영식이 이미 k개의 랜선 있음. but 길이 제각각
# 자른 랜선은 붙일 수 없으며 n개보다 많이 만드는 것도 n개를 만드는 것에 포함
# 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하여라

k, n = map(int, input().split())
k_list = [int(input()) for _ in range(k)]

start = 1
end = max(k_list)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0

    for length in k_list:
        total += length // mid

    if total >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
