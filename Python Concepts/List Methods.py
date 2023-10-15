mylist=[]

for i in range(10):
    mylist.append(i)

#index()-> This method returns index of speciifed elements
idx=mylist.index(4)
print(idx)

# index(element,start,end) method also takes 2 more parameters like
# start->index from which we start searching element
# end-> index till we can search that element
# if element not found it will raise an exception
lst=['cats','dogs','human','elephant','tigers','lions']
idx=lst.index('lions',2)
print(idx)

#append()-> This method adds an element to end of list
lst.append('zebra')
print(lst)

#extend()-> This method adds all the elements of an iterable(list,tuple,etc.) to the end of list
#this method modifies original list not return new list
lst1=['Cows','kangaroo']
lst.extend(lst1)
print(lst)

#insert(index,element)-> This method takes 2 parameters to add an element in a list
lst.insert(2,'panthers')
print(lst)

lst.insert(6,'dogs')
#remove()-> This method removes the first matching element which is passed as an argument to method from list
lst.remove('dogs')
print('list after deleting element:-\n',lst)

lst.append('tigers')
lst.append('tigers')

#count() -> This method returns the number of times the specified element appear
ct=lst.count('tigers')
print(f"The element tiger apperaed in list {ct} times.")

#pop(index)-> THis method removes an item at the specified index and return removed item.
ele=lst.pop(len(lst)-4)
print(f"Removed element at index {len(lst)-1} is {ele}.")

#if index is not passed to pop() method then it by default deletes last element in list.
ele=lst.pop()
print(ele)

#reverse()-> This method reverses an elements of list.
lst.reverse()
print(lst)

#sort(key=...,reverse=...)-> This method sorts an item of a list in an ascending or descending oreder.
lst.sort()
print(lst)

#copy() ->this method copies a list to another list
newlist=lst1.copy()
print(newlist)

#clear()-> This method removes all items from the list.
newlist.clear()
print(newlist)


#sorting the list containning dictionary
list=[]
n=int(input("Enter the number of elemnts"))
for i in range(n):
    mydict={}
    mydict['Name']=input("Enter movie name")
    mydict['Director']=input("Enter director name")
    mydict['Year']=input("Enter the year which movie was released")
    list.append(mydict)

sorted_list = sorted(list, key=lambda x: x['Year'])
print(sorted_list)