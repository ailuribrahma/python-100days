#type casting is two types
#1. implicit type casting(sytetem will do it for you)
#2. explicit type casting(you will do it)

print("before type casting")
print("123" + "456")

print("after type casting")
print(int("123") + int("456"))

print("number of letters in your name   = " + str(len(input("enter your name: "))))

# let's break down the above code
name_of_the_user = input("enter your name: ")
length_of_name = len(name_of_the_user)


print(type("number of letters in your name   = " )) #str
print(type(length_of_name)) #int

print("number of letters in your name   = " + str(length_of_name))