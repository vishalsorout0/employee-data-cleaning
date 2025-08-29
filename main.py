import numpy as np
import pandas as pd

df=pd.read_csv("employee_records_messy.csv")

print(df.head(3))
print(df.isnull().sum())
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
df['Age'].fillna(df['Age'].median(),inplace=True)
print(df.isnull().sum())



# replacing infinity values
df.replace([np.inf,-np.inf],np.nan,inplace=True)
df.fillna(df.mean(numeric_only=True),inplace=True)





# deleting duplicates
df.drop_duplicates(inplace=True)
print(df.shape)#(30000, 8)




# replace negative salaries
# np.where(condition,value if true,value if false)
df['Salary']=np.where(df['Salary']<0,df['Salary'].mean(),df['Salary'])
df['Age']=np.where(df['Age']<0,df['Age'].mean(),df['Age'])


# handeling outliners of salary(removing rows)
mean=df['Salary'].mean()
standard_deviation=df['Salary'].std()
lower_bound= mean-(3 * standard_deviation)
upper_bound= mean+(3 * standard_deviation)

df=df[(df['Salary']>lower_bound)&(df['Salary']<upper_bound)]
df=df[(df['Age']>18)&(df['Age']<100)]
df.reset_index(drop=True,inplace=True)



# sorting 
df.sort_values(by="Employee_ID",ascending=True,inplace=True)



# removing extra spaces
df['Country']=df['Country'].str.strip()
df['Department']=df['Department'].str.strip()



# making cases consitent
df['Country']=df['Country'].str.capitalize()
df['Department']=df['Department'].str.upper()






df.to_csv("cleaned_data.csv",index=False)

print("data cleaned compeleted ! ")
newdf=pd.read_csv('cleaned_data.csv')

print(newdf.shape)#(29996, 8)
