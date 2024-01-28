 #1
 name= input("Enter your First Name ")
 length=len(name)
 print("Your name length is" ,length)

 #2
 string=input("Enter a string that contain $ sign")
 measur=string.count("$")
 print("$ occur",measur,"times in your string")

 #3
 integer=int(input("Enter a integer "))
 checkpoint= integer%2
 if(checkpoint==0):
     print("Even")
 else:
     print("Odd")


 #4
 print("Enter any three integers ")
 num1=int(input())
 num2=int(input())
 num3=int(input())

 if(num1>num2):
     if(num1>num3):
       print(num1,"is greatest")
     else:
         print(num3,"is greatest")

 elif(num2>num3):
    print(num2,"is greatest")
else:
     print(num3,"is greatest")

#5
num=int(input("Enter an integer "))

checkpoint2=num%7
if(checkpoint2==0):
    print(num,"is multiple of 7")
else:
    print("not multiple of 7")


