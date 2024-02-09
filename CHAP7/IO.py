# f=open("/workspaces/Python/CHAP7/file.txt","r")
# data=f.read()
# print(data)

# f=open("/workspaces/Python/CHAP7/file.txt","w")
# f.write("Hey this is mehak and i have trucate the file data")
# f.close()

# f=open("/workspaces/Python/CHAP7/file.txt","a")
# f.write(" Now I have appended data ")
# f.close()

# with open("/workspaces/Python/CHAP7/file.txt","r+") as f:
#     data=f.read()
#     data1=f.write("hel")
#     print(data)

# with open("/workspaces/Python/CHAP7/file.txt","a+") as f:
#     data1=f.write("hel")
#     data=f.read()
#     print(data)


 
# with open("/workspaces/Python/CHAP7/file.txt","w+") as f:
#     data1=f.write("hel")
#     data=f.read()
#     print(data)

# with open("/workspaces/Python/CHAP7/sample.txt","w") as f:
#     f.write("hello")
# import os
# os.remove("/workspaces/Python/CHAP7/sample.txt")



#1
# with open("excercise.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing java\nI like programming in java")
 #2   
# with open("excercise.txt","r") as f:
#     container0=f.read()
#     container1=container0.replace("java","python")

# with open("excercise.txt","w") as f:
#     f.write(container1)

#3
# with open("excercise.txt","r") as f:
#     container1=f.read()
#     condition=container1.find("learning")
#     if(condition!=-1):
#         print("Found")
#     else:
#         print("not found")

#4
# def lineno():
#     find="learning"
#     line=True
#     indexno=1
#     with open("/workspaces/Python/CHAP7/excercise.txt","r") as f:
#         while(line):
#             line=f.readline()
#             container=line.find(find)
#             if(container!=-1):
#                 print("found at index no",indexno)
#                 morelines=False
#                 return
            
#             indexno+=1
#     print("Not found")
                
    
# lineno()


#5
with open("/workspaces/Python/CHAP7/file.txt","w") as f:
    f.write("2,4,5,7,9,3,8,22,36")


with open("/workspaces/Python/CHAP7/file.txt","w") as f:
    f.write("2,4,5,7,9,3,8,22,36,72,81")


with open("/workspaces/Python/CHAP7/file.txt","r") as f:
    container0=f.read()
    integers=container0.split(",")
    #print(type(integers))
    count=0

    for i in integers:
        #print(type(i))
        list=int(i)
        #print(type(list))
        if list%2==0:
            count+=1
    print(count)    
      

