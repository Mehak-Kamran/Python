#function 
def cal_avg(a,b):
    avg=(a+b)/2
    return avg

print("Enter two nos ")
user_input1=int(input())
user_input2=int(input())

avg_calculated=cal_avg(user_input1,user_input2)
print(avg_calculated)

