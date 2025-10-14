# name = "prem"
# def another():
#   color = "blue"
#   greeting("Ladani",color) 
# # def greeting(firstname):
# def greeting(name,color):
#     # color = "blue"
#     print(color)
#     print(name)
    # print(firstname)

# greeting() 
# print(color)
# greeting("Deep patel")
name = "prem"
count = 1
# count += 1

def greeting(firstname, color):
    # override the provided color locally
    # nonlocal color
    color = "red"
    print(color)
    print(firstname)

def another():
  color = "blue"
  global count
  count += 1
  print(count)
  # error it when the call inside the function 
  #Traceback (most recent call last):
#   File "d:\prem\coding\code with python\scope.py", line 28, in <module>
#     another()
#     ~~~~~~~^^
#   File "d:\prem\coding\code with python\scope.py", line 25, in another
#     count += 1
#     ^^^^^
# UnboundLocalError: cannot access local variable 'count' where it is not associated with a value 
  greeting("Ladani", color)

another()