# object: First Non-Repeating Character
st=input('Enter a string: ').strip()
def nr(s):
    seen={}
    for i in s:
        if i not in seen:
            seen[i]=1
        else:
            seen[i]+=1
    print(seen)
    for k,v in seen.items():
        if seen[k]==1:
            return k
        else:
            char=-1
    return char 
print('Non-repeating char:',nr(st))

    