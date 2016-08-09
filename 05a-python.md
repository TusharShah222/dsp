# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists are what they seem - a list of values. Each one of them is numbered, starting from zero - the first one is numbered zero, the second 1, the third 2, etc. You can remove values from the list, and add new values to the end. Example: Your many cats' names.
Tuples are just like lists, but you can't change their values. The values that you give it first up, are the values that you are stuck with for the rest of the program. Again, each value is numbered starting from zero, for easy reference.

Tuples may work as keys in dictionaries, since there value doesnt change

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

A list keeps order, dict and set don't: when you care about order, therefore, you must use list (if your choice of containers is limited to these three, of course;-).

dict associates with each key a value, while list and set just contain values: very different use cases, obviously.

set requires items to be hashable, list doesn't: if you have non-hashable items, therefore, you cannot use set and must instead use list.

set forbids duplicates, list does not: also a crucial distinction. (A "multiset", which maps duplicates into a different count for items present more than once, can be found in collections.Counter -- you could build one as a dict, if for some weird reason you couldn't import collections, or, in pre-2.7 Python as a collections.defaultdict(int), using the items as keys and the associated value as the count).

Checking for membership of a value in a set (or dict, for keys) is blazingly fast (taking about a constant, short time), while in a list it takes time proportional to the list's length in the average and worst cases. So, if you have hashable items, don't care either way about order or duplicates, and want speedy membership checking, set is better than list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

lambda is just a fancy way of saying function. Other than its name, there is nothing obscure, intimidating or cryptic about it. When you read the following line, replace lambda by function in your mind:

>>> f = lambda x: x + 1
>>> f(3)
4

It just defines a function of x. Some other languages, like R, say it explicitly:

> f = function(x) { x + 1 }
> f(3)
4


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

squares = list(map(lambda x: x**2, range(10)))
or, equivalently:

squares = [x**2 for x in range(10)]
which is more concise and readable.

map(cube, range(1, 11))
is equivalent to

[cube(1), cube(2), ..., cube(10)]
While the list returned by

filter(f, range(2, 25))
is equivalent to result after running

result = []
for i in range(2, 25):
    if f(i):
        result.append(i)
Notice that when using map, the items in the result are values returned by the function cube.

In contrast, the values returned by f in filter(f, ...) are not the items in result. f(i) is only used to determine if the value i should be kept in result.

filter(), as its name suggests, filters the original iterable and retents the items that returns True for the function provided to filter().

map() on the other hand, apply the supplied function to each element of the iterable and return a list of results for each element.

Follows the example that you gave, let's compare them:

>>> def f(x): return x % 2 != 0 and x % 3 != 0
>>> range(11)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> map(f, range(11)) #the ones that returns TRUE are 1, 5 and 7
[False, True, False, False, False, True, False, True, False, False, False]
>>> filter(f, range(11)) #So, filter returns 1, 5 and 7
[1, 5, 7]

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 Days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 Days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```
7850 Days


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





