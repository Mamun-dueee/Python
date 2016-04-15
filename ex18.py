def print_two(*args): #def for defining function, *args is just like argv.
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)
    
def print_two_again(arg1, arg2): #this is another way to get argument.
    print "arg1: %r, arg2: %r" %(arg1, arg2)
    
def print_one(arg1):
    print "arg1: %r" %arg1
    
def print_none():
    print "I got nothing'."
    
print_two("Mamun", "Sumon")
print_two_again("Sumon", "Mamun")
print_one("First")
print_none()