mydict={'key':'val','Key1':'val1','Key2':'val2'}

#copy()-> THis method copies a dictionary to another dictionary
dict2=mydict.copy()
print(dict2)

#clear()-> This method removes all key,values from dictionary.
dict2.clear()
print("Dict2 is ",dict2)

#fromkeys()-> This method creates a dictionary from given sequence of keys and values.
alpha=['a','b','c']
nums=[1,2,3]
dict2=dict2.fromkeys(alpha,nums)
print('dict2 is now like ->\n',dict2)

#get() -> This method returns a value for the specified key in dictionary.
val=mydict.get('Key1')
print(f"Key1:{val}")

#items() -> This method returns a view object that display a list of dictionary key,value pairs.
pairs=mydict.items()
print(pairs)

#keys()-> This methos extract the keys of dictionary and return the list of keys as view object.
dictkeys=dict2.keys()
print("Key's in dict2 are \n",dictkeys)

#popitem() ->This method removes and returns the last element pair inserted into dictionary.
item=dict2.popitem()
print("Last inserted key,value pair is ",item)

#setdefault()-> This method returns a value of a key if key found in dictionary.
#If not found then it inserts a key with a value to the dictionary
mydict.setdefault('Key3','defval')
print(mydict)

#pop() -> This method removes and return an element from dictionary having given key.
rem_item=mydict.pop('Key2')
print("Removed item is",rem_item)

#values() -> Thi method returns a view object that displays list of all values in dictionary.
all_vals=mydict.values()
print(all_vals)

# print(mydict.__eq__())

a=1
b=2
a,b=b,a
print(a,b)

#Tuple methods

#count() -> This method returns the number of times the specific element appears in the tuple.
vowels=('a','e','i','e','o','e','u','e')
print(f"The letter e came in tuple of {vowels.count('e')} times")

#index()-> This method retuyrns the index od specified element.
print(f"The index of letter i is {vowels.index('i')}")