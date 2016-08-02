# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(raw_input())
for i in range(a):
    lst=dict()
    s=raw_input()
    anagrams=0
    #abc=[[(None)]*len(s) for i in range(len(s))]
    for a in range(len(s)):
        for b in range(a,len(s)):
            k=''.join(sorted(s[a:b+1]))
            if lst.has_key(k):
                lst[k]+=1
            else:
                lst[k]=1
    for v in lst.values():
        if v>2:
            anagrams=anagrams+(v*(v-1)/2)
        elif v==2:
            anagrams=anagrams+1
    
    print anagrams
                
        