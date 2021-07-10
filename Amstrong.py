import math                         # import all math files 
num=int(input("Enter a value"))
sum=0
temp=num
while(num!=0):
    r=num%10
    sum=sum+pow(r,3)
    num=num//10
if(temp==sum):
    print("An Amstrong Number")
else:
    print("Not an Amstrong Number")