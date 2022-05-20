#!/usr/bin/python
import re
 
line = "	)SalesmanReserve5] [nvarchar](40) NULL,"
 
str1 = line.strip()
print(str1)
print(str1.startswith(')'))
print(re.findall(r'\[.*?\]', str1))

# if matchObj:
#    print("matchObj.group() : ", matchObj.group())
#    print("matchObj.group(1) : ", matchObj.group(1))
#    print("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print "No match!!"