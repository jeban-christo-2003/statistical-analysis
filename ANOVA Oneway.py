#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, f_oneway
from scipy import stats

# Define parameters
num_patients_per_medication = 30
num_medications = 4

# Generate synthetic data for one-way ANOVA
np.random.seed(42)  # for reproducibility
age = np.random.randint(18, 80, size=num_patients_per_medication * num_medications)
gender = np.random.choice(['Male', 'Female'], size=num_patients_per_medication * num_medications)
medication = np.repeat(np.arange(num_medications), num_patients_per_medication)
blood_pressure = np.random.normal(loc=120, scale=5, size=num_patients_per_medication * num_medications)

# Generate synthetic names with corresponding gender
def generate_names(num_names, genders):
    male_first_names = ['John', 'Michael', 'William', 'David', 'Robert']
    female_first_names = ['Emily', 'Olivia', 'Samantha', 'Emma', 'Jane']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown']
    names = []
    for gender in genders:
        if gender == 'Male':
            first_name = np.random.choice(male_first_names)
        else:
            first_name = np.random.choice(female_first_names)
        last_name = np.random.choice(last_names)
        full_name = first_name + ' ' + last_name
        names.append(full_name)
    return names

names = generate_names(num_patients_per_medication * num_medications, gender)

# Create DataFrame for one-way ANOVA data
one_way_data = pd.DataFrame({
    'Name': names,
    'Age': age,
    'Gender': gender,
    'Medication': medication,
    'BloodPressure': blood_pressure
})

# Convert DataFrame to CSV
one_way_data.to_csv('Blood Pressure.csv', index=False)

print("CSV file generated successfully.")


# In[21]:


df1=pd.read_csv("Blood Pressure.csv")
df1.head()


# In[23]:


df1.describe(include='all')


# In[26]:


df1.nunique()


# 
# # 2. Univariate Analysis
# # Histogram of Age

# In[29]:



# 2. Univariate Analysis
# Histogram of Age
plt.figure(figsize=(8, 6))
sns.histplot(df1['Age'], bins=20, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[40]:


skewness = stats.skew(df1['BloodPressure'])
kurtosis = stats.kurtosis(df1['BloodPressure'])
print("\nSkewness:", skewness)
print("Kurtosis:", kurtosis)


# In[41]:


shapiro_test = stats.shapiro(df1['BloodPressure'])
print("\nShapiro-Wilk Test for Normality:")
print("Test Statistic:", shapiro_test.statistic)
print("p-value:", shapiro_test.pvalue)


# In[43]:


# QQ plot for normality
plt.figure(figsize=(8, 6))
stats.probplot(df1['BloodPressure'], dist="norm", plot=plt)
plt.title('Q-Q Plot')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.show()


# In[44]:


# From the test and Graph analysis the distribution is normally distributed


# In[45]:


plt.figure(figsize=(6, 4))
sns.countplot(df1['Gender'])
plt.title('Count of Gender')
plt.show()


# In[46]:


#Bivariate analaysis


# In[48]:


plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender', y='BloodPressure', data=df1)
plt.title('Blood Pressure vs. Gender')
plt.xlabel('Gender')
plt.ylabel('Blood Pressure')
plt.show()


# In[51]:


# Box plot for Age
plt.figure(figsize=(8, 6))
sns.boxplot(x='Age', data=df1, color='skyblue')
plt.title('Box Plot of Age')
plt.xlabel('Age')
plt.show()


# In[58]:


#Hypothesis Testing using ANOVA
#Null Hypothesis (H0): The mean blood pressure is the same across all medication groups.
#Alternative Hypothesis (H1): At least one medication group has a different mean blood pressure from the others


# In[61]:


# One-way ANOVA
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Fit ANOVA model
model = ols('BloodPressure ~ Medication', data=df1).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(model, typ=2)
print("\nOne-Way ANOVA Results:")
print(anova_table)


# In[62]:


# Significance level
alpha = 0.05

# Check if p-value is less than alpha
if anova_table['PR(>F)'][0] < alpha:
    print("Reject the null hypothesis (H0).")
    print("There is a significant difference in the mean blood pressure levels among different medication groups.")
else:
    print("Fail to reject the null hypothesis (H0).")
    print("There is no significant difference in the mean blood pressure levels among different medication groups.")

