import pandas as pd
from sklearn.linear_model import LinearRegression
data={
    "Size":[1000,1500,2000],
    "Bedrooms":[2,3,4], 
    "price":[50,75,100]
}
df=pd.DataFrame(data)
x=df[["Size"]]
y=df["price"]
model=LinearRegression()
model.fit(x,y)
print("Price of the 1800sqft", model.predict([[1800]]))