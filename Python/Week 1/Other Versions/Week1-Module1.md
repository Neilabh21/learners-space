## Hello, World!

Now that we have Python up and running, we can write our first Python program.

Let's create a very simple program called Hello World. A "Hello, World!" is a simple program that outputs Hello, World! on the screen. Since it's a very simple program, it's often used to introduce a new programming language to beginners. Python is a very simple language, and has a very straightforward syntax. It encourages programmers to program without boilerplate (prepared) code. The simplest directive in Python is the "print" directive - it simply prints out a line (and also includes a newline, unlike in C++)

To print a string in Python 3, just write:

```print('The text to be printed')```


```python
#Try changing the code below to output your name
print('Hi! My name is Neilabh.')

#This will be printed in a newline
print('I am learning pyhton!')
```

    Hi! My name is Neilabh.
    I am learning pyhton!
    

## Variables and Types

A variable is a named location used to store data in the memory. It is helpful to think of variables as a container that holds data that can be changed later in the program.

Python is <font color=blue>completely <em>object oriented,</em></font> so you do <font color=red>not</font> need to declare variables before using them, or declare their type. 

<font color=blue>Every variable in Python is an object.</font> 

Let us explore a few basic types of variables.

## Rules and Naming Convention for Variables and constants
1. <font color=blue>Constant</font> and <font color=blue>Variable Names</font> should have a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). For example:

```snake_case
MACRO_CASE
camelCase
CapWords```

2. Create a name that makes sense. For example, `vowel` makes more sense than `v`.
3. If you want to create a variable name having two words, use underscore to separate them. For example:

```my_name
current_salary```

4. Use capital letters possible to declare a constant. For example:

```PI
G
MASS
SPEED_OF_LIGHT
TEMP```

5. Never use special symbols like !, @, #, $, %, etc.
6. Don't start a variable name with a digit.

#### 1) Numbers
Python supports two types of numbers - integers and floating point numbers (numbers with decimals). Here, we have created a variable named myint. We have assigned the value 10 to the variable and print the value.


```python
myint = 10
print(myint)

#assign your age to this variable
myage = 20
#print your age
print("My age is", myage)
```

    10
    My age is 20
    

To define a floating point number, you may use one of the following notations:


```python
myfloat = 7.0
print(myfloat)

#7e-2 means 7 x 10 ^ -2
myfloat = float(7e-2)
print(myfloat)

#change myflot to store the number of your choice and print it
newfloat = 2.99792458e8
print("Speed of Light is", newfloat, "m/s.")
```

    7.0
    0.07
    Speed of Light is 299792458.0 m/s.
    

#### 2) Strings
Strings are used to store alphanumeric data and are defined either with a single quote or a double quotes. 

The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)


```python
mystring = 'hello'
print(mystring)

#the same variable can be reassigned too!
mystring = "hello again"
print(mystring)

#here single quote is treated as apostrophe
mystring = "Don't worry about apostrophes"
print(mystring)
```

    hello
    hello again
    Don't worry about apostrophes
    

## Boolean
A Boolean can have any of the two values: True or False.

In the below program, we use boolean literal True and False. In Python, True represents the value as 1 and False as 0. The value of x is True because 1 is equal to True. And, the value of y is False because 1 is not equal to False.

Similarly, we can use the True and False in numeric expressions as the value. The value of a is 5 because we add True which has a value of 1 with 4. Similarly, b is 10 because we add the False having value of 0 with 10.


```python
x = (1 == True) #note the case of True, true/TRUE or any other are invalid
y = (1 == False) #note the case of False
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
```

    x is True
    y is False
    a: 5
    b: 10
    

###### It is also possible to assign multiple values to multiple variables. Run the code below to see!


```python
a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)
```

    5
    3.2
    Hello
    

###### If you want to assign the same value to multiple variables at once, you can do this as:


```python
x = y = z = "same"

#print these values to check yourself!
print(x, y, z)
```

    same same same
    

###### We can use the ```type()``` function to know which class a variable or a value belongs to.


```python
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", type(a))

a = 'Python'
#print its type to check the class name yourself
print(a, "is of type", type(a))
```

    5 is of type <class 'int'>
    2.0 is of type <class 'float'>
    (1+2j) is complex number? <class 'complex'>
    Python is of type <class 'str'>
    

## Python List
List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.

Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ].



```python
a = [1, 2.2, 'python']
print(a)
```

    [1, 2.2, 'python']
    

We can use the slicing operator [ ] to extract an item or a range of items from a list. The index starts from 0 in Python. To index items from backward negative integers can be used: [-1] means the last item, [-2] means the secong las item and so on.


```python
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

#a[-2:] = [35, 40]
print("a[-2:] = ", a[-2:])
```

    a[2] =  15
    a[0:3] =  [5, 10, 15]
    a[5:] =  [30, 35, 40]
    a[-2:] =  [35, 40]
    

Lists are mutable, meaning, the value of elements of a list can be altered.


```python
a = [1, 2, 3]
a[2] = 4
print(a)

#see the last item to check
a[-1] = 78
print('Last item = ', a[2])
```

    [1, 2, 4]
    Last item =  78
    

## Python Tuple
Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.

Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically. We can use the slicing operator [] to extract items but we cannot change its value.


It is defined within parentheses () where items are separated by commas.


```python
t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])
```

    t[1] =  program
    t[0:3] =  (5, 'program', (1+3j))
    


```python
# Run this code to see that it generates error
# Tuples are immutable
t[0] = 10
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-13-bcfa9279d250> in <module>
          1 # Run this code to see that it generates error
          2 # Tuples are immutable
    ----> 3 t[0] = 10
    

    TypeError: 'tuple' object does not support item assignment


###### Just like a list and tuple, the slicing operator [ ] can be used with strings. Strings, however, are immutable.


```python
s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6] = 'w', alter the statement below to print world
print(None)
```

    s[4] =  o
    None
    


```python
# Run the code below to see it generates error
# Strings are immutable in Python
s = 'Hello world!'
s[5] ='d'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-15-1687d10c2dbf> in <module>
          2 # Strings are immutable in Python
          3 s = 'Hello world!'
    ----> 4 s[5] ='d'
    

    TypeError: 'str' object does not support item assignment


## Python Set
Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.


```python
a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))
```

    a =  {1, 2, 3, 4, 5}
    <class 'set'>
    

We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates.


```python
a = {1,2,2,3,3,3}
print(a)
```

    {1, 2, 3}
    

Since, set are unordered collection, indexing has no meaning. Hence, the slicing operator [] does not work.


```python
a = {1,2,3}

#run this code to see it produces an error
a[1]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-18-736e219dfaef> in <module>
          2 
          3 #run this code to see it produces an error
    ----> 4 a[1]
    

    TypeError: 'set' object is not subscriptable


## Python Dictionary
Dictionary is an unordered collection of key-value pairs.

It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.

In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type. We use key to retrieve the respective value. But not the other way around.


```python
d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])
```

    <class 'dict'>
    d[1] =  value
    d['key'] =  2
    


```python
# run this code to see it generates error
print("d[2] = ", d[2])
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-20-f4206cf449b2> in <module>
          1 # run this code to see it generates error
    ----> 2 print("d[2] = ", d[2])
    

    KeyError: 2


## Conversion between data types
We can convert between different data types by using different type conversion functions like int(), float(), str(), etc.
<font color=blue>Conversion from float to int will truncate the value (make it closer to zero).</font>
Conversion to and from string must contain compatible values.


```python
print(float(5))

print(int(10.6))
print(int(-10.6))

print(float('2.5'))
print(str(25))
```

    5.0
    10
    -10
    2.5
    25
    


```python
#generates error
print(int('1p'))
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-22-d4f93f31bc19> in <module>
          1 #generates error
    ----> 2 print(int('1p'))
    

    ValueError: invalid literal for int() with base 10: '1p'


We can even convert one sequence to another. To convert to dictionary, each element must be a pair:


```python
#list ot set
print(set([1,2,3]))

#set to tuple
print(tuple({5,6,7}))

#string to list
print(list('hello'))

#list to dict
print(dict([[1,2],[3,4]]))

#tuple to dict
print(dict([(3,26),(4,44)]))
```

    {1, 2, 3}
    (5, 6, 7)
    ['h', 'e', 'l', 'l', 'o']
    {1: 2, 3: 4}
    {3: 26, 4: 44}
    

## Operators
Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.

### Arithmetic operators
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

* `+`	Add two operands or unary plus
* `-`	Subtract right operand from the left or unary minus
* `*`	Multiply two operands

* `/`	Divide left operand by the right one (always results into float)
* `%`	Modulus - remainder of the division of left operand by the right
* `//`	Floor division - division that results into whole number adjusted to the left in the number line
* `**`	Exponent - left operand raised to the power of right


```python
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)
```

    x + y = 19
    x - y = 11
    x * y = 60
    x / y = 3.75
    x // y = 3
    x ** y = 50625
    

### Comparison operators
Comparison operators are used to compare values. It returns either True or False according to the condition.

* `>`	Greater than - True if left operand is greater than the right
* `<`	Less than - True if left operand is less than the right
* `==`	Equal to - True if both operands are equal	
* `!=`	Not equal to - True if operands are not equal	
* `>=`	Greater than or equal to - True if left operand is greater than or equal to the right	
* `<=`	Less than or equal to - True if left operand is less than or equal to the right


```python
x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)
```

    x > y is False
    x < y is True
    x == y is False
    x != y is True
    x >= y is False
    x <= y is True
    

### Logical operators
Logical operators are the and, or, not operators.

* `and`	True if both the operands are true
* `or`	True if either of the operands is true
* `not`	True if operand is false (complements the operand)


```python
x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)
```

    x and y is False
    x or y is True
    not x is False
    

### Assignment operators
Assignment operators are used in Python to assign values to variables. a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.

There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same. It is equivalent to a = a + 5.

Operator | Example | Equivalent to
--- | --- | ---
= | x = 5 |	x = 5
+=	| x += 5 | x = x + 5
-=	| x -= 5 |	x = x - 5
*=	| x *= 5 |	x = x * 5
/=	| x /= 5 |	x = x / 5
%=	| x %= 5 |	x = x % 5
//=	| x //= 5 |	x = x // 5
**=	| x **= 5 |	x = x ** 5

### Identity operators
`is` and `is not` are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

Operator | Meaning | Example
--- | --- | ---
`is` | True if the operands are identical (refer to the same object) | x is True
`is not` | True if the operands are not identical (do not refer to the same object) | x is not True


```python
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)
```

    False
    True
    False
    

### Membership operators
in and not in are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

In a dictionary we can only test for presence of key, not the value.

Operator | Meaning | Example
--- | --- | ---
`in` | True if value/variable is found in the sequence | 5 in x
`not in` | True if value/variable is not found in the sequence | 5 not in x


```python
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)
```

    True
    True
    True
    False
    

Here, 'H' is in x but 'hello' is not present in x (remember, Python is case sensitive). Similarly, 1 is key and 'a' is the value in dictionary y. Hence, 'a' in y returns False.
