import getpass,os


player1 = input("Enter Player 1 Name : ")
player2 = input("Enter Player 2 Name : ")

while True:
    os.system('clear')
    def game(p1, p2):
        if p1 == "r":
            if p2 == "p":
                return True
            elif p2 == "s":
                return False
        elif p1 == "p":
            if p2 == "r":
                return True
            elif p2 == "s":
                return False
        elif p1 == "s":
            if p2 == "p":
                return False
            elif p2 == "r":
                return True

   
    #  p1=input(f"{player1} turn : Rock(r) Paper(p) sessor(s) ? ")
    p1 = getpass.getpass(prompt=f"\n{player1} turn : Rock(r) Paper(p) sessor(s) ? ")
    p2 = input(f"{player2} turn : Roc2k(r) Paper(p) sessor(s) ? ")

    print(f"\n{player1} Choose (%s) \t {player2} Choose (%s) \n" % (p1, p2))

    if p1 != p2:
        if game(p1, p2):
            print(f"{player2} Win !!! \t {player1} Lost !!!")
       
    else:
        print("Match is Tie !!!")

    play = int(
        input("\nIf you want to play again ?[y-1/n-0] : ")
    )
    if play == 1:
        pass
    else:
        break
