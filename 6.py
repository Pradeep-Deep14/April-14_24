#Create a python program to display
#all prime numbers within an interval

lower=100
upper=120

print("Prime Numbers between",lower,
      "and",upper,"are")

for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i)==0:
                break
        else:
            print(num)