# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
import random
ls = []
dict = {}
print("Enter the number of friends joining (including you):")
tot_friends = int(input())
if tot_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    print() 

    for i in range(tot_friends):
        name = input()
        ls.append(name)
       
    
    print("Enter the total bill value:")
    bill_ = int(input())
    print()
    print("Do you want to use the 'Who is lucky?'' feature? Write Yes/No:")
    choice = input()
    if choice == "Yes":
        lucky_ = random.choice(ls)
        print()
        print(lucky_ ," is the lucky person")
        for i in ls:
            if i == lucky_:
                dict.update({i: 0})
            else:
                dict.update({i: bill_/(tot_friends-1)})
    else:
        print()
        print("No one is going to be lucky")
        for i in ls:
            dict.update({i: bill_/(tot_friends)})
    
    
    print(dict)

    


