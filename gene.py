# Enter your code here. Read input from STDIN. Print output to ST
size=int(raw_input())
a=raw_input()
limit=size/4
begin=0
end=0
lst={'A':0,'C':0,'G':0,'T':0}
for i in range(size-1,0,-1):
    lst[a[i]]+=1
    if lst[a[i]]>limit:
        lst[a[i]]-=1
        end=i
        break
curlow=end
i=0
while (i<end) and (end<size):
    lst[a[i]]+=1
    if end-i+1<curlow:
        curlow=end-i+1
    if lst['A']>limit or lst['G']>limit or lst['T']>limit or lst['C']>limit:
        lst[a[end]]-=1
        end+=1 
        #print "end:",end
    i+=1
print curlow        
    
        
            