print("welcome to the the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    disablity = input("Do you have any disablity? ")
    if age < 12:
        print("Please pay $5.")
        if disablity == True:
            print("You get 50% discount, please pay $2.5")
        else:
            print("No discount")
    elif age <= 18:
        print("Please pay $7.")
        if disablity == True:
            print("You get 50% discount, please pay $3.5")
        else:
            print("No discount")
    elif age < 19:
         print("Please pay $12.")        
         if disablity == True:
                print("You get 50% discount, please pay $6")
    else:
        print("No discount")                                    
else:
    print("Sorry, you have to grow taller before you can ride.")        