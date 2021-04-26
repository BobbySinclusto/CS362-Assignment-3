n = -1
while True:
    try:
        n=int(input("Enter year: "))
    except:
        pass
    if n >= 0:
        break
    print("Invalid year, try again")

print(n, "is a leap year!" if n%4==0 and (n%400==0 or n%100!=0) else "is not a leap year.")
