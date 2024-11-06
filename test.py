#CONDITIONS
#conditions.exc.1
l1: list [float] = []
for _ in range (2):
    num: float = float(input("enter a float: "))
    l1.append(num)
for _ in range (3):
    print (min(l1))

#conditions.exc.2
import statistics
l1: list [int] = []
for _ in range (2):
    num: int = int(input("enter an integer: "))
    l1.append(num)
print(statistics.mean(l1))

#conditions.exc.3
l1: list [float] = []
for _ in range (3):
    num: float = float(input("enter a float: "))
    l1.append(num)
print(max(l1))

#conditions.exc.4
movie_length: int = int(input("enter movie length in minutes: "))
print (f"the movie in {movie_length//60} hours and {movie_length%60} minutes long")

#conditions.exc.5
num: int = int(input("enter a 4 digit number: "))
if 1000<=num<=9999:
    print (f"the right most digit is {((num%1000)%100)%10}")
else:
    pass

#conditions.exc.6
num: int = int(input("enter a 4 digit number: "))
if 1000<=num<=9999:
    print (f"the right most digit is {((num%1000)%100)//10}")
else:
    pass

#conditions.exc.7
num: int = int(input("enter a 2 digit number: "))
while not 10<=num<=99:
    print("num must be 2 digits")
    num: int = int(input("enter a 2 digit number: "))
else:
    print(f"{(num // 10) + (num % 10)}")

#conditions.exc.8
num: int = int(input("enter a 2 digit number: "))
while not 10<=num<=99:
    print("num must be 2 digits")
    num: int = int(input("enter a 2 digit number: "))
else:
    print(f"{(num // 10) +((num%10)*10)}")

#conditions.exc.9
num: int = int(input("enter a number: "))
if num %2 == 0:
    print ("even")
else:
    print ("odd")

#conditions.exc.10
salary: int = int(input("what is your salary: "))
if salary <=6000:
    print("you dont owe income tax")
if 6000<salary<=12000:
    print(f"you owe {(salary-6000)*0.1} income tax")
if 12000<salary<=18000:
    print(f" you owe {((salary-12000)*0.2)+600} income tax")
if 18000<salary <=25000:
    print(f"you owe {((salary-18000)*0.3)+1800} income tax")
if 25000<salary <=35000:
    print(f"you owe {((salary-25000)*0.4)+3900} income tax")
if 35000< salary<=50000:
    print(f"you owe {((salary-35000)*0.45)+7900} income tax")
if salary>50000:
    print(f"you owe {((salary-50000)*0.51)+14650} income tax")

#conditions.exc.11
age: int = int(input('enter you age: '))
height: int = int(input('enter you height: '))
if 8<=age<18 and height>115:
    print( "you may enter")
if age >=18 and height >100:
    print("you may enter")
else:
    print ("sorry you cant")

#LOOPS
#loops.exc.1
top: int = int(input("enter an integer:"))
for i in range (1,top+1):
    print (i, end =" ")

#loops.exc.2
num1: int = int(input("enter an integer: "))
num2: int = int(input("enter an integer: "))

if num1>num2:
    for i in range (num2,num1+1,1):
        print (i, end =" ")
else:
    for i in range (num1,num2+1,1):
        print (i, end =" ")

#loops.exc.3
n: int = int(input("enter a number: "))
for i in range (2,n+1,2):
    print (i, end =" ")

#loops.exc.4
den: int = int(input("enter an integer: "))
max: int = int(input("enter an integer: "))
for i in range (den, max+1, den):
    print (i, end =" ")

#DATA_ANALYSIS
#data_analysis.exc.1
sentinel: int = 99
num_sum: int = 0
while True:
    num: int = int(input("enter a number: "))
    if num== sentinel:
        if num_sum ==0:
            print("None")
        break
    num_sum+= num
if num_sum != 0:
    print (num_sum)

#data_analysis.exc.2
sentinel: int =0
num: int = int(input("enter a number: "))
max_num: int = num
min_num: int = num
while True:
    num: int = int(input("enter a number: "))
    if num <= sentinel:
        break
    if num<min_num:
        min_num = num
    if num>max_num:
        max_num = num
print (max_num)
print (min_num)

#data_analysis.exc.3
max_num: int = 0
num1: int = int(input("enter a number: "))
num2: int = int(input("enter a number: "))
num3: int = int(input("enter a number: "))
num4: int = int(input("enter a number: "))
num5: int = int(input("enter a number: "))

if num1>num2 and num1>num3 and num1>num4 and num1>num5:
    print (f"the first number ({num1}) is the largest")
if num2>num1 and num2>num3 and num2>num4 and num2>num5:
    print(f"the second number ({num2}) is the largest")
if num3>num1 and num3>num2 and num3>num4 and num3>num5:
    print(f"the third number ({num3}) is the largest")
if num4>num1 and num4>num2 and num4>num3 and num4>num5:
    print(f"the forth number ({num4}) is the largest")
if num5>num1 and num5>num2 and num5>num3 and num5>num4:
    print(f"the fifth number ({num5}) is the largest")
#data_analysis.exc.4
num1: int = int(input("enter a number: "))
num2: int = int(input("enter a number: "))
num_sum: int = 0
for _ in range (num2):
    num_sum += num1
print (num_sum)

#data_analysis.exc.5
num1: int = int(input("enter a number: "))
num2: int = int(input("enter a number: "))
num_sum1: int = 1
num_sum2: int = 1
for _ in range (num2):
    num_sum1 *= num1
print (f"{num1}**{num2} =",num_sum1)
for _ in range (num1):
    num_sum2 *= num2
print (f"{num2}**{num1} =",num_sum2)

#data_analysis.exc.6
#data_analysis.exc.7
num1: int = int(input("enter a number: "))
num2: int = int(input("enter a number: "))
x: int = 0
y: int = 0
if num1 > num2:
    for i in range(1,num2):
        if num2%i== 0:
            if num1%i==0:
                x = i
    print (x)
if num1 < num2:
    for i in range(1,num1):
        if num2%i== 0:
            if num1%i==0:
                x = i
    print (x)

#data_analysis.exc.8
while True:
    num: int = int(input("Enter a number: "))
    if num == sentinel:
        break
    if num < 1:
        print("Number must be positive")
    else:
        if num == 1:
            print("1 is not prime number")
        else:
            divider: int = 2
            while divider < num:
                if num % divider == 0:
                    break
                divider += 1
            if divider < num:
                print(f"{num} is not prime")
            else:
                print(f"{num} is prime")
#COMPLEX_LOOPS
#complex_loops.exc.1
##complex_loops.exc.2
voting_subject: str = input("what are we voting on: ")
vote_list: list[int] = []
country_list: list[int] = []
against: int = 0

for i in range (6):
    try:
        vote: int = int(input("cast your vote: 1.'in favor', 2.'against', 3. ,'abstaining', 4. 'veto': "))
        if 1<=vote<=4:
            vote_list.append(vote)
            country_list.append(i)
            if vote ==2:
                against = i
        if vote == 4:
            country_list.append(i)
            vote_list.append(vote)
            break
    except:
        pass
if 4  in vote_list:
    print (f"country number {i+1} vetoed the subject")
else:
    print (f"{vote_list.count(1)} countries voted 'in favor'")
    print (f"{vote_list.count(2)} countries voted 'against'")
    print (f"{vote_list.count(3)} countries voted 'abstaining'")
    if 1 in vote_list:
        print (f"country number {(vote_list.index(1))+1} was the first to vote 'in favor'")
    print (f"country number {against+1} was the last to vote 'against'")