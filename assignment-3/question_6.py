# Write a program for a matchstick game being played between the computer and a user. Your
# program should ensure that the computer always wins. Rules for the game are as follows:
#  There are 21 matchsticks.
#  The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
#  After the person picks, the computer does its picking.
#  Whoever is forced to pick up the last matchstick loses the game

  
matchSticks=21
print("Welcome to the Matchstick Game!")
while matchSticks > 0:
    user_input=int(input("Pick matchsticks (1-4) :"))
    while user_input < 1 or user_input > 4 or user_input==matchSticks:
        print("Invalid choice. Pick again.")
        user_input=int(input("Pick matchsticks (1-4):"))
    print("You pick",user_input,"matchsticks")
    matchSticks=matchSticks-user_input
    print("Remaining matchsticks: ",matchSticks)
    if matchSticks == 0:
        print("You picked the last matchstick. You lose!")
        break
    computer_pick=5-user_input
    print("\nComputer's turn: The computer picks",computer_pick,"matchstick(s).")
    matchSticks=matchSticks-computer_pick
    print("Remaining matchsticks: ", matchSticks)
    if matchSticks==0 or matchSticks ==1:
        print("Computer Win")
    