#!/usr/bin/env python
# coding: utf-8
import yfinance as yf
import numpy as np
import pandas as pd
import statsmodels.api as sm

data =  yf.download("xle", start='1990-01-01')

print(data)

df = data["Close"].pct_change() * 100

#print(df)

df = df.rename("Today_Change_%")
df = df.reset_index()
#print(df)

df1 = pd.merge(data,df, on="Date")

df1['Volume_Lag'] = data.Volume.shift(1).values/1000000000
df1['Volume'] = df1['Volume']/1000000000
#df1.rename(columns={'Volume_Lag': 'Volume'}, inplace=True)

df1["Up_Down"] = [1 if (i > 0) else 0 for i in df1["Today_Change_%"]]

#print(df1)

df1["Trend"] =  (df1["Close"] - df1["Low"])/ ((df1["High"] - df1["Low"]))

df1["Trend_Lag1"] = df1["Trend"].shift(1)

df1 = sm.add_constant(df1)

df1.dropna(inplace= True)
#print(df1)

X = df1[['const','Trend_Lag1','Volume_Lag']]

y = df1["Up_Down"].values

cutoff=0.50

model = sm.Logit(y,X)

result =  model.fit()

result.summary()

prediction = result.predict(X)


df1['Prediction_Caculated'] = pd.array(prediction)
df1['Prediction_indicator'] = pd.array([1 if i > cutoff else 0 for i in prediction])
#print(df1.tail(10))

y = df1["Up_Down"].values

def confusion_matrix(act,pred):
    predtrans = ['Up' if i > cutoff else 'Down' for i in pred]
    actuals = ['Up' if i > 0 else 'Down' for i in act]
    confusion_matrix = pd.crosstab(pd.Series(actuals),
                                   pd.Series(predtrans),
                                   rownames = ["Actual"],
                                   colnames = ["Predict"]
                                  )
    return confusion_matrix

confusion_matrix(y,prediction)

z = confusion_matrix(y,prediction)
print (((z.iloc[0,0] + z.iloc[1,1])) / len(df1))

x_tran= df1[df1.Date.dt.year < 2020][['const','Trend_Lag1','Volume_Lag']]
y_train=df1[df1.Date.dt.year < 2020]["Up_Down"]
x_test= df1[df1.Date.dt.year >= 2020][['const','Trend_Lag1','Volume_Lag']]
y_test= df1[df1.Date.dt.year >= 2020]["Up_Down"]

result=model.fit()

confusion_matrix(y_test, prediction)

#len(x_test)


# In[35]:


z = confusion_matrix(y_test,prediction)
(z.iloc[0,0] + z.iloc[1,1]) / len(x_test)
#((z.iloc[0,0] + z.iloc[1,1])) / ((z.iloc[0,0] + z.iloc[1,1]) + z.iloc[1,0] + z.iloc[0,1])


((z.iloc[0,0])+(z.iloc[1,1])) / ((z.iloc[0,0] + z.iloc[1,1]) + z.iloc[1,0])

df1 = df1.assign(share=np.nan,money=np.nan)

#Simulate Investment transaction buy on opening at 1 and sell average at 0

def buy_sell(open_price, sell_price,prediction, money, share):
    if prediction == 1 and money != 0:
        share =  money / open_price
        money = 0
    elif prediction == 0 and share != 0:
        money = share * sell_price
        share = 0
    else: pass
    return [money, share]
money = 1000000
share = 0
for i in range(len(df1)):
    [money, share] = buy_sell(df1.iloc[i,2],(df1.iloc[i,3]+df1.iloc[i,4])/2,df1.iloc[i,14], money, share)
    df1.iloc[i,15] = share
    df1.iloc[i,16] = money
    

print ("The investment return = $%.2f, and the shares are %.2f shares" %(money, share))

#df1.tail(20)

# Base on today's data to  predicate tomorrow trend
prediction = result.predict(x_test)
tomorrow_up_down = result.predict([1.0,df1.iloc[-1,11],df1.iloc[-1,7]])
print ("Tomorrow\'s trend= %f" %tomorrow_up_down)
print ("It will go up") if tomorrow_up_down > 0.5 else print ("It will go down") 

#df1.to_csv('fb.csv', index = False)

