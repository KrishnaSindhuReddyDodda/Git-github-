num = int(input("Enter the Number: "))

for i in range(0, num):
    for j in range(0, i+1):
        print("*", end="")
    print()

for i in range(1, num):
    for j in range(0, num-i):
        print("*", end="")
    print()
