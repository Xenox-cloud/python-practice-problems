def Prime(n):
    if n < 0:
        return 2
    if n == 5 or n == 7 or n == 3 or n == 2 or n == 1:
        return 0
    if n%2==0 or n%3==0 or n%5==0 or n%7==0:
        return 1
    else:
        return 0
prime_list = []
num = int(input("Enter a number: "))
for i in range(2,(num**2)):
    if Prime(i)==0:
        print("prime",i)
        prime_list.append(i)
    else:
        print("not prime")
print(prime_list)