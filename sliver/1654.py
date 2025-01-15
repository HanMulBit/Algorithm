# 랜선 자르기
# n개의 랜선 제작필요
# 영식이 이미 k개의 랜선 있음. but 길이 제각각
# 자른 랜선은 붙일 수 없으며 n개보다 많이 만드는 것도 n개를 만드는 것에 포함
# 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하여라
k, n = map(int, input().split())
k_list = [int(input()) for _ in range(k)]

# 이분 탐색을 위한 시작점과 끝점 설정
start = 1
end = max(k_list)

# 이분 탐색 수행
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0

    # 현재 mid 길이로 잘랐을 때 만들 수 있는 랜선의 개수 계산
    for length in k_list:
        total += length // mid

    # 만약 랜선의 개수가 n개 이상이라면, 더 긴 길이로 시도
    if total >= n:
        result = mid
        start = mid + 1
    else:
        # 랜선의 개수가 n개 미만이라면, 더 짧은 길이로 시도
        end = mid - 1

print(result)
