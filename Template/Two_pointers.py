def two_pointers(array, target):
    left = 0  # 배열 시작 인덱스
    right = len(array) - 1  # 배열 마지막 인덱스

    while left < right:  # 포인터가 교차하지 않을 때까지 반복
        current_sum = array[left] + array[right]  # 두 포인터 합 계산

        if current_sum == target:
            return (left, right)  # 목표값을 찾았으면 두 포인터 위치 반환

        if current_sum < target:
            left += 1  # 합이 목표값보다 작으면 왼쪽 포인터 증가
        else:
            right -= 1  # 합이 목표값보다 크면 오른쪽 포인터 감소

    return -1  # 목표값을 찾지 못했을 경우 -1 반환

arr = list(map(int,input().split()))
target = int(input())

print(two_pointers(array,target))