#list comphersion
#example suppose we want a list of numbers divisible by 3
#one way be as follows
ls=[]
for i in range(100):
    if i%3==0:
        ls.append(i)

print(ls)

#but another one linear way to do that is
ls1=[i for i in range(100) if i%3==0]
print(ls1)

#dictionary compheresions
dict1={ i:f"item {i}" for i in range(40) if i%5==0}
print(dict1)

dict2={value:key for key,value in dict1.items()}
print(dict2)

r=int(input("Enter upto how much you want to generate:-"))
print("Please selct compherension that you want:-")
print("1)List compherension\n2)dictionary compherension\n3)set compherension")
ch=int(input("Enter your choice:-"))
if ch==1:
    ls=[i for i in range(r)]
    print(ls)
elif ch==2:
    dict={i:f" item {i}" for i in range(r)}
    print(dict)
else:
    set1={i for i in range(r)}
    print(set1)