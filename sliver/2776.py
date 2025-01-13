# 수첩1 : 하루동안 본 정수
# 수첩2 : 연종이 봤다고 주장하는 수
# m개의 질문을 던지며 수첩 2의 수가 수첩 1에 있으면 1, 아니면 0

t = int(input())
for _ in range(t):
    n = int(input())
    note1 = set(map(int,input().split()))
    
    m = int(input())
    note2 = list(map(int,input().split()))
    
    for num in note2:
        if num in note1:
            print(1)
        else:
            print(0)