# object: Longest Substring Without Repeating Characters
st=input('Enter words : ').strip()
l=len(st)
def sub(s):
    max_len=0
    for i in range(l):
        for j in range(i+1,l+1):
            subst=s[i:j]
            if len(set(subst))==len(subst):
                max_len=max(max_len,len(subst))
    return max_len
print('max len:',sub(st))
    