#Trieur de liste, selectif
Mylist = [5,7,8,9,6,3,4,2,0,1]
Result = [0]

print(Mylist)

Lenght = len(Mylist)

Biggest = 0

for u,BIG in enumerate(Mylist):
    if(BIG>Biggest):
        Biggest = BIG


for x in range(Lenght):
    Take = Biggest
    for i,Num in enumerate(Mylist):
        if(Num<Take):
            Take = Num
    Count = Mylist.count(Take)
    for y in range(Count):
        Result.append(Take)
        Mylist.remove(Take)
    
Result.pop(0)
print()
print("Votre liste à été trié avec succès !")
print()
print(Result)

def selectMin(list):
    var=list[0]
    for i in list:
        if var>i:
            var=i
    return var

def triSelect(list):
    result=[]
    myList=[]
    myList.extend(list)
    while len(myList)>0:
        var=selectMin(myList)
        for x in range(myList.count(var)):
            result.append(var)
            myList.remove(var)
        
    return result

def fusion(u,d):
    
    select=[]
    
    while len(u) > 0 or len(d) > 0:
        
        if len(u) > 0:
            
            if len(d) > 0:
                if(u[0]<d[0]):
                    select.append(u[0])
                    u.pop(0)
                else:
                    select.append(d[0])
                    d.pop(0)
            else:
                select.append(u[0])
                u.pop(0)
        else:
            select.append(d[0])
            d.pop(0)
    
    return select
    
def triFusion(list):
    
    if len(list)>1:
        
        half=len(list)//2
        
        list0=list[0:half]
        list1=list[half:len(list)]
        
        list0trie=triFusion(list0)
        list1trie=triFusion(list1)
        Yo=fusion(list0trie,list1trie)
        return Yo
        
    else:
        return list


print(selectMin([4,2,7,8]))
print(triSelect([4,2,7,8]))
print(triFusion([4,2,7,8]))