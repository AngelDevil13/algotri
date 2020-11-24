import random

Colone = []
ColoneNum = 5
LineNum = 5
Linehidden = []
displayFULL = []
staticNum = 0
variableNum = 0
displayGUI = []
SHOWING = 0
Position = 0
STATE = 0
STOP = 0

def initial():
    Okay = []
    
    for x in range(ColoneNum):
        choice = random.randint(0, 10)
        if choice == 0:
            Okay.append(1)
        else:
            Okay.append(0)
    return Okay
while Colone.count(1)<1:
    for y in range(LineNum):
        Linehidden = initial()
        for u in range(ColoneNum):
            displayGUI.append(0)
        Colone.extend(Linehidden)

print(Colone.count(1))

#-------------------Delete this when it's done v
for z in range(ColoneNum):
    variableNum=variableNum+ColoneNum
    displayFULL.extend(Colone[staticNum:variableNum])
    staticNum=variableNum
    print(displayFULL)
    displayFULL.clear()
print("------------------------------------------")
#-------------------Delete this when it's done ^
def bomb(Loca):
    result = Colone[Loca]
    return result

def proximity(var):
    Valid = 0
    final = 0
    if (var-(ColoneNum+1))>=0:
        final = final+bomb(var-(ColoneNum+1))
    if (var-ColoneNum)>=0:
        final = final+bomb(var-ColoneNum)
    if (var-(ColoneNum-1))>=0:
        final = final+bomb(var-(ColoneNum-1))
    if (var+1)<(ColoneNum*LineNum):
        final = final+bomb(var+1)
    if (var+(ColoneNum-1))<(ColoneNum*LineNum):
        final = final+bomb(var+(ColoneNum-1))
    if (var+ColoneNum)<(ColoneNum*LineNum):
        final = final+bomb(var+ColoneNum)
    if (var+(ColoneNum+1))<(ColoneNum*LineNum):
        final = final+bomb(var+(ColoneNum+1))
    if (var-1)>=0:
        final = final+bomb(var-1)
    return final

def DisplayGUI():
    for w in range(ColoneNum):
        Position=ColoneNum*w
        print(end="[")
        for v in range(LineNum):
            Position=Position+v
            
            STATE=Colone[Position]
            
            SHOWING=displayGUI[Position]
            
            
            if SHOWING == 0:
                print(end="*")
            else:
                if STATE==1:
                    STOP = 1
                    print(end='X')
                else:
                    MEH=proximity(Position)
                    print(MEH,end="")
            if v < (LineNum-1):
                print(end=", ")
            Position=Position-(v)
        print("]")
        
#-----------How to display something ? v
def DisplayONE(Num):
    displayGUI.pop(Num)
    displayGUI.insert(Num,1)
#-----------How to display something ? ^

def Turn():
    print("------------------------------------------")
    DisplayGUI()
    print()

def invalid():
    print()
    print("Invalid number !")
    print()
    print()

DisplayGUI()

#Add an entry
print("------------------------------------------")
print("Use this logic please !")
print()
print("  1,2,3,4,5...")
print("1,")
print("2,")
print("3,")
print("4,")
print("5")
print("...")

while STOP==0:
    print()
    YES=0
    while YES==0:
        print("Please Type a COLUM number between 0 and ",(ColoneNum))
        ENTRYDos=int(input())
        print()
        print("Please Type a LINE number between 0 and ",(ColoneNum))
        ENTRYUno=int(input())
        
        ENTRY=(ENTRYUno-1)*ColoneNum+(ENTRYDos-1)
        
        if ENTRY > 0:
            if ENTRY <= (ColoneNum*LineNum):
                YES=1
            else:
              invalid()
        else:
            invalid()
            
    DisplayONE(ENTRY)
    Turn()
    print(STOP)

print("GAME OVER")