def hello_world():
    print("Hello prem")

hello_world()

def sum(num1=0,num2=0):
    # print(num1+num2)
    if(type(num1) is not int or type(num2) is not int ):
        return 0
    return num1+num2

# total = sum(2,3)
# total = sum("a",3)
# total = sum(1,2)
# total = sum()
total = sum(7,2)
print(total)

# sum(2,3)
# sum(1,7)
# sum(100,3)

def multiple_items(*args): #their represented the tuple
    print(args)
    print(type(args))

multiple_items("prem","jeel","deep")

def mult_named_items(**kwargs): #their represented as the dictionary
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "prem",last="ladani")

