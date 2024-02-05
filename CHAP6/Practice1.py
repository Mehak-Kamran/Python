#1
# no=int(5)
# def natural_no(no):
#     if no==0:
#         return 0
#     else:
#         return natural_no(no-1)+no

# cal_natural_n0=natural_no(no)
# print(cal_natural_n0)

#2
list=["apple","orange","banana"]
length=len(list)

def printout(length):
    if length<0:
        return 
    else:
        printout(length-1)
        print(list[length])

printout(length-1)
