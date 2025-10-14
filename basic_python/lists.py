users = ['prem','jeel','het']

data = ['prem',21,True]

emptylist = []

print("prem" in emptylist)

print(users[0])
print(users[-1])

print(users.index('prem'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Dev')
print(users)

users += ['jamin']
print(users)

users.extend(['ketan','Henna'])
print(users)

# users.extend(data)
# print(users)

users.insert(0,'tapan')
print(users)

users[2:2] = ['denial park','jack kim']
print(users)

users[1:3] = ['pkp','jpg']
print(users)

users.remove('jeel')
print(users)

print(users.pop())
print(users)

del users [0]
print(users)

# del data 
data.clear()
print(data)

users[1:2] = ['deva']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,43,56,1,78]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums,reverse=True))
print(nums)
 
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))
mylist = list([1,"Neel",True])
print(mylist)

#tuples 

mytuple = tuple(("dax",42,True))

anothertuple = (1,4,2,6,4,4)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one,*two,hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(4))

