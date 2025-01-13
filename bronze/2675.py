t = int(input())
for _ in range(t):
    r, s = input().split()
    r = int(r)
    p = ''.join([char * r for char in s])
    print(p)