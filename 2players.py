import getpass

while True:

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
            if p2 == "r":
                return False
            elif p2 == "p":
                return True

    player1 = input("Enter Player 1 Name : ")
    player2 = input("Enter Player 2 Name : ")

    #  p1=input(f"{player1} turn : Rock(r) Paper(p) sessor(s) ? ")
    p1 = getpass.getpass(prompt=f"{player1} turn : Rock(r) Paper(p) sessor(s) ? ")
    p2 = input(f"{player2} turn : Roc2k(r) Paper(p) sessor(s) ? ")

    print(f"\n{player1} Choose (%s) \t {player2} Choose (%s) \n" % (p1, p2))

    if p1 != p2:
        if game(p1, p2):
            print(f"{player2} Win !!! \t {player1} Lost !!!")
        else:
            print(f"{player1} Win !!! \n {player2} Lost !!!")
    else:
        print("Match is Tie !!!")

    play = int(
        input("\nIf you want to play again ? \n if yes press 1 \t if No press 2 \n")
    )
    if play == 1:
        pass
    else:
        break
