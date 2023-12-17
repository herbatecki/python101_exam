import random

while True:
        project_tuple = ("paper", "scissors", "stone")
        choose = random.choice(project_tuple)
##        print(choose)
        user_bet = input("Please choose your bet of 'paper', 'scissors', 'stone' and tap it into this place: ")
        if choose == user_bet:
                print(f"Both computer and you have chosen {choose}. Try one more time.")
                continue
        elif choose != user_bet:
                if choose == 'paper' and user_bet == 'stone':
                        print(f"{choose} covers {user_bet}! Computer wins!")
                        decision = input("Would you like to try one more time? Tap Y or N: ")
                        if decision == "Y":
                                continue
                        else:
                                break
                elif choose == 'stone' and user_bet == 'paper':
                        print(f"{user_bet} covers {choose}! You win!")
                        decision = input("Would you like to try one more time? Tap Y or N: ")
                        if decision == "Y":
                                continue
                        else:
                                break
                elif choose == 'paper' and user_bet == 'scissors':
                        print(f"{user_bet} cut {choose}! You win!")
                        decision = input("Would you like to try one more time? Tap Y or N: ")
                        if decision == "Y":
                                continue
                        else:
                                break
                elif choose == 'scissors' and user_bet == 'paper':
                        print(f"{choose} cut {user_bet}! Computer wins!")
                        decision = input("Would you like to try one more time? Tap Y or N: ")
                        if decision == "Y":
                                continue
                        else:
                                break
                elif choose == 'stone' and user_bet == 'scissors':
                        print(f"{choose} breaks down {user_bet}! Computer wins!")
                        decision = input("Would you like to try one more time? Tap Y or N: ")
                        if decision == "Y":
                                continue
                        else:
                                break
                elif choose == 'scissors' and user_bet == 'stone':
                        print(f"{user_bet} breaks down {choose}! You win!")
                        decision = input("Would you like to try one more time? Tap Y or N: ")
                        if decision == "Y":
                                continue
                        else:
                                break
