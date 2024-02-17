#!/usr/bin/env python
# coding: utf-8

# In[3]:


from scipy.stats import f_oneway

# Example dataset (exam scores for three classes)
class_a_scores = [85, 90, 88, 92, 86]
class_b_scores = [80, 82, 85, 88, 81]
class_c_scores = [78, 75, 80, 79, 83]

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(class_a_scores, class_b_scores, class_c_scores)

print("F-statistic:", f_statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference in the mean exam scores between the three classes.")
else:
    print("There is no significant difference in the mean exam scores between the three classes.")


# In[4]:


from scipy.stats import chi2_contingency

# Example dataset (results of a transportation survey)
survey_data = [[30, 20, 50], [25, 35, 40]]  # Rows: Car, Bus, Bike / Columns: Male, Female

# Perform Chi-Square test
chi2_statistic, p_value, dof, expected = chi2_contingency(survey_data)

print("Chi-Square Statistic:", chi2_statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("There is a significant association between gender and preferred mode of transportation.")
else:
    print("There is no significant association between gender and preferred mode of transportation.")


# In[5]:


dof


# In[6]:


p_value


# In[10]:


p_value=round((p_value),2)


# In[11]:


if p_value>0.06:
    print("yes")
else:
    print("no")

