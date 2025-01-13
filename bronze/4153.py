while True:
    a_list = map(int,input().split())
    sorted_list = sorted(a_list)
    a = sorted_list[0]
    b = sorted_list[1]
    c = sorted_list[2]
    
    if a == 0 and b == 0 and c == 0:
        break
    elif a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")