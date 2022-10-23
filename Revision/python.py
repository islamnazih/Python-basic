# Game 
# Start >>>>> Welcome massage  , choices
# enter game number
# Start Game [1:100] , sentence no duplicate
# ask play again Y , N
#   


def divide(x,y):
    for n in range(1,101):
        if n%x == 0 and n%y == 0 :
            print(n)


# divide(7,10)


def duplicate(sentance):
    Words = []
    for x in sentance.split(" "):   
        if  x in Words:
            pass
        else:
            Words.append(x)
    print(" ".join(Words)) #convert list to string 

duplicate("Hello my name is is is islam")