myset={'apple','banana','cherry'}

print("Set is ",myset)
#Set items are unchangeable, but you can remove items and add new items.
#Sets are unordered, so you cannot be sure in which order the items will appear.
#Set items are unordered, unchangeable, and do not allow duplicate values.

myset={'apple','banana','cherry','apple',True,1}
#True and 1 is considered the same value
print("Without duplicate valus set will be ",myset)

print('Length of set is',len(myset))

#add() -> This method to add an item to a set
myset.add('orange')
print("Set after adding new item will be",myset)

#To add values from another set to current set update() method is used.
tropical = {"pineapple", "mango", "papaya"}
myset.update(tropical)
print(f"Set After adding values from another set is {myset}")

lst=['Guava','coconut','mango']
#we can add any iterable to current set using update() method.
myset.update(lst)
print(myset)

#To remove an item in a set, use the remove(), or the discard() method.
myset.remove(True)
print(f"Set after removing a value {myset}")

# This main difference between remove() and discard() method is
# if the item to remove does not exist, discard() will NOT raise an error.
myset.discard(True)
# myset.remove(True) #This will give error as True is not in myset.
print(myset)

tempset={"pineapple", "mango"}
# we can also delete all items using clear() method.
#del set_name also deletes whole set.
tempset.clear() #this only removes all items from set.
print(tempset)
del tempset #this deletes the whole set.

#as sets are unindexed we can iterate them only by following way
for x in myset:
    print(x,end=" ")

#to join sets we have many method like union(),update(),intersection() and symmetric_difference()
#update() method->
set2={'Lichi','Strawberry'}
set2.update(myset)
print("\nAfter adding items from myset to set2",set2)

#---------------------------------------------------------------------------------------------------#
#set Methods->

#copy() -> This method copies set1 to set2
new_set=set2.copy()
print("New Set will be",new_set)

#difference() -> This method returns a set that contains the items that only exist in set x, and not in set y
x={'orange','cherry','pineapple'}
print("myset is-> \n",myset)
print("newly definde set x is->\n",x)
difference_set=myset.difference(x)
print("Difference of myset and x is->\n",difference_set)
#The returned set contains items that exist only in the first set, and not in both sets.

'''difference_update() -> this method works like difference() method but insetad of returning new set it
updates first set accodingly.
The difference_update() method removes the items that exist in both sets.
The difference_update() method is different from the difference() method, 
because the difference() method returns a new set, without the unwanted items
the difference_update() method removes the unwanted items from the original set.'''

# myset.difference_update(x)
# print(myset)

#intersection() -> This method Return a set that contains the items that exist in both set x, and set y.
newset=myset.intersection(x)
print(newset)

#similarly intersection_update() works it finds intersection of set1 and set2,update set1 accordingly.
# x.intersection_update(myset)
# print(x)

#isdisjoint() -> This method Return True if no items in set x is present in set y.
print("Is myset is a disjoint of x?\n",myset.isdisjoint(x))

#issubset() -> This mehthod return True if all items in set x are present in set y.
print("Is x is a subset of myset?\n",x.issubset(myset))

#issuperset() -> This check if set1 is superset of set2 means it return true if all elements in set2 has to be present in set1.
print("Is x is a subset of myset?\n",myset.issuperset(x))

#symmetric_difference()-> This method return a set that contains all items from both sets, except items that are present in both sets.
tempset=myset.symmetric_difference(x)
print(tempset)

#symmetric_difference_update() -> this method similarly as symmetric_difference() method but only difference is it updates set1 in place insted of returning new set
# myset.symmetric_difference_update(x)
# print(myset)

#union()-> this method return a set that contains all items from both sets, duplicates are excluded.
superset=myset.union(x)
print("The union set of myset and x is\n",superset)

