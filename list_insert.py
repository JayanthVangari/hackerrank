l=list()
x=raw_input()
i=1
while i<x:
    try:
        input=raw_input()
    except EOFError:
        break
    if input.startswith("insert"):
        items=input.split(" ")
     
        l.insert(int(items[1]),int(items[2]))
    elif input.startswith("print"):
        print str(l)
    elif input.startswith("remove"):
        items=input.split(" ")
        l.remove(int(items[1]))
    elif input.startswith("append"):
        items=input.split(" ")
        l.append(int(items[1]))
    elif input.startswith("reverse"):
        l.reverse()
    elif input.startswith("pop"):
        l.pop()
    elif input.startswith("sort"):
        l.sort()
    i=i+1