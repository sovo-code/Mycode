# 编码实现勒让德符号的计算
def isshsu(p):
    for i in range(2, p-1):
        if p%i==0:
            return False
    return True
def LegendreSymbol(a,b):
    x, y = int(a), int(b)
    if x==0:
        return 0
    elif x == 1:
        return 1
    else:
        e=0
        a1=x
        while True:
            if a1%2==0:
                a1 = a1//2
                e+=1
                continue
            else:
                break
        if e%2==0:
            s=1
        elif y%8==1 or y%8==7:
            s=1
        elif y%8==3 or y%8==5:
            s=-1
        if y%4==3 and a1%4==3:
            s=-s
        b1=y%a1
        if a1==1:
            return s
        else:
            return s*LegendreSymbol(b1,a1)

a=input("输入第一个数：")
b=input("输入第二个数：")
print(LegendreSymbol(a,b))
