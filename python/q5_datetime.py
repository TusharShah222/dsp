# Hint:  use Google to find python function

####a) 
#date_start = '01-02-2013'  
#date_stop = '07-28-2015'   

import time
import datetime

stringDate1 = "01, 02, 2013"
stringDate2 = "07, 28, 2015"
dateObject1 = datetime.datetime.strptime(stringDate1, "%m, %d, %Y")
dateObject2 = datetime.datetime.strptime(stringDate2, "%m, %d, %Y")
deltadate = dateObject2 - dateObject1
print deltadate

####b)  
#date_start = '12312013'  
#date_stop = '05282015'  

import time
import datetime


stringDate1 = "12312013"
stringDate2 = "05282015"

dateObject1 = datetime.datetime.strptime(stringDate1, "%m%d%Y")
dateObject2 = datetime.datetime.strptime(stringDate2, "%m%d%Y")
deltadate = dateObject2 - dateObject1
print deltadate


####c)  
#date_start = '15-Jan-1994'  
#date_stop = '14-Jul-2015'

import time
import datetime


stringDate1 = "15-Jan-1994"
stringDate2 = "14-Jul-2015"

dateObject1 = datetime.datetime.strptime(stringDate1, "%d-%b-%Y")
dateObject2 = datetime.datetime.strptime(stringDate2, "%d-%b-%Y")
deltadate = dateObject2 - dateObject1
print deltadate  
