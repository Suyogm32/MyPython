import numpy as np

my_2d_array=np.array([[1,2],[3,4],[5,6]])

print(my_2d_array)

new2d_Array=np.insert(my_2d_array,2,[[7,8,9]],axis=1)
print("2d array after adding new element is\n",new2d_Array)

new2d_Array=np.append(new2d_Array,[[10,11,12]],axis=0)
print("2d array after adding new element is\n",new2d_Array)

new2d_Array=np.delete(new2d_Array,1,axis=1)
print("2d array after deleting 2nd coloumn \n",new2d_Array)