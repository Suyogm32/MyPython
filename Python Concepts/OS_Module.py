import os

print(os.getcwd())
# os.chdir("C:\Users\admin\AppData\Local\Programs\Python\Python311\python.exe")
# print(os.getcwd())
print(os.listdir())
#To create a directory
# os.mkdir("tryout folder")

#To create multiple directories
# os.makedirs("this/tryout")

#To renme the file
# os.rename("trythis.txt","Suyog info.txt")
# print(os.listdir())

#to get environment variables
# print(os.environ.get('Path'))

#
# os.path.join()

#This will check weather given path exsisits or not
print(os.path.exists("C://"))

#To check a file by giving it's path we use
print(os.path.isfile("D:\python\OS_Module.py "))
print(os.path.isdir("D:\python "))