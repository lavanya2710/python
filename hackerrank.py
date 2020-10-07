"""#1
def countswap(a):
    swap=0
    for j in range(len(a)-1):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                swap=swap+1
    print("Array is sorted in %s swaps." %swap)
    print("First Element:",a[0])
    print("Last Element:",a[-1])
n=int(input(""))
a=list(map(int,input().split()))
countswap(a)
#2
def maximumToys(prices, k):
    count=0
    total=0
    prices.sort()
    for i in prices:
        total=total+i
        if total<=k:
            count=count+1
    return count
 #3
class player:
    def __init__(self,name,score):
         self.name=name
         self.score=score
    def __comparator__(a,b):
        if score.a<score.b:
            return 1
        elif score.a==score.b:
            if a.name<b.name:
                return 1
            else:
                return -1
        else:
            return -1"""

#4
"""def bank(exp,d):
    d=5
    for i in range(d[0],d[2]):
       print(i)
    exp=[2,3,4,2,3]
    exp.sort()
    print(exp)
    n=len(exp)
    median=n/2
    median1=n+1/2
    #for i in exp:
    #for j in range():
        #print(i)
    if n%2==0:
        return median
    else:
        return median1
obj=bank([2,3,4,2,3],5)
print(obj)"""










