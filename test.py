#arn = "arn:aws:iam::123456789012:user/johndoe"
#print(arn.split("/")[1])

#str1 = "ugander"
#str2 = "raj"
#result = str1 + " " + str2
#print(result)

#x = lambda a : a + 10
#print(x(5))

#x = 5 > 3 and 4 > 6 and 10 > 9
#print(x)

import re
txt = "The rain in Spain"
x = re.match("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")