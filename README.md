# mspIIprojects
These are my CCA MSPII Projects.


# Input
age = input('How old are you?')
variable = input(request)

int() function - converts to integer
float() function - converts to floating point number (number with decimals)

# Project01 - The Interview
1) Ask at least three questions.
2) Store responses in variables with meaningful names ==> Use snake_case
3) After all questions have been asked and answered, print sumarry to user. Use string formatting ==> print(f'You are {age} years old')

# Range
range(min, max) - minimum is included, maximum is excluded

range(1,4) == 1,2,3

range(max) -- numbers from 0 to (max-1)

range(min, max, stepsize)

range(4,20,2)
4,6,8,10,12,14,16,18

# For loops

for i in x:
   do something

x must be an iterator!!

Iterator -- a set of objects that you can go through one at a time (iterate through)

i is a variable name, given to each object in x, as it is returned from x.

The for loop iterates through _x_, grabbing its objects one at a time, naming them _i_, and performing a task with _i_, until no objects are left to be iterated through.

for i in range(10):
....print(i)

YOU MUST HAVE A TAB (or 4 spaces)


# Lists

my_list = [1,2,3,4,5]
another_list = ['a','hello','budd','5']
blah_ist = [1,'he',4.5534,'thisthing',my_list]

0-based indexing!!

Slicing is the same as strings!!

+ concatenates/joins lists
* multiplies a list

.append() -- adds an item to the end of the list
b.append(11) adds 11 to the end of b

.extend()  -- adds the items from an iterable to the end of a list
b.extend(a) adds the items in a to the end of b

.insert() -- insert an item before an index
.insert(index,item)

.remove() -- removes an item from a list
a.remove('carrot') removes carrot from the list

.pop() -- removes last item in list, and returns it

.reverse() -- reverses the list

min() & max() -- returns minimum and maximum of list
min(a) returns the minimum value in the list
**key** argument: applies a function (key=function) to the list before finding the minimum & maximum

.count() counts the number of that object in the list

.index() -- returns the first index where that item appears in the list

.sort() -- sorts the list in alphanumerical order

.clear() -- clears the list of all contents

# Project_02 -- Shopping Cart
Make a 2-dimensional list of items & their prices--
items = [
  ['apple',4.99],
  ['banana',8.49]
]

Output to user --
Loop through items list, print out: "Would you like to buy a _____, it costs ______?"
If user responds 'yes', add the item to a new shopping list,
else, do nothing.

At the end, print out the user's shopping list and total cost.

Ask the user if they'd like to remove something, if they say yes, ask what item they want to remove, remove that object, and decrease the cost by the price of that object.

# Conditionals
**if conditions**:
if true:
    do this

== equal to

**else conditions**
Must follow an if conditional

if (a):
  do this
else:
  do this

**elif conditions**
(short for else if)

# while loops
while(true):
  do this

# Dictionaries
Stores values (information) that can be accessed with specific keys.
dictionary = {'key1': value1, 'key2': value2, ...}
access dictionary values by key:
dict['key1']
 output --- value1
Change values --
dict['key1'] = new_value
Add new key/value pairs
dict['key3'] = value3

Looping through dictionaries

for key, value in dictionary:
    print(key, value)

products = {'apple': 3, 'banana': 2, 'carrot': 4}

for name, cost in products.items():
    print(name, cost)

# Tuple
(1,2,3,4)
x, y = (10,-3)

# PROJECT 03: Math Calc
While loops & if/elif/else conditions & dictionaries
- Pick 2-3 real-world formulas
  - Example: F = m*a
- Ask user which formula they would like to solve/a solution for
- Ask user which variable they want to solve for (target)
- Ask user to input all other variables
- Solve the formula for the target variable
- Output solution to user

