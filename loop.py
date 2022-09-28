# #stop writing loops weirdly


# #How we are thought to loop

# #This type of look work on almost all languages

# #Give i an itial value of 0
# i = 0

# #Create a list it could be number strings etc...
# my_list = range(10)

# #loop trough your list while the length of your list is greateer thab your initial value
# while i < len(my_list):
#     #get the individual value in your list
#     v = my_list[i]
#     #print the value
#     print(v)
#     #increment your initial value
#     i += 1


# #But in python you can do it differently

# for i in range(len(my_list)):
#     v = my_list[i]
#     print(v)


# #Both of these waays to loop are complicated because you have the len(my_list) that you have to know

# #so the easier way in python is to just loop through the list

# for v in my_list:
#     print(v)


########## What is a for loop ############

'''
for name in iterable:
    statements

iterable produce a stream of values

assign stream values to name

Execute statements once for each value in iterable

--------> iterable decides what values it produces <------------

List produces elements

for e in [1,2,3,4]:
    print(e)

1
2
3
4

Strings prodces characters

for c in "Hello":
    print(c)

H
e
l
l
o

Dictionary-- Dicts  produces keys
d = {'a':1,'b':2,'c':3}
for keys in d:
    print(keys)
* dictionary don't have indeces so the order is going to be random
a
c
b

Also...
for v in d.itervalues()#This dictionary built in function/method returns only the values
for k,v in d.iteritems()#and this returns both the keys and the values


Files produces lines

with open('file.txt') as file:
    for line in file:
        print(line)


stdlib iterables

for match on re.finditer(pattern,string):
    # once for each regex match

for root, dirs, files in os.walk('/some/dir):
    # once for each sub-directory


for num in itertools.count():
    # once for each integer.. infinite!


#cool trick with itertools 

from itertools import chain, repeat, cycle
seq = chain(repeat(17,3),cycle(range(4)))

for num in seq:
    print(num)
    #this will run froever


#other uses for iterables
new_list = list(iterable)

results = [f(x) for x in iterable]

total = sum(iterable)
smallest = min(iterable)
largest = max(iterable)

combined = "".join(iterable)

'''

#How do i get the index if i simplify my list too much?

'''
you would probalby want to use this function in order to get the index value

NO!!!!

for i in range(len(my_list)):
    v = my_list[i]
    print(i,v)


YES !!!!! 

for i,v in enumerate(my_list):
    prrint(i,v)

enumerate works also for iteration that don't have indexing such as reading a file

when reading a file there is no way of telling the loop to go at line 100
the file has to be read one line at a time starting from the begening of the file 
to the end.

Enumerate does it for us

'''

#How do I loop over two lists or more?
'''

NO!!!!!!

names =['jhon','sarah','gigi']
ages = [1,2,3]

for i in range(len(names)):
    name = names[i]
    age = ages[i]
    print(f"{name} is {age} years old")


YES!!!!!!

for name, age in zip(names,ages):
    print(f"{name} is {age} years old")

ANOTHER YES!!!!

dict(zip(names,ages))

result = {'jhon': 1, 'sarah': 2, 'gigi': 3}


print(f"The oldest person on the list is: {max(result.values())} years old")

print(f"The oldest person's name and age is: {max(result.items(),key=lambda b:b[1])}")

print(f"The oldest person's name is: {results,key=result.get}")


'''


###### Customizing iteration ################


'''
nums = [1,2,3]

NOO!!!!!

def evens(stream):
    them = [] 
    for n in stream:
        if n% 2 ==0:
            them.append(x)

    return them


for n in evens(nums):
    do_something(n)

YESSS !!

def evens(stream):
    for n in stream:
        if n % 2 ==0:
            yield n
# it appends and returns the value that it appended

for n in evens(nums):
    do_something(n)

def hello_world():
    yield "hello"
    yield "world"

for x in hello_world():
    print x

hello
world
'''

###abstracting your iteration###

'''
f = open('text.txt')
for line in f:
    line = line.strip()

    if line.startswith('#'):

         continue

    if not line:
        continue

    do_something(line)


create a generator instead

def interseting(f):
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        if not line:
            continue

        yield line
        
and now you can do this 

with open('text.txt') as f:
    for line in interseting(f):
        do_something(line)

with open('changed_text.dat') as f:
    for line in interseting(f):
        do_something(line)

'''


#How do you break out of 2 loops


'''
NOOOOOOOOOOOOOOOOOOOOO

for row in range(height):
    for col in range(width):

        value = spreadsheeet.get_value(col,row):
        do_something(value)

        if this_is_my_value(value):
            break


YESSSSSSSSSSSSSSSSSSSSSS

def range_2d(width,height):
    """Produce a stream of two_d coordinates."""
    for yn in range(height):
        for x in range(width):
            yield x,y


for col,row in range_2d(width,height):
    value = spreadsheeet.get_value(col,row):
    do_something(value)

    if this_is_my_value(value):
        break



for cell in spreadsheet.cells():
    value = cell.get_value()
    do_something(value)

 
    if this_is_my_value(value):
        break   
    

'''



###### Low level iteration ######

'''

iterable produces iterator

iterator produces stream of values


iterator = iter(iterable) #iterable.__iter_()
value = next(iterator) #iterator.next() ot .__next__()
value = next(iterator)


book full of pages is iterable and a bookmark is an iterator.
** you can have 2 bookmarks in the same book


example

with open("blah.txt") as f:
    #read the first line
    header_line = next(f)

    #read the rest
    for data_line in f:
        #....

'''


###### Making your object iterable #####

'''
class ToDoList(object):
    def __init__(self) -> None:
        self.tasks = []

    #use the iter function on a list of data that your function has
    #dunder iter method need to be created if you want to make your object iterable
    def __iter__(self):
        return iter(self.tasks)

todo = ToDoList()

for task in todo:
    #......



Lets make it even better


class ToDoList(object):
    def __init__(self) -> None:
        self.tasks = []

    def __iter__(self):
        #only if the task is not done we will return/yield it
        for task in self.tasks:
            if not task.done:
                yield task

    #gives is all task
    def all(self):
        return iter(self.tasks)

    #generator expresion will do evrything the __iter__ is doing
    def done(self):
        return (t for ti in self.tasks if t.done)

    
'''