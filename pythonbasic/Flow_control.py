greetings ='Morning'
if greetings == 'Good Morning':
    print('Condition matches')
else:
    print('Condition not match')


# How for loops work in python and importance of code indentation
Bangalore = ['majestic', 'coxtown', 'MG ROad', 'Indira Nagar','Brigade road']
for b in Bangalore:
    print(b)

# How while loop works in python.
a = 10
while a >1:
    if a == 9:
        a = a -1
        continue # it will skip the current iteration
    if a == 3:
        break # it will break the loop and come out of the loop.
    print(a)
    a = a-1
print('While loop execution is done')

