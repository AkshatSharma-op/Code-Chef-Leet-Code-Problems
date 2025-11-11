# object: Majority Element in the list
num=input('enter number').strip().split()
print(num)
def mj(l):
    ln=len(l)
    seen={}
    for i in l:
        if i not in seen:
            seen[i]=1
        else:
            seen[i]+=1
    h=ln/2
    print('seen',seen)
    m=max(seen.values())
    if m>h:
        for k,v in seen.items():
            if m==v:
                return k
    else:
        char= -1  
    return char
print(mj(num))
