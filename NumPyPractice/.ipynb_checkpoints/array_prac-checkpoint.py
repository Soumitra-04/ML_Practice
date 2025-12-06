import numpy as np   #importing the standard library numpy
#create an empty array of size 10, and reshape them in 1 block , 2 dimensions and 5 numbers in one row  
x = np.empty((10),dtype = np.int32).reshape(1,2,5)  

print(x)
print(x.ndim)               #printing the dimensions of x
print(x.shape)              #print the shape of x that is 1,2,5
print(x.size)               #prints the size of the array , here 10
print(x.dtype.itemsize)     #prints the size of each itemtype in the array... here the datatype is 32 bit integer, so size will be 32 bits

z = np.linspace(0, 2, 9)                   # 9 numbers from 0 to 2
print(z)
y = np.linspace(2,11,10,dtype = np.int64) #create an array with 10 elements from 2 to 11 and the datatype is a 64 bit integer
print(y)
a = np.array([[10,20],          #2 blocks are required so we won't get an error
             [20,30]])
print(a)
x = np.linspace(0, 2 * np.pi, 2)        #useful to evaluate function at lots of points
print("x = \n", x)
f = np.sin(x)               #calculate the sine of each element and make an array of those values  
# print(f) 
b = np.arange(20).reshape(5,4) #create an array b that ranges from 0 to 20 , and make it's shape of 5 rows and 4 columns
print(b) 
print(b ** 2) #calculate the power of each element and display the array
rg = np.random.default_rng(1)  # create instance of default random number generator
a = np.ones((3, 3), dtype=int) #create a  3 X 3 array filled with 1
a *= 3
print("a is: \n",a,a.ndim,"\n")
b = rg.random((3, 3)) #creates a 3 by 3 array filled with random numbers 
print("b is: \n",b,b.ndim,"\n")
# print("a + b is : \n",b + a,"\n")
# print("A dot B is: \n", a.dot(b),"\n")
c = a + b
# print("\n",c,np.dtype.name)
d = np.exp(c * 1j)
# print("\n",d,np.dtype.name)
print(a.min())
print(a.sum())
a = np.arange(10) ** 3 #creates an array from 0 to 9 with each element cubed
print("a is: \n",a)
print("a[2] is: \n",a[2])
print("a[2:5] is: \n",a[2:5]) #slices the array from 3rd to 5th element, i.e 3,4,5
b = np.fromfunction(lambda x,y: 10 * x + y, (5, 4), dtype=int)
print("b is : \n",b)
print("\nb[2,:] is : \n",b[2, :])