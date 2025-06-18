import random
computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youChoice={"r":1,"p":-1,"s":0}
reverseChoice={1:"Rock",-1:"Paper",0:"Scissors"}
you=youChoice[youstr]
print(f"you Choose: {reverseChoice[you]}\n Computer Choose: {reverseChoice[computer]}")
YourScore=0
ComputerScore=0
if(computer==you):
    print("Your match is draw!!:)")
else:
    if(computer==-1 and you==1):
        print("You Lose!\nTry again")
        ComputerScore+=1  
    elif(computer==1 and you==-1):
        print("You Won!")
        YourScore+=1
    elif(computer==-1 and you==0):
        print("You Lose!\nTry again")
        ComputerScore+=1
    elif(you==0 and computer==-1):
        print("You Won!")
        YourScore+=1
    elif(you==1 and computer==0):
        print("You Won!")
        YourScore+=1
    elif(you==0 and computer==1):
        print("You Lose!\nTry again") 
        ComputerScore+=1
    else:
        print("Someting went Wrong!!")          
print("Your Score is:",YourScore)
print("Computer Score is",ComputerScore)
