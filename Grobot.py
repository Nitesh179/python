import random

pName=input("Player Name : ")
while True:
 def game(comp,you):
    if comp=='s' :
        if you=='g': return True
        elif you=='w': return False

    elif comp=='w':
        if you=='s': return True
        elif you=='g':return False

    elif comp=='g':
        if you=='w':return True        
        elif you=='s':return False


 
 print("Robot turn : Snake(s) Water(w) Gun(g) ?")

 randNo=random.randint(1,3)
 if randNo == 1:
    comp='s'
 elif randNo == 2:
    comp='w'
 elif randNo == 3:
    comp='g'        

 plyr=input(f"{pName} turn : Snake(s) Water(w) Gun(g) ? ")

 print(f"\nRobot Choose (%s) \t {pName} Choose (%s) \n" %(comp,plyr))

 if comp!=plyr:
  if game(comp,plyr):print(f"congrat's {pName} You Win !!")
  else : print(f"Ooh shit {pName} You Lose !!")

 else: print("this match is tie !!!")

 play=int(input("\nIf you want to play again ? \n if yes press 1 \t if No press 2 \n"))
 if play==1: pass
 else :
   break





