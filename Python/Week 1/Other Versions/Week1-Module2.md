## Python if Statement
Decision making is required when we want to execute a code only if a certain condition is satisfied. The if…elif…else statement is used in Python for decision making.

Python if Statement Syntax

```if test expression:
    statement(s)```
    
Here, the program evaluates the test expression and will execute statement(s) only if the test expression is True.
If the test expression is False, the statement(s) is not executed.

In Python, the body of the if statement is indicated by the indentation. The body starts with an indentation and the first unindented line marks the end. Python interprets non-zero values as True. None and 0 are interpreted as False.


```python
# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

```

    3 is a positive number.
    This is always printed.
    This is also always printed.
    

The body of if is executed only if the condition evaluates to True. 
When the variable num is equal to 3, test expression is true and statements inside the body of if are executed.
If the variable num is equal to -1, test expression is false and statements inside the body of if are skipped.

The print() statement falls outside of the if block (unindented). Hence, it is executed regardless of the test expression.

## Python if...else Statement
Syntax of if...else

`if test expression:
    Body of if
else:
    Body of else`
    
The if..else statement evaluates test expression and will execute the body of if only when the test condition is True. If the condition is False, the body of else is executed. Indentation is used to separate the blocks.


```python
# Program checks if the number is positive or negative
# And displays an appropriate message

num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
```

    Positive or Zero
    

In the above example, when num is equal to 3, the test expression is true and the body of if is executed and the body of else is skipped.

If num is equal to -5, the test expression is false and the body of else is executed and the body of if is skipped.

If num is equal to 0, the test expression is true and body of if is executed and body of else is skipped.

## Syntax of if...elif...else

```if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else```
    
The elif is short for else if. It allows us to check for multiple expressions. If the condition for if is False, it checks the condition of the next elif block and so on. If all the conditions are False, the body of else is executed. Only one block among the several if...elif...else blocks is executed according to the condition. The if block can have only one else block. But it can have multiple elif blocks.


```python
'''In this program, 
we check if the number is positive or
negative or zero and 
display an appropriate message'''

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```

    Positive number
    

When variable num is positive, Positive number is printed.

If num is equal to 0, Zero is printed.

If num is negative, Negative number is printed.

## Python Nested if statements
We can have a if...elif...else statement inside another if...elif...else statement. This is called nesting in computer programming.

Any number of these statements can be nested inside one another. Indentation is the only way to figure out the level of nesting. They can get confusing, so they must be avoided unless necessary.


```python
'''In this program, we input a number
check if the number is positive or
negative or zero and display
an appropriate message
This time we use nested if statement'''

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
```

    Enter a number: -3
    Negative number
    

## For Loops in Python
The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.

```Syntax of for Loop
for val in sequence:
	Body of for
```
    
Here, val is the variable that takes the value of the item inside the sequence on each iteration. Loop continues until we reach the last item in the sequence. The body of for loop is separated from the rest of the code using indentation.


```python
# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

print("The sum is", sum)
```

    The sum is 48
    

## The range() function
We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers). We can also define the start, stop and step size as range(start, stop,step_size). step_size defaults to 1 if not provided.

The range object is "lazy" in a sense because it doesn't generate every number that it "contains" when we create it. However, it is not an iterator since it supports `in`, `len` and `__getitem__` operations. This function does not store all the values in memory; it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go. To force this function to output all the items, we can use the function list().

The following example will clarify this.


```python
print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))
```

    range(0, 10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [2, 3, 4, 5, 6, 7]
    [2, 5, 8, 11, 14, 17]
    

We can use the `range()` function in for loops to iterate through a sequence of numbers. It can be combined with the `len()` function to iterate through a sequence using indexing. Here is an example.


```python
# Program to iterate through a list using indexing

#Add your favourite to the list!
genre = ['WNCC', 'Krittika', 'MnP']

# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])
```

    I like WNCC
    I like Krittika
    I like MnP
    

## for loop with else
A for loop can have an optional `else` block as well. The `else` part is executed if the items in the sequence used in for loop exhausts.

The `break` keyword can be used to stop a for loop. In such cases, the else part is ignored. Hence, a for loop's else part runs if no break occurs.

Here is an example to illustrate this.


```python
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
```

    0
    1
    5
    No items left.
    

Here, the `for` loop prints items of the list until the loop exhausts. When the `for` loop exhausts, it executes the block of code in the else and prints No items left.

This for...else statement can be used with the break keyword to run the `else` block only when the `break` keyword was not executed. Let's take an example:


```python
# program to display student's marks from record
subject_name = 'MA105'

#change MA106 to MA105 to see the marks displayed
marks = {'MA106': 90, 'PH107': 55, 'CH105': 77}

for subject in marks:
    if subject == subject_name:
        print(marks[subject])
        break
else:
    print('No entry with that name found.')
```

    No entry with that name found.
    

## While Loop
The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true. We generally use this loop when we don't know the number of times to iterate beforehand.

Syntax of while Loop in Python

```while test_expression:
    Body of while
```

In the while loop, test expression is checked first. The body of the loop is entered only if the test_expression evaluates to `True`. After one iteration, the test expression is checked again. This process continues until the test_expression evaluates to `False`.

In Python, the body of the while loop is determined through indentation. The body starts with indentation and the first unindented line marks the end. Python interprets any non-zero value as `True`. `None` and `0` are interpreted as `False`.


```python
# Program to add natural
# numbers up to 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))
# or just change n to any number of your choice and see yourself
n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)
```

    The sum is 55
    

In the above program, the test expression will be True as long as our counter variable i is less than or equal to n (10 in our program).

We need to increase the value of the counter variable in the body of the loop. This is very important (and mostly forgotten). Failing to do so will result in an infinite loop (never-ending loop).

Finally, the result is displayed.



## Break and Continue in Python
In Python, `break` and `continue` statements can alter the flow of a normal loop.

Loops iterate over a block of code until the test expression is false, but sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.

The `break` and `continue` statements are used in these cases.

#### Python break statement
The `break` statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.

If the `break` statement is inside a nested loop (loop inside another loop), the `break` statement will terminate the innermost loop.


```python
# Use of break statement inside the loop

for val in "Quarantine":
    if val == "i":
        break
    print(val)

print("The end")
```

    Q
    u
    a
    r
    a
    n
    t
    The end
    

#### Python continue statement
The `continue` statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.


```python
for val in "Coding":
    if val == "i":
        continue
    print(val)

print("The end")
```

    C
    o
    d
    n
    g
    The end
    

This program is same as the above example except the break statement has been replaced with continue.

We continue with the loop, if the string is i, not executing the rest of the block. Hence, we see in our output that all the letters except i gets printed
