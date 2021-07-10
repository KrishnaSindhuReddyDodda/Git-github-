num=int(input("enter a value"))
sum=0
temp=num
while(num!=0):
    r=num%10
    sum=sum*10+r
    num=num//10
if(temp==sum):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")