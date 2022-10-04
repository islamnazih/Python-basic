# Password Guess
# ---------------------------

tries = 4
mainpassword = "islam@123"

inputpass = input("enter your password: ")

while inputpass  != mainpassword:

    tries -= 1 #tries - 1

    print(f"wrong password {'last' if tries == 0 else tries } chance")
    inputpass = input("enter your password: ")

    if tries == 0:
        print("All tries finsish")

        break
else :
    print("correct pass ")