mylist = []
mylist.append('hero')
print(mylist)
mylist.remove('hero')
print(mylist)
# =======================


mylist2 = list()
mylist2 = ['cherry', 'apple', 'bannana']
mylist3 = sorted(mylist2)
print(mylist3)
list4 = list(range(0, 10))
list5 = list4.copy()
list5.append('end ')
print(list5)
print([4*i for i in list5])
tups = (1, 2, 3)
print(type(tups))
print(tups[0])
for i in tups:
    print(i)
print(len(tups))

mydict = {1, 2, 3, 4}
odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}



print(odds.intersection(prime))
