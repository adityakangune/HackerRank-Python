'''
Python any() function accepts iterable (list, tuple, dictionary etc.)
as an argument and return true if any of the element in iterable is true,
 else it returns false. If iterable is empty then any() method returns false
'''
s = input()
print( any( i.isalnum() for i in s))
print( any( i.isalpha() for i in s))
print( any( i.isdigit() for i in s))
print( any( i.islower() for i in s))
print( any( i.isupper() for i in s))
