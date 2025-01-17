# 산성 용액과 알칼리성 용액
# 산성 용액은 양의 정수, 알칼리성 용액은 음의 정수
# 혼합 용액의 특성값은 각 용액의 특성값의 합
# 특성값이 0에 가까운 용액을 제작하려함
# 산성, 알칼리성 하나만 주어지는 경우도 존재할 수 있음

n = int(input())
n_list = list(map(int,input().split()))

n_list.sort()

left = 0
right = n - 1
min_diff = float('inf')
result = []

while left < right:
    nlist_sum = n_list[left] + n_list[right]
    nlist_diff = abs(nlist_sum)
    
    if nlist_diff < min_diff:
        min_diff = nlist_diff
        result = [n_list[left], n_list[right]]
        
    if nlist_sum < 0:
        left += 1
    else:
        right -= 1
    
print(result[0], result[1])