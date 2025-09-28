import re

txt = "This is a Ladani Prem"
# x = re.search("^This.*Prem$", txt)
# x = re.findall("Prem", txt)
# x = re.split("\s", txt)
x = re.sub("\s","9", txt)
print(x)

