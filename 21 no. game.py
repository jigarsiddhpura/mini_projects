try:

    import random
    print("Player 2 is computer")

    def player1_record():
        while (1):
            num = int(input("How many numbers you wish to enter?\n> "))
            if num > 3:
                print("Maximum numbers you can enter is 3")
                continue
            else:
                break

        print("Enter your values")
        counter = 0
        while counter < num:
            inp = int(input("> "))
            list1.append(inp)
            check()
            counter += 1


    def comp_record():
        nums_of_comp = random.randint(1, 3)
        counter = 0
        while counter < nums_of_comp:
            value = list1[-1] + 1
            list1.append(value)
            check()
            counter += 1


    def check():
        if len(list1) > 1:
            if list1[-1] - list1[-2] != 1:
                print("Invalid input , You are disqualified")
                exit()


    while (1):
        start = input("Do you want to start the game? (Yes/No)\n> ").capitalize()
        list1 = [0]
        if start == "Yes":
            print("Enter 'F' to take a first start")
            print("Enter 'S' to take a second start")
            begin = input("> ").upper()
            if begin == "F":
                while list1[-1] < 21:
                    player1_record()
                    if list1[-1] >= 21:
                        print("OOPS ! , YOU LOSE")
                        break
                    comp_record()
                    print("Order of inputs after computer's turn is:")
                    print(list1)
                    if list1[-1] >= 21:
                        print("CONGRATULATONS!! , YOU WIN")
                        break
                    print("\nYour turn.\n")

            elif begin == "S":
                while list1[-1] < 21:
                    comp_record()
                    print("Order of inputs after computer's turn is:")
                    print(list1)
                    if list1[-1] >= 21:
                        print("CONGRATULATONS!! , YOU WIN")
                        break
                    print("\nYour turn.\n")
                    player1_record()
                    if list1[-1] >= 21:
                        print("OOPS ! , YOU LOSE")
                        break

            else:
                print("Incorrect input")
        else:
            break
except Exception as e:
    print("Oops! ",e)