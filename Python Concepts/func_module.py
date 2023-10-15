import sys

# out=open("target.txt",'w')
# print("Hello world",file=out)

# import random
# print(dir(random))
#
# a=1
# b=2
# c=3
# a,b,c=b,c,a #2 3 1
# print(a,b,c)
#
# import glob
# print("All python files are ",glob.glob("*.py"))

fo = open("target.txt")
print(fo.tell())
line = fo.readline()
print(fo.tell())
print(line)
pos = fo.tell()
print("Current Position: "+str(pos))
fo.close()