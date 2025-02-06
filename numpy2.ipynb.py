#!/usr/bin/env python
# coding: utf-8

# In[15]:


#slicing
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
slice1=arr[2:6]
slice2=arr[::2]
Reversed=arr[::-1]
print(slice1)
print(slice2)
print(Reversed)


# In[20]:


#slicing multi dimensional array
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
#slice rows 0 to 2 column 1 to 3
subarray=arr[0:2,1:3]
print(subarray)


# In[21]:


#extra act first column
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
col=arr[:,0]
print(col)


# In[22]:


arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0,0])
print(arr[1,2])


# In[23]:


#basic indexing
arr=np.array([10,20,30,40,50])
print(arr[1])


# In[24]:


#negative indexing
arr=np.array([10,20,30,40,50])
print(arr[-1])


# In[25]:


#subset indexing
arr=np.array([10,20,30,40,50])
print(arr[1:4])


# In[33]:


#specfic condition for indexing
arr=np.array([10,20,30,40,50])
print(arr[arr>25])


# In[32]:


#horizontal join
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
result=np.hstack((arr1,arr2))
print(result)


# In[34]:


#vertical join
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
result=np.vstack((arr1,arr2))
print(result)


# In[35]:


#depth join
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
result=np.dstack((arr1,arr2))
print(result)


# In[44]:


#spilt into 3 equal parts
arr1=np.array([1,2,3,4,5,6])
result=np.split(arr1,3)
print(result)


# In[46]:


#spilt unequal parts
arr1=np.array([1,2,3,4,5])
result=np.array_split(arr1,3)
print(result)


# In[ ]:




