#1
list=["apple","orange","banana"]

def length_of_list(list):
      length=len(list)
      return length

cal_list_lengt=length_of_list(list)
#print(cal_list_lengt)

#2
vegeies=["ladyfinger","potato","carrot"]

def print_vegies(list):
    for i in range(3):
       print(vegeies[i],end=" ")

#print_vegies(vegeies)
print()

#3
user_input=int(input("Enter an int "))


def factorial(user_input):
     fact=1
     
     for i in range(user_input+1,0):
        fact=fact*i
        return fact


cal_fact= factorial(user_input)
print(cal_fact)