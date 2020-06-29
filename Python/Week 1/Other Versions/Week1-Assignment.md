# Welcome to the first assignment of this course

As you know, each week in this course is dedicated to certain specific topics and the assignment format is carefully designed to suit the content that the students have to be evaluated upon. Since, this was the first week and your introduction to Python, the assignments are basic level and wherein you have to complete the program to generate the expected output.

Each question has a function written (don't worry you will be introduced to functions next week :), you just have to complete the program and run the subsequent cells which have the code to evalute the output of your function. If your program matches the required output, you get a point! There are 5 questions, minimum passing criteria is to get 3/5 points.

## Q1) Sum of Digits
You're given an integer $N$. Write a program to calculate the sum of all the digits of $N$.

#### One Implementation


```python
#complete the program below
def calculate_sum(N):
    #you can use the variable N in your code
    #initialise this variable to required value
    sum_digits = 0
    
    #write the code to calculate sum here. Hint - use can use loops
    for digit in str(N):
        sum_digits += int(digit)
    
    return sum_digits
```


```python
#do not change this
print(calculate_sum(1234567))
print(calculate_sum(9900))
```

    28
    18
    

#### A Shorter Implementation


```python
def calculate_sum(N):
    sum_digits = sum([int(x) for x in list(str(N))])
    return sum_digits
```


```python
#do not change this
print(calculate_sum(1234567))
print(calculate_sum(9900))
```

    28
    18
    

##### Expected output :  
``28``

``18``

## Q2) Factorial
You're given an integer $N$ (where $ N < 100$). Write a program to calculate the $N!$.

#### One Implementation


```python
#complete the program below
def calculate_fac(N):
    #you can use the varibale N in your code
    #initialise this variable to required value
    factorial = 1
    
    #write the code to calculate factorial here. 
    if (N != 0):
        for integer in range(1, N+1):
            factorial *= integer
            
    return factorial
```


```python
#do not change this code
print(calculate_fac(0))
print(calculate_fac(12))
```

    1
    479001600
    

#### A Shorter Implementation


```python
#complete the program below
def product(array):
    if len(array)==0: return 1
    else: return array[0] * product(array[1:])

def calculate_fac(N):
    return product(range(1, N + 1))
```


```python
#do not change this code
print(calculate_fac(0))
print(calculate_fac(12))
```

    1
    479001600
    

##### Expected output:

`1`

`479001600`

## Q3) Mahasena

Kattapa, as you all know was one of the greatest warriors of his time. The kingdom of Maahishmati had never lost a battle under him (as army-chief), and the reason for that was their really powerful army, also called as Mahasena.

Kattapa was known to be a very superstitious person. He believed that a soldier is "lucky" if the soldier is holding an even number of weapons, and "unlucky" otherwise. He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" soldiers, and "NOT READY" otherwise.

Given the number of weapons each soldier is holding, your task is to determine whether the army formed by all these soldiers is "READY FOR BATTLE" or "NOT READY".


The input consists of a single integer `N` denoting the number of soldiers and a list `Weapons` of integers A1, A2, ..., AN, where Ai denotes the number of weapons that the ith soldier is holding. You have to print whether the army is `READY FOR BATTLE` or `NOT READY`. Output is case sensitive!

#### One Implementation


```python
#complete the program below
def is_ready(N, Weapons):
    Lucky = 0
    for soldier in Weapons:
        if (soldier % 2 == 0):
            Lucky += 1
    if (2 * Lucky > N):
        print("READY FOR BATTLE")
    else:
        print("NOT READY")
```


```python
#do not change this code
is_ready(6, [1, 2, 3, 4, 5, 6])
is_ready(4, [20, 24, 25, 228])
```

    NOT READY
    READY FOR BATTLE
    

#### A Shorter Implementation


```python
#complete the program below
def is_ready(N, Weapons):
    if (sum([x % 2 for x in Weapons]) * 2 < len(Weapons)):
        print("READY FOR BATTLE")
    else:
        print("NOT READY")
```


```python
#do not change this code
is_ready(6, [1, 2, 3, 4, 5, 6])
is_ready(4, [20, 24, 25, 228])
```

    NOT READY
    READY FOR BATTLE
    

#### One Liner


```python
#complete the program below
def is_ready(N, Weapons):
    print("READY FOR BATTLE") if (sum([x % 2 for x in Weapons]) * 2 < len(Weapons)) else print("NOT READY")
```


```python
#do not change this code
is_ready(6, [1, 2, 3, 4, 5, 6])
is_ready(4, [20, 24, 25, 228])
```

    NOT READY
    READY FOR BATTLE
    

##### Expected output:

`NOT READY`

`READY FOR BATTLE`

## Q 4) Little Elephants

A Little Elephant and his friends from the Zoo of Powai like candies very much.

There are $N$ elephants in the Zoo. The elephant with number $K$ ($1 \leqslant K \leqslant N$) will be happy if he receives at least $A_K$ candies. There are $C$ candies in all in the Zoo.

The Zoo staff is interested in knowing whether it is possible to make all the $N$ elephants happy by giving each elephant at least as many candies as he wants, that is, the $K^{th}$ elephant should receive at least $A_K$ candies. Each candy can be given to only one elephant. Print `Yes` if it is possible and `No` otherwise.

The input consists of integers $N$ and $C$, the total number of elephants and the total number of candies in the Zoo respectively. The third input `candies` is a list and contains $N$ integers $A_1, A_2, ..., A_N$. 

For each test case output exactly one line containing the string `Yes` if it possible to make all elephants happy and the string `No` otherwise. Output is case sensitive. So do not print `YES` or `yes`.


#### One Implementation


```python
#complete the program below
def all_happy(N, C, candies):
    if (sum(candies) < C):
        print("Yes")
    else:
        print("No")
```


```python
#do not change this code
all_happy(6, 8, [1, 1, 2, 2, 1, 2])
all_happy(5, 575, [0, 110, 120, 130, 140])
```

    No
    Yes
    

#### One-Liner


```python
#complete the program below
def all_happy(N, C, candies):
    print("Yes") if (sum(candies) < C) else print("No")
```


```python
#do not change this code
all_happy(6, 8, [1, 1, 2, 2, 1, 2])
all_happy(5, 575, [0, 110, 120, 130, 140])
```

    No
    Yes
    

##### Expected Output: 

`No`

`Yes`

## Q 5) COVID Pandemic and Long Queue

Due to the COVID pandemic, people have been advised to stay at least $6$ feet away from any other person. Now, people are lining up in a queue at the local shop and it is your duty to check whether they are all following this advice.

There are a total of $N$ spots (numbered $1$ through $N$) where people can stand in front of the local shop. The distance between each pair of adjacent spots is $1$ foot. Each spot may be either empty or occupied; you are given a sequence $A_1,A_2,\cdots,A_N$, where for each valid $i$, $A_i=0$ means that the $i^{th}$ spot is empty, while $A_i=1$ means that there is a person standing at this spot. It is guaranteed that the queue is not completely empty.

For example, if $N=11$ and the sequence $A$ is $(0,1,0,0,0,0,0,1,0,0,1)$, then this is a queue in which people are not following the advice because there are two people at a distance of just $3$ feet from each other.

You need to determine whether the people outside the local shop are following the social distancing advice or not. As long as some two people are standing at a distance smaller than $6$ feet from each other, it is bad and you should report it, since social distancing is not being followed.

##### Input format
The first input is N. The next input `queue` is in the form of a dictionary where each element is given as `'spot_number: value (0 or 1)`

Example: the above sequence would be in input as:

`{'1' : 0,  '2' : 1,  '3' : 0,  '4' : 0,  '5' : 0,  '6' : 0,  '7' : 0,  '8' : 1,  '9' : 0,  '10' : 0,  '11' : 1}`

##### Output format
For each test case, print a single line containing the string `Yes` if social distancing is being followed or `No` otherwise. Output is case-sensitive!


```python
#complete the program below
def social_dist(N, queue):
    flag = 0
    list_key = []
    
    for key_name in queue:
        if(queue[key_name] == 1):
            list_key.append(int(key_name))

    for x, y in zip(list_key[0::], list_key[1::]):
        if (y - x < 6):
            print("No")
            flag = 1
    
    if flag == 0: print("Yes")
            
            
```


```python
#do not change this code
queue1 = {'1':1, '2':0, '3':0, '4':0, '5':1}
social_dist(5, queue1)

queue2 = {'1':0, '2':0, '3':1, '4':0, '5':0, '6':0, '7':0, '8':0, '9':1, '10':0}
social_dist(10, queue2)
```

    No
    Yes
    

##### Expected output:

`No`

`Yes`
