# 1. making a report about: number of win/lose
# 2. assume that you have 100$. In each game, you should pay 5$.
#     After finishing game, report the amount go got.
# 3. Game will end if you lost all money
import random
win_count= 0
lose_count= 0
money= 100

while True:
    print("computer thinks a number from 1 to 100")
    comp_number= random.randint(1,100)

    level= int(input("choose level [1,2,3]?:"))
    times= 10 if level == 1 else 5 if level == 2 else 3
    is_win= False
    money-= 5
    print(f"you have {money}$ left (because you paid 5$ to play)")
    for time in range(times):
      your_num= int(input("enter your number #" + str(time + 1) + ":"))
      if your_num == comp_number:
        is_win= True
        win_count+= 1
        money+= 10
        print("you win!!!")
        print(f"you won 10$, now you have {money}$")
        break
      else:
         if your_num < comp_number:
            print("too low!")
         else:
            print("too high!")
    if not is_win:
        lose_count+= 1
        print("----------------")
        print("game over!")
    print(f"report: Win={win_count}, Lose={lose_count}, Money={money}$")
    if money<= 0:
        print("you lost all your money, see you again!")
        break
    cont= input("do you want to play [Y/N]?")
    if cont== "N":
        print("thanks for coming!!!")
        break
