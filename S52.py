# Ex 1. Ordonarea unui dictionar

D = {'a': 1, 'c': 3, 'b': 2}
keys = list(D.keys())
print(keys)
keys.sort()
print(keys)
for key in keys:
    print(key, '=>', D[key])

''' range () '''
'''
The built-in range function produces a series of successively higher integers, which can be used as indexes in a for.
Because for loops typically run quicker than while-based counter loops, it’s to your advantage to use tools like these
that allow you to use for when possible.
'''
'''
With one argument, range generates a list of integers from zero up to but not including the argument’s value.
If you pass in two arguments, the first is taken as the lower bound.
An optional third argument can give a step; if it is used, Python adds the step to each successive integer in the result(the
step defaults to 1).
'''
print(range(5)) # De la 0 până la acel număr fără acel număr 
print(list(range(5)))
print(list(range(1, 5)))
print(list(range(1, 100, 5)))  # we use list to print the actual numbers in the sequence

for i in range(3):
    print(i, 'sheep')

'''Functions'''
'''
Functions are the most basic program structure Python provides for maximizing code reuse and minimizing code redundancy.
'''

'''
The def statement creates a function object and assigns it to a name. Its general format is as follows:

def <name> (arg1, arg2, arg3 ... ): 
    #function body
    
After the def has run, you can call (run) the function in your program by adding
parentheses after the function’s name. The parentheses may optionally contain one or
more object arguments, to be passed (assigned) to the names

'''


def suma(a, b):
    return a + b


print(suma(3, 5))


# Individual exercise 1:

# Print all the prime numbers from 1 to 100. Define is_prime function()

def is_prime(n):
    return True


for number in range(1, 101):
    if (is_prime(number)):
        print(number, end=" ")

'''LAMBDA FUNCTIONS'''

''' 
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

lambda arguments : expression

'''

X = lambda a: a + 10
print(X(10))
y = lambda a, b: a * b
print(y(2, 3))

'''Why use lambda functions? '''

'''The power of lamda is better shown when you use them as an anonymus function inside other functions '''

'''Example :
 
Say you have a function defintion that takes one argument, and that argument will be multipllied with an unkown number. 
Use that function definition to make a function that always doubles the number: 
'''


def myfunc(n):
    return lambda a: a * n


doubler = myfunc(2)

print(doubler(11))

'''Use the same function defintion to make a function that always triples the number you send in: '''

tripler = myfunc(3)

print(tripler(22))

'''Lambda function can also be used as parameters for other functions: '''

my_list = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x ** 2, my_list))  # map() function applies given function to each element of the list
print(result)

my_list = [2, 4, 6, 8, 9, 10, 11, 12, 14]
result = list(
    filter(lambda x: x % 2 == 0, my_list))  # filter function creates a list of element for which the function is True
print(result)



'' 'Working with files '''


'''You must open the file using Python's built-in open() function. 
This function requires the path to the file and the mode as arguments and returns a file object.'''

# Open a file for reading ('r')
file = open('example.txt', 'r')

# Open a file for writing ('w')
file = open('example.txt', 'w')

# Open a file for appending ('a')
file = open('example.txt', 'a')

# Open a file for both reading and writing ('r+')
file = open('example.txt', 'r+')

'''
Once a file is opened in reading mode, you can use methods like .read(), .readline(), or .readlines() to read its content.

'''

# Read the entire content of the file
file = open('example_2.txt', 'r')
content = file.read()
print(content)

# Read one line at a time
line = file.readline()
print(line)

# Read all lines into a list
lines = file.readlines()
print(lines)

file.close()


'''To write to a file, open it in writing ('w') or appending ('a') mode. Then use the .write() or .writelines() method.'''

# Write a string to a file
file = open('example.txt', 'w')
file.write('Hello, world!\n')

# Write multiple lines at once
lines = ['First line\n', 'Second line\n']
file.writelines(lines)

#It's important to close a file when you're done with it to free up system resources.

file.close()


'''A better practice is to use the with statement when dealing with file objects. 
It ensures that the file is properly closed after its suite finishes, even if an exception is raised.
'''

# Reading using 'with'
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing using 'with'
with open('example.txt', 'w') as file:
    file.write('Goodbye, world!\n')

with open('example_3.txt', 'w') as file:
    file.write('Hello, Python!\n')
    file.write('File handling is easy.')

with open('example_3.txt', 'r') as file:
    content = file.read()
    print(content)


''' Reading data from csv files '''

''' Before you can read a CSV file, you need to import Python's built-in csv module. '''

import csv

'''use the with statement so that the file is properly closed after its suite finishes.'''

with open('angajati1.csv', mode='r') as file:
    # Reading operations go here
    # Use the csv.reader() function to create a reader object which will iterate over lines in the given CSV file.
    reader = csv.reader(file)
    # The reader object is iterable.
    # You can loop over it to retrieve each row of the CSV file. Each row is returned as a list of strings.
    for row in reader:
        print(row)


'''
If your CSV file has headers (i.e., the first row contains column names), you can use csv.DictReader instead. 
This will read each row as a dictionary, where the keys correspond to the headers.'''

import csv

with open('angajati.txt', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Access columns by names instead of position
        print(row['Nume'])




