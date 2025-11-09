# Object: Count subarrays with sum divisible by K
k=int(input('Value of k: ').strip())
s=input('Enter array: ').strip().split()
arr=list(map(int,s))

def subarr(a,t):
    count=0
    l=len(arr)
    for i in range(l):
        sum=0
        for j in range (i,l):
            sum+=arr[j]
            if sum%k==0:
                count+=1
    return count
print('count',subarr(arr,k))
