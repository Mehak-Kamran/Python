#CHAPTER 2 STRINGS AND CONDITIONAL
Fname="Mehak"
Lname="Kamran"

#concatenation
print("My name is",Fname+" "+Lname)

#length
print(len(Fname))

#indexing
print(Fname[1])

#slicing
print(Fname[0:4])
print(Fname[:5])
print(Fname[0:])
#the neagative indexing concept is only for slicing 
print(Lname[-3:])
print(Lname[-3:len(Lname)])

#string Functions

intro="i am beautiful"
fun=intro.capitalize()
print(fun)
fun2=intro.endswith("ul")
print(fun2)
fun3=intro.count("a")
print(fun3)
fun4=intro.replace("am","an")
print(fun4)
fun5=intro.find("beautiful")
print(fun5)

#CONDITIINAL

marks=int(input("Enter your marks "))
if(marks>=90):
    print("Your grade is A")
elif(marks<90 and marks >=80):
    print("Your grade is B")
elif(70<=marks<80):
    print("Your grade is C")
else:
    print("Your grade is D")








