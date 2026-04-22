import pandas as pd
df=pd.DataFrame({
    "Name":["Sanjog","Sarin","Swagat","Susan"],
    "Age":[20,21,21,22],
    "Address":["Parbat","Kirtipur","Nuwakot","Dang"]
})
#basic writing of csv file
df.to_csv("output1.csv")
#not including the index columns
df.to_csv("output2.csv",index=False)
#custom separation
df.to_csv("output3.csv",index=False,sep=";")
#writing only specific columns
df.to_csv("output4.csv",index=False,columns=["Name","Age"])