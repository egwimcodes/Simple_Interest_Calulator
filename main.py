from method_formulars import simple_interest, time, rate, principle

# OFFICIALSNOWWISDOM SIMPLE INTEREST CALCULATOR

print("""
++++++++++++++++++++++++++++++++++++++++++++++++
     WELCOME TO MY SIMPLE INTEREST CALCULATOR
++++++++++++++++++++++++++++++++++++++++++++++++

     Press ==> [ 0 ] -> SIMPLE INTEREST
     Press ==> [ 1 ] -> PRINCIPAL
     Press ==> [ 2 ] -> RATE
     Press ==> [ 3 ] -> TIME
     Press ==> [ 4 ] -> QUIT
""")
try:
    to_solve = int(input("Please what would you like to calculate: "))
    while True:
        if to_solve == 0:
            simple_interest()
            break
        elif to_solve == 1:
            principle()
            break
        elif to_solve == 2:
            rate()
            break
        elif to_solve == 3:
            time()
            break
        else:
            if to_solve == 4:
                print("Quiting....")
                break
            else:
                print("Sorry the number you entered is not valid")
                break
except Exception:
    print("Sorry you input was not a number")
