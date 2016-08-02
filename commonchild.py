# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
def comchar(tup1,tup2):
    ls1= [[0]*(len(t1)) for i in xrange(len(t2))]    
    for i in range(len(tup1)):
        for j in range(len(tup2)):
            #print tup1[i],tup2[j]
            if tup1[i]==tup2[j]:
                if i==0 or j==0:
                    ls1[i][j]=1
                    #print i,j
                else:
                    ls1[i][j]=1+ls1[i-1][j-1]
                    #print i,j
                    #print i-1,j-1
            else:
                if i!=0 or j!=0:
                    ls1[i][j]=maxim(ls1[i][j-1],ls1[i-1][j])
                    #print i,j
    #print ls1
    return ls1[len(tup1)-1][len(tup2)-1]
def maxim(a1,b1):
    if a1>b1:
        return a1
    else:
        return b1           
k=raw_input()
l=raw_input()
t1=list(tuple(k))
t2=list(tuple(l))
print comchar(t1,t2)




