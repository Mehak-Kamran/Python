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

with open("/workspaces/Python/CHAP7/sample.txt","w") as f:
    f.write("hello")
import os
os.remove("/workspaces/Python/CHAP7/sample.txt")

