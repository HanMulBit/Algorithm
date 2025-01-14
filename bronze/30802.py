# 티셔츠 한 장과 펜 한자루 웰컴 키트
# 티셔츠는 S,m,l,xl,xxl,xxxl 6가지 사이즈로 같은 사이즈 t장 묶음으로만 주문
# 펜은 한 종류로 p자루씩 묶음으로 주문하거나 한 자루씩 주문
# 티셔츠는 남아도 되고 부족하면 안되며 신청한 사이즈대로
# 펜은 남거나 부족하면 안됨
# 티셔츠 최소 몇 묶음 주문해야하는지, 
# 펜은 최대 몇 묶음 주문가능하며 한 자루씩 몇 개를 주문하는지 구하여라

n = int(input())
tshort_list = list(map(int,input().split()))
t, p = map(int,input().split())

tshort_bundle = 0
for count in tshort_list:
    bundle = count // t
    if count % t != 0:
        bundle += 1
    tshort_bundle += bundle
    
total_pen = sum(tshort_list)
pen_bundle = total_pen // p
pen_single = total_pen % p

print(tshort_bundle)
print(pen_bundle,pen_single)
