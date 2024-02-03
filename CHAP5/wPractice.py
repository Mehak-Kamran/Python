#1
i=1
while i<=100:
    print(i)
    i+=1
#2
j=100
while j>=1:
    print(j)
    j-=1

#3
integer=int(input("Enter a no "))
k=1
while k<=10:
    print(integer,"x",k,"=",integer*k)
    k+=1

#4
score=[1,4,9,16,25,46,49,64,81,100]
g=0
while g<len(score):
    print(score[g])
    g+=1

#5
list=(1,4,9,16,25,46,49,64,81,100)
t=0
search=int(input("Enter element to search"))
while t<=len(list):
    if(list.index(search)):
        print("value found")
    
    t+=1
print(list[in])
    