#!/usr/bin/env python
# coding: utf-8

# In[38]:


from scipy import stats
import numpy as np


# In[39]:


test_group=[850,900,880,920,860]
control_group=[80,88,18,28,81]


# In[41]:


t_stat,p_value=stats.ttest_ind(test_group,control_group)


# In[58]:


t_stat


# In[50]:


p_value


# In[51]:


a=0.05
if p_value<a:
    print("The test group is significantly bettter")
else:
    print("there is no significantly better")


# In[66]:


import statsmodels.api as sm
import numpy as np

control_group = np.array([85, 90, 95, 100, 105,121,122,123,134,145,123,321,234,124,231,211,134,155,133,144,153,231,234,123,221,231,143,145,155,165,177,231])
test_group = np.array([75, 80, 85, 90, 95,110,100,210,220,230,225,345,431,123,233,43,122,33,442,122,233,321,132,145,133,143,155,165,231,321,222,223])

z_statistic, p_value = sm.stats.ztest(test_group, control_group)
print("Z-statistic:", z_statistic)
print("P-value (Z-test):", p_value)

alpha = 0.05
print(f"significant value :{alpha}")


if p_value < alpha:
    print("Reject the null hypothesis (Z-test)")
else:
    print("Accept the alternate hypothesis the null hypothesis (Z-test)")


# In[70]:


import scipy.stats as stats
import numpy as np

# Example data
group1 = np.array([85, 90, 95, 100, 105])
group2 = np.array([75, 80, 85, 90, 95])
group3 = np.array([65, 70, 75, 80, 85])

# Perform F-test
f_statistic, p_value = stats.f_oneway(group1, group2, group3)
print("F-statistic:", f_statistic)
print("P-value (F-test):", p_value)

# Significance level
alpha = 0.05
print(f"significant value is: {alpha}")

# Check if p-value is less than alpha
if p_value < alpha:
    print("Reject the null hypothesis (F-test)")
else:
    print("Fail to reject the null hypothesis (F-test)")


# In[68]:


import scipy.stats as stats
import numpy as np

# Example data
observed = np.array([[10, 20, 30], [15, 15, 25]])

chi2_statistic, p_value, dof, expected = stats.chi2_contingency(observed)
print("Chi-square statistic:", chi2_statistic)
print("P-value (Chi-square test):", p_value)

# Significance level
alpha = 0.05

# Check if p-value is less than alpha
if p_value < alpha:
    print("Reject the null hypothesis (Chi-square test)")
else:
    print("Fail to reject the null hypothesis (Chi-square test)")


# In[55]:


print(f"chi2_statistic   {chi2_statistic}")
print(f"degrees of freedom  {dof}")
print(f"probability value  {p_value}")


# In[67]:


#From the above test we can conclude the relation of the columns or the difference of columns
#according to the test the relation or the differnece is decided
#above is sample data from which can analyze the significant difference or significant realtion through the statistical test

