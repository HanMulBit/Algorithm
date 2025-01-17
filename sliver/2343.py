# 강의 동영상 블루레이로 판매
# n개의 강의 but 강의 순서가 바뀌면 안됨
# i ~ j 번째 강의 녹화 같은 블루레이에 하려면 i와 j 사이 강의 같은 블루레이에 녹화
# m개의 블루레이에 모든 기타 강의 동영상 녹화, 모두 같은 크기
# 블루레이의 크기를 최소로 하는 개수를 구하여라
n, m = map(int,input().split())
lecture_time = list(map(int,input().split()))

start = max(lecture_time)
end = sum(lecture_time)

def devide_lec(mid):
    
    count = 1
    total = 0
    
    for time in lecture_time:
        if total + time > mid:
            count += 1
            total = time
        else:
            total += time
    return count <= m

while start <= end:
    mid = (start + end) // 2
    if devide_lec(mid):
        end = mid - 1
    else :
        start = mid + 1
        
print(start)