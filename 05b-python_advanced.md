## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

import pandas as pd
import re

df = pd.read_csv("faculty.csv")

degr = df[" degree"]

deg=degr.replace('\.','',regex=True).astype("string")

"""

dfz=degr.replace('\*','',regex=True).astype(float)

breakout = deg.groupby('a').count()

Nodecimals = degr[' degree'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')

"""

"""

print deg.count(sort)

"""
print deg.value_counts(sort = True)



####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> import pandas as pd
>> import re

>> df = pd.read_csv("faculty.csv")


>> #degr = df[" degree"]

>> #deg=degr.replace('\.','',regex=True).astype("string")


>> #print deg.count(sort)
>> #print deg.value_counts(sort = True)

>> #Titles
>> tits = df[' title']

>> print tits.value_counts(sort = True)



####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.
>> import pandas as pd
>> import re

>> df = pd.read_csv("faculty.csv")


>> #degr = df[" degree"]

>> #deg=degr.replace('\.','',regex=True).astype("string")


>> #print deg.count(sort)
>> #print deg.value_counts(sort = True)

>> #Titles
>> tits = df[' email']

>> print tits.value_counts(sort = True)


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> import pandas as pd
>> import re

>> df = pd.read_csv("faculty.csv")
>> emailz = list(df[" email"])

>> dom = emailz


>> print dom




>> domain = re.search("@[\w.]+", emailz)
>> #print domain.group(" email")
>> print emailz.value_counts(sort = True)

>> Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

>> import pandas as pd
>> import re


>> df = pd.read_csv("faculty.csv")

>> s = df
>> snail = df[" email"]
>> #print snail[0]



>> snail_d = re.search("@[\w.]+", snail[0])

>> #snail_d.group()
>> print snail 
>> #domain = re.search("@*", "snail")
>> #print df
>> #domain = re.search('@', df, 1)
>> #print df[" email"]
>> #snail = df[" email"]

>> #print snail_d
>> print snail_d.group(0)




---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}



for i in faculty_dict:
    print i, faculty_dict[i]







####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:



professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],
                  ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],
                  ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
                  ('Mingyao', 'Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
                  ('Hongzhe', 'Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']};



print professoror_dict


####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

import pprint
from collections import OrderedDict

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],
                  ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],
                  ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
                  ('Mingyao', 'Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
                  ('Hongzhe', 'Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']};


#Sort using lambdas
print "******"
print "*********** SORTING USING LASTNAME*************"
print "******"
sort_by_lastname = sorted(professor_dict.items(), key=lambda item: item[0][1])
pp.pprint(sort_by_lastname)

#Preserve order and "dictionize"
print "******"
print "*********** SORTING THAN DICT USING LASTNAME*************"
print "******"
dict_by_lastname = OrderedDict(sorted(professor_dict.items(), key=lambda item: item[0][1]))
pp.pprint(dict_by_lastname)





>> REPLACE THIS WITH YOUR RESPONSE

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

