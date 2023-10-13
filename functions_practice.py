def hello():
    print("Welcome User!")
    return

def pack(arg1,arg2,arg3):
    inp=[arg1,arg2,arg3]
    print(inp)
def eat_lunch(*args):
    if len(args) != 0:
        print("First I eat: ", args[0])
        for i in range(len(args)-1):
            print("Then I eat: ", args[i+1])
    else:
        print("My lunchbox is empty!")
print() 
hello()
print()
pack("one", "one", "one")
print()
eat_lunch("one","two","three","four","five")