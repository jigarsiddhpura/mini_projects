n = 50       # actual no.

i = 5        # no. of guesses u have
print("you have only 5 guesses")
while(i>0):
    n1 = int(input("guess the number = "))
    i=i-1
    if n1 > 50:
        print("number guessed is greater than actual")
    elif n1 < 50:
        print("number guessed is smaller than actual")
    else:
        print("YOU WON,no. of guess you took is",5-i)
        break
    print("no. of guess left is", i)
if i==0:
    print("you lose")