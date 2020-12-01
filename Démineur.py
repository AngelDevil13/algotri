import random

Colone = []
ColoneNum = 0
LineNum = 0
Linehidden = []
displayFULL = []
staticNum = 0
variableNum = 0
displayGUI = []
SHOWING = 0
Position = 0
STATE = 0
STOP = 0

print("Enter the horizontal perimeter value of your choice :")
LineNum=int(input())

print("Enter the vertical perimeter value of your choice :")
ColoneNum=int(input())

def initial():
    Okay = []
    for x in range(ColoneNum):
        choice = random.randint(0, 10)
        if choice == 0:
            Okay.append(1)
        else:
            Okay.append(0)
    return Okay
    
while Colone.count(1)<1 or Colone.count(0)<1:
    for y in range(LineNum):
        Linehidden = initial()
        for u in range(ColoneNum):
            displayGUI.append(0)
        Colone.extend(Linehidden)
    if(Colone.count(1)<1 or Colone.count(0)<1):
        Colone.clear()


def bomb(Loca):
    result = Colone[Loca]
    return result

def proximity(var):
    Valid = 0
    final = 0
    limitmin = 0
    limitmax = 0
    
    while (limitmax-1)<var:
        limitmax=limitmax+LineNum
        
    limitmax=limitmax-1
        
    if limitmax<1:
        limitmax=limitmax+LineNum
        
    if limitmax>(ColoneNum*LineNum):
        limitmax=limitmax-LineNum
    
    limitmin=limitmax-(LineNum-1)
    
    if limitmin<0:
        limitmin=0
    
    
    if (var+1)<=limitmax:#droite
        final = final+bomb(var+1)
        
    if (var-1)>=limitmin:#gauche
        final = final+bomb(var-1)
        
    limitminDOWN = limitmin-(LineNum)
    if(limitminDOWN<0):
        limitminDOWN = 0
        
    if (var-LineNum)>=limitminDOWN and (var-LineNum)<=(limitminDOWN+LineNum):#en haut
        final = final+bomb(var-LineNum)
        
        if (var-(LineNum+1))>=limitminDOWN and (var-(LineNum+1))<=(limitminDOWN+(LineNum-1)):#diagonale gauche haut
            final = final+bomb(var-(LineNum+1))
        
        if (var-(LineNum-1))>=limitminDOWN and (var-(LineNum-1))<=(limitminDOWN+(LineNum-1)):#digonale droite haut
            final = final+bomb(var-(LineNum-1))
        
        
    limitmaxUP = limitmax+(LineNum)
    if(limitmaxUP>((ColoneNum*LineNum)-1)):
        limitmaxUP = (ColoneNum*LineNum)-1
        
        
        
    if (var+LineNum)<=limitmaxUP and (var+LineNum)>=(limitmaxUP-LineNum):#en bas
        final = final+bomb(var+LineNum)
        print("EB")
        
        if (var+(LineNum-1))<=limitmaxUP and (var+(LineNum-1))>=(limitmaxUP-(LineNum-1)):#diagonale gauche bas
            final = final+bomb(var+(LineNum-1))
            print("Dgb")
        
        if (var+(LineNum+1))<=limitmaxUP and (var+(LineNum+1))>=(limitmaxUP-(LineNum-1)):#diagonale droite bas
            final = final+bomb(var+(LineNum+1))
            print("Ddb")
        
    return final

def DisplayGUI(MOO):
    for w in range(ColoneNum):
        Position=LineNum*w
        print(end="[")
        for v in range(LineNum):
            Position=Position+v
            
            STATE=Colone[Position]
            
            SHOWING=displayGUI[Position]
            
            if SHOWING == 0:
                print(end="*")
            else:
                if STATE==1:
                    print(end='X')
                    MOO = 1
                else:
                    MEH=proximity(Position)
                    print(MEH,end="")
            if v < (LineNum-1):
                print(end=", ")
            Position=Position-(v)
        print("]")
        
    if(MOO==1):
        LOL=1
    else:
        LOL=0
    return LOL
        
#-----------How to display something ? v
def DisplayONE(Num):
    displayGUI.pop(Num)
    displayGUI.insert(Num,1)
#-----------How to display something ? ^

def TEST(OK):
    NO=0
    if(OK==0):
        for u in range(len(Colone)):
            if(displayGUI[u]==Colone[(u)]):
                NO=1
        if(NO==0):
            OK=2
    return OK

def Turn(ORA):
    print("------------------------------------------")
    ORA=DisplayGUI(ORA)
    print()
    return ORA

def invalid():
    print()
    print("Invalid number !")
    print()
    print()

DisplayGUI(STOP)

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
        print("Please Type a COLUM number between 0 and ",(LineNum))
        ENTRYDos=int(input())
        print()
        print("Please Type a LINE number between 0 and ",(ColoneNum))
        ENTRYUno=int(input())
        
        ENTRY=(ENTRYUno-1)*LineNum+(ENTRYDos-1)
        
        if ENTRY > -1:
            if ENTRY <= (ColoneNum*LineNum):
                YES=1
            else:
              invalid()
        else:
            invalid()
            
    DisplayONE(ENTRY)
    STOP=Turn(STOP)
    STOP=TEST(STOP)


if STOP==1:
    print("YOU LOSE !")
else:
    print("CONGRATULATION !")
    print("YOU HAVE WON !")
    
print()
print()
print("GAME OVER")