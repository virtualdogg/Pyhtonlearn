n=15
G=0
while(True):

    G=G+1
    if(G>9):
        print("you have run out of guesses")
        break
    a=int(input())
    if(a==n ):
        print("Correct guess")
        print("Total guess",G)
        break
    elif(a >n):
        print("Guess again- The required number is smaller")
        print("Total guess left =",9-G)
        continue
    elif (a < n):
        print("Guess again- The required number is greater")
        print("Total guess left =", 9 - G)
        continue



