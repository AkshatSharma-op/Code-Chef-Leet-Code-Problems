#“Find Non-repearing Pairs with Given Sum"
k=int(input('Enter the target value'))
arr=list(map(int,input('Enter list').strip().split()))
def pair(t,a):
    s=set()
    d={}
    count=0
    for x in a:
        y=t-x
        if y in d and d.get(y,1)==1:
            pair=tuple(sorted((x,y)))
            s.add(pair)
            count+=1
            print(s)
        else:
            d[x]=1
        print(d)
    return s
print('pairs: ',len(pair(k,arr)))
