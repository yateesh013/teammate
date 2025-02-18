nums=[3,4,-7,1,3,3,1,4]
tar=7


def get_subarrays(n,t):
    r=[]
    map={0:[-1]}
    cur=0
    for i in range(len(n)):
        cur+=n[i]
        temp=cur-t
           
        if temp in map:
            for j in map[temp]:
                if i!=j:
                    r.append(n[j+1:i+1])
        if cur in map:
            map[cur].append(i)
        else:
            map[cur]=[i]
    return r               


#res=get_subarrays(nums,tar)
#for i in res:
#    print(i)



