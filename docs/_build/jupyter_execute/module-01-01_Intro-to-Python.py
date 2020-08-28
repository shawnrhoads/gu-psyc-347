# Intro to Python Basics

This tutorial has been adapted from the following resources on Jupyter Notebooks and Python:
- Luke Chang's [DartBrains](https://dartbrains.org)
- [NumPy Quickstart Tutorial](https://numpy.org/devdocs/user/quickstart.html)

## Types of Variables
- Numeric types:
    - int, float, long, complex
- string
- boolean
    - True / False
    
Python's simple types are summarized in the following table:

**<center>Python Scalar Types</center>**

| Type        | Example        | Description                                                  |
|-------------|----------------|--------------------------------------------------------------|
| ``int``     | ``x = 1``      | integers (i.e., whole numbers)                               |
| ``float``   | ``x = 1.0``    | floating-point numbers (i.e., real numbers)                  |                  
| ``complex`` | ``x = 1 + 2j`` | Complex numbers (i.e., numbers with real and imaginary part) |
| ``bool``    | ``x = True``   | Boolean: True/False values                                   | 
| ``str``     | ``x = 'abc'``  | String: characters or text                                   | 
| ``NoneType``| ``x = None``   | Special object indicating nulls                              | 

Use the `type()` function to find the type for a value or variable

# Integer
a = 1
print(type(a))

# Float
b = 1.0
print(type(b))

# String
c = 'hello'
print(type(c))

# Boolean
d = True
print(type(d))

# None
e = None
print(type(e))

# Cast integer to string
print(type(str(a)))

## Math Operators
- +, -, *, and /
- Exponentiation **
- Modulo % (Remainder)

# Addition
a = 2 + 7
print(a)

# Subtraction
b = a - 5
print(b)

# Multiplication
print(b*2)

# Exponentiation
print(b**2)

# Modulo
print(b%9)

# Division
print(b/9)

## String Operators
Some of the arithmetic operators also have meaning for strings. E.g. for string concatenation use + sign

String repetition: Use * sign with a number of repetitions

# Combine string
a = 'Hello'
b = 'World'
print(a + b)

# Repeat String
print(str(a+' ')*5)

## Logical Operators

Perform logical comparison and return Boolean value

```
x == y # x is equal to y
x != y # x is not equal to y
x > y # x is greater than y
x < y # x is less than y
x >= y # x is greater than or equal to y 
x <= y # x is less than or equal to y
```

# Works for string
a = 'hello'
b = 'world'
c = 'Hello'
print("a==b: " + str(a==b))
print("a==c: " + str(a==c))
print("a!=b: " + str(a!=b))
print()

# Works for numeric
d = 5
e = 8
print("d < e: " + str(d < e))

## Conditional Logic (if…)

Unlike most other languages, Python uses tab formatting rather than closing conditional statements (e.g., end)

Syntax:
```
if condition: 
    do something
```

Implicit conversion of the value to bool() happens if condition is of a different type than bool, thus all of the following should work:
```
if condition:
    do_something
elif condition:
    do_alternative1
else:
    do_otherwise # often reserved to report an error
                 # after a long list of options
    ```

n = 2

if n:
    print("n is non-0") #note spacing

if n is None:
    print("n is None")
    
if n is not str:
    print("n is not string")

## Loops
**for** loop is probably the most popular loop construct in Python:
```
for target in sequence:
    do_statements
```

string = "Python is going to make conducting research easier"
for c in string:
    print(c)

for i in [1,2,3,4,5]:
    print(i)

It’s also possible to use a **while** loop to repeat statements while condition remains True:
```
while condition do:
    do_statements
```

x = 0
end = 10

csum = 0
while x < end:
    csum += x
    print(x, csum)
    x += 1
print("Exited with x==%d" % x )

## Functions

A **function** is a named sequence of statements that performs a computation. You define the function by giving it a name, specify a sequence of statements, and optionally values to return. Later, you can “call” the function by name.

def make_upper_case(text):
    return (text.upper())

- The expression in the parenthesis is the **argument**.
- It is common to say that a function **"takes" an argument** and **"returns" a result**.
- The result is called the **return value**.

The first line of the function definition is called the header; the rest is called the body.

The header has to end with a colon and the body has to be indented. It is a common practice to use 4 spaces for indentation, and to avoid mixing with tabs.

Function body in Python ends whenever statement begins at the original level of indentation. There is no end or fed or any other identify to signal the end of function. Indentation is part of the the language syntax in Python, making it more readable and less cluttered.

string = "Python is going to make conducting research easier"
string_upper = string.upper()
print(string_upper)

make_upper_case(string)

## Python Containers

There are 4 main types of builtin containers for storing data in Python:
- list $\checkmark$
- dict $\checkmark$
- set
- tuple

### Lists
In Python, a list is a mutable sequence of values. Mutable means that we can change separate entries within a list. 
- Each value in the list is an element or item
- Elements can be any Python data type
- Lists can mix data types

- Lists are initialized with [] or list()
```
l = [1,2,3]
```

- Elements within a list are indexed (starting with 0)
```
l[0]
```

- Elements can be nested lists
```
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

- Lists can be sliced.
```
l[start:stop:stride]
```

- Like all python containers, lists have many useful methods that can be applied
```
a.insert(index,new element)
a.append(element to add at end)
len(a)
```

- List comprehension is a very powerful technique allowing for efficient construction of new lists.
```
[a for a in l]
```

list = [1,2,3]
list

list_str = ['hello', 'bye', 'hi']

[i.upper() for i in list_str]

[index*9 for index in list]

# Indexing and Slicing
a = ['lists','are','arrays']
print(a[0])
print(a[1:3])

# List methods
a.insert(2,'python')
a.append('.')
print(a)
print(len(a))

# List Comprehension
print([x.upper() for x in a])

list = [1,2,3,4,5]
list[0::2]

### Dictionaries
- In Python, a dictionary (or dict) is mapping between a set of indices (keys) and a set of values
- The items in a dictionary are key-value pairs
- Keys can be any Python data type
- Dictionaries are unordered

# Dictionaries
eng2sp = {}
eng2sp['one'] = 'uno'
print(eng2sp)
print()

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print()

print(eng2sp.keys())
print(eng2sp.values())

## Classes
*(from: https://realpython.com/python3-object-oriented-programming/)*

"The primitive data structures available in Python, like numbers, strings, and lists are designed to represent simple things like the cost of something, the name of a poem, and your favorite colors, respectively.

What if you wanted to represent something much more complicated?

For example, let’s say you wanted to track a number of different animals. If you used a list, the first element could be the animal’s name while the second element could represent its age.

How would you know which element is supposed to be which? What if you had 100 different animals? Are you certain each animal has both a name and an age, and so forth? What if you wanted to add other properties to these animals? This lacks organization, and it’s the exact need for classes.

Classes are used to create new user-defined data structures that contain arbitrary information about something. In the case of an animal, we could create an Animal() class to track properties about the Animal like the name and age.

It’s important to note that a class just provides structure—it’s a blueprint for how something should be defined, but it doesn’t actually provide any real content itself. The Animal() class may specify that the name and age are necessary for defining an animal, but it will not actually state what a specific animal’s name or age is.

It may help to think of a class as an idea for how something should be defined."

![img](https://cdn-media-1.freecodecamp.org/images/M4t8zW9U71xeKSlzT2o8WO47mdzrWkNa4rWv)


# let's create a cat class
class Cat:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = True
        self.tired = True
        self.mood = 5

    # instance method
    def description(self):
        __name_age__ = "{} is {} years old. ".format(self.name, self.age)
        
        if self.tired == True:
            __is_tired__ = "{} is tired. ".format(self.name)
        else:
            __is_tired__ = "{} is not tired. ".format(self.name)
        
        if self.hungry == True:
             __is_hungry__ = "{} is hungry. ".format(self.name)
        else:
            __is_hungry__ = "{} is not hungry. ".format(self.name)
        
        return str(__name_age__+__is_tired__+__is_hungry__)

    # instance method
    def meow(self):
        return "{} says {}".format(self.name, "Meow! Meow!")
    
    def feed(self):
        self.hungry = False
        self.mood = self.mood + self.mood*.5
        print(self.meow())
        
    def sleep(self):
        self.tired = False
    
        

# Instantiate the Cat object
kitty = Cat("Fat Cat", 6)

# call our instance methods
print(kitty.description())
print(kitty.meow())

print(kitty.mood)

kitty.feed()

print(kitty.description())

print(kitty.mood)

kitty.sleep()

print(kitty.description())

kitty.meow()

kitty.name = 'Junaid'

## Modules

A Module is a python file that contains a collection of related definitions. Python has hundreds of standard modules. These are organized into what is known as the [Python Standard Library](http://docs.python.org/library/). You can also create and use your own modules. To use functionality from a module, you first have to import the entire module or parts of it into your namespace

To import the entire module:
`python import module_name`

You can also import a module using a specific name:
`python import module_name as new_module_name`

To import specific definitions (e.g. functions, variables, etc) from the module into your local namespace:
`from module_name import name1, name2`

import os
from glob import glob

To get the curent directory, you can use: `os.path.abspath(os.path.curdir)`

Let’s use glob, a pattern matching function, to list all of the ipynb files in the current folder.

data_file_list = glob(os.path.join(os.path.curdir,'*ipynb'))
print(data_file_list)

This gives us a list of the files including the relative path from the current directory. What if we wanted just the filenames? There are several different ways to do this. First, we can use the the os.path.basename function. We loop over every file, grab the base file name and then append it to a new list.

file_list = []
for f in data_file_list:
    file_list.append(os.path.basename(f))

print(file_list)

It is also sometimes even cleaner to do this as a list comprehension

[os.path.basename(x) for x in data_file_list]

### NumPy
NumPy is the fundamental package for scientific computing with Python.

import numpy as Junaid

NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called axes.

NumPy’s array class is called `ndarray`. It is also known by the alias `array`. The more important attributes of an ndarray object are:

- **ndarray.ndim**: the number of axes (dimensions) of the array.
- **ndarray.shape**: the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be `(n,m)`. The length of the `shape` tuple is therefore the number of axes, `ndim`.
- **ndarray.size**: the total number of elements of the array. This is equal to the product of the elements of `shape`.
- **ndarray.dtype**: an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.
- **ndarray.itemsize**: the size in bytes of each element of the array. For example, an array of elements of type `float64` has `itemsize` 8 (=64/8), while one of type `complex32` has `itemsize` 4 (=32/8). It is equivalent to `ndarray.dtype.itemsize`.
- **ndarray.data**: the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities. 

a = Junaid.arange(15) #array of numbers 0 to 14
a

a.dtype

print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))

#### Creating arrays
You can create an array from a regular Python list or tuple using the array function. The type of the resulting array is deduced from the type of the elements in the sequences.

A frequent error consists in calling array with multiple numeric arguments, rather than providing a single list of numbers as an argument.
```
a = np.array(1,2,3,4)    # WRONG
a = np.array([1,2,3,4])  # RIGHT
```

b = Junaid.array([6, 7, 8])
print(b)
print(type(b))

`array` transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on.

c = Junaid.array([(1.5, 2 ,3), (4, 5, 6), (7.1, 7.2, 7.3)])
print(c)
print()

print(c.shape)

The function `zeros` creates an array full of zeros, the function `ones` creates an array full of ones, the function `random.rand` creates an array of random floats from a uniform distribution over [0, 1], and the function `empty` creates an array whose initial content is random and depends on the state of the memory. By default, the dtype of the created array is `float64`.

Junaid.zeros((3,4))

import numpy as np

test = np.ones((2,3,4), dtype=np.int16)

np.random.rand(3,2)

np.empty((2,3)) # uninitialized, output may vary

To create sequences of numbers, NumPy provides a function analogous to `range` that returns arrays instead of lists.

np.arange( 10, 30, 5 ) # array from 10 to 30 in increments of 5

#### Shape Manipulation

Three main functions include:
- `ravel()` flattens an array
- `reshape()` changes the shape of arrays
- `transpose()` transposes the array

example = np.random.rand(4,4)
example

example*10

example_flat = example.ravel()  # returns the array, flattened
example_flat

example_flat.reshape(2,8) # returns the array with a modified shape 2x8

example_flat.reshape(4,4) # returns the array back to original shape

test = np.random.rand(2,3,6)

test

test.ravel()

example.transpose()

## "The Zen of Python"
*from [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython/blob/master/00-Introduction.ipynb)*

"Python aficionados are often quick to point out how "intuitive", "beautiful", or "fun" Python is. While I tend to agree, I also recognize that beauty, intuition, and fun often go hand in hand with familiarity, and so for those familiar with other languages such florid sentiments can come across as a bit smug. Nevertheless, I hope that if you give Python a chance, you'll see where such impressions might come from. And if you really want to dig into the programming philosophy that drives much of the coding practice of Python power-users, a nice little Easter egg exists in the Python interpreter: simply close your eyes, meditate for a few minutes, and `import this`"

import this

