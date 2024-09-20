# Remove Empty Tuples
list1 = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), 
         ('krishna', 'akbar', '45'), ('', ''), ()]
list1 = [t for t in list1 if t]
print(list1)
