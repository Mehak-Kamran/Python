#1
score=[1,4,9,16,25,46,49,64,81,100]
for s in score:
    print(s)

#2
id=(1,4,9,16,25,46,49,64,81,100)
search=int(input("Enter id to search"))
for i in id:
    if(i==search):
        print("Element Found")
        break
else:
    print("Element not found")