import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data={
    "Experience":[1,2,3,4,5],
    "TestScore":[50,60,70,80,90],
    "Communication":[5,6,7,8,9],
    "Hire":[0,0,1,1,1]
}

df=pd.DataFrame(data)

x=df[["Experience","TestScore","Communication"]]
y=df["Hire"]

model=RandomForestClassifier()
model.fit(x,y)

print(model.predict([[1,80,8]]))