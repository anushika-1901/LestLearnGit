# l1=[23,10,56,24,11]
# l2=[45,56,78,23]
# for i in l1:
#     if i %2==1:
#         continue 
#     print(i)

# l1.reverse()
# print(l1)

# matrix=[[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# print(matrix[0][0])
# print(matrix[1][2])
# for i in matrix:
#     for j in i:
#         print(j)


import random
possible_actions=['Rock','Paper','Scissors']
computer_action=random.choice(possible_actions)
actions={1:'Rock',2:'Paper',3:'Scissors'}
print("""
        Possible actions :
      1.Rock
      2.paper
      3.Scissors
""")
user_action=int(input("Enter the value of action :"))
map_user_action=actions[user_action]
if computer_action==map_user_action:
    print("It's a tie")
elif map_user_action=='Rock':
    if computer_action=='Paper':
        print("You lose")
    else:
        print("You win")
elif map_user_action=='Paper':
    if computer_action=='Scissors':
        print("You lose")
    else:
        print("You win")
elif map_user_action=='Scissors':
    if computer_action=='Rock':
        print('You lose')
    else:
        print('You win')

print(f"Computer chose {computer_action} and you chose {map_user_action}")
print(map_user_action)

