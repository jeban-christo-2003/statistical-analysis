#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from sklearn.impute import KNNImputer

X = np.array([[1, 2, np.nan], [3, np.nan, 4], [np.nan, 5, 6]])

k = 2
imputer = KNNImputer(n_neighbors=k)

X_imputed = imputer.fit_transform(X)

X


# In[4]:


X_imputed


# In[ ]:




