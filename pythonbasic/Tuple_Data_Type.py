a= (1,2,3,4)
print(a) # prints the whole tuple

# Tuple holding multiple type of data
b = ('Hello',1,2,3,'Go')
print(b) # prints the whole tuple
print(b[0])

# Tuple supports read only operation.

#['Hey','you',1,2,3,'Go']

t = ('hello','you',1,2,3,'Go')
print(t) # complete
print(t[0]) # single value
print(t[-1])
print(t[2:5])
#t.insert(2,'Karthik') # attribute Error. Insertion is not supported.
#t.append('end') # Attribute Error. Values cannot be added to the last of the tuple
t[2]='Karthik Babu' # object does not support item assignment


# In Tuple data type what are the operations unsupported.
# 1.  insert a value is unsupported
# 2. append a value to the end of the Tuple is unsupported
# 3. update a new value in the tuple is unsupported.





