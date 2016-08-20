n=int(raw_input())
x=sorted(map(int,raw_input().strip().split(' ')))
y=sorted(map(int,raw_input().strip().split(' ')))
pos=0
neg=0
l=list()
#print x,y
for i in range(n):
    if x[i]>y[i]:
        pos=pos+(x[i]-y[i])
        l.append((x[i]-y[i]))
    elif x[i]<y[i]:
        neg = neg + (y[i]-x[i])
        l.append(y[i]-x[i])
ans=-1
temp=sum(l)
if temp%2==0 and pos==neg:
        ans=temp/2
print ans