#import pandas as pd
#df=pd.DataFrame({
    #"Name":["Roshini","Sahaja","priya"],
    #"Age":[20,21,22],
    #"City":["Hyderabad","Bangalore","Chennai"],
   # "Marks":[85,80,90]
#})
#print(df[df["Marks"]>80])

#data={
    ##df=pd.DataFrame(data)
#print(df.isnull())
#df['Marks'].fillna(df['Marks'].mean(), inplace=True)
#df['Age'].fillna(df['Age'].median(), inplace=True)
#df['height'].fillna(df['height'].min(), inplace=True)
#df.dropna(inplace=True)
#print(df)

import matplotlib.pyplot as plt
names=['A','B','C','D']
marks= [85,90,95,80]
plt.bar(names, marks)
plt.xlabel('Names')
plt.ylabel('Marks')
plt.title('Marks of students')
plt.savefig('marks_chart.png')
print("Chart saved as marks_chart.png")

#plt.plot(names,marks)

#plt.xlabel('Names')
#plt