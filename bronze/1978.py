# 주어진 수 n개 중 소수가 몇 개인지 찾아서 출력하는 프로그램 작성
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0 :
            return False
    return True

n = int(input())
n_list = list(map(int,input().split()))
count = 0

for num in numbers:
    if is_prime(num):
        count += 1
        
print(count) 
