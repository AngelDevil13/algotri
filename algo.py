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

def triSelect (list):
    result=[]
    while len(list)>0:
        var=selectMin(list)
        for x in range(list.count(var)):
            result.append(var)
            list.remove(var)
        
    return result

print(selectMin([4,2,7,8]))
print(triSelect([4,2,7,8]))