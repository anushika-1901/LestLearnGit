import random 
chances=5
print("""Please select level of game :
      1.Level One
      2.Level Two
      3.Level Three

""")
game_level=int(input("Enter the level :"))
if game_level==1:
    computer_generated_number=random.randint(0,50)
elif game_level==2:
    computer_generated_number=random.randint(0,100)
else:
    computer_generated_number=random.randint(0,200)
won=False 
while chances:
    chances-=1
    user_guess=int(input("Guess the number :"))
    if user_guess==computer_generated_number:
        won=True 
        print(f"You guessed the number.Left chances are {chances}")
        break
    elif user_guess>computer_generated_number:
        print("Sorry number is less")
    elif user_guess<computer_generated_number:
        print("Sorry number is greater")

if not won:
    print(f"You lost better luck next time.The number was {computer_generated_number}") 

