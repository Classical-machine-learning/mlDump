import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.vector_ar.var_model import VAR


df = pd.read_csv('dataset.csv',parse_dates=[['Date','Time']])
# print(df.dtypes)

df['Date_Time'] = pd.to_datetime(df.Date_Time,format= '%d/%m/%y %H.%M.%S')
data = df.drop(['Date_Time'],axis=1)
data.index = df.Date_Time
cols = data.columns

for b in cols:
    for a in range(len(data)):
        if(data[b][a]==-200):
            data[b][a] = data[b][a-1]

def plot_initial(data):
    plt.figure(figsize=(12,12))
    plt.plot(data)
    plt.grid(True)
    plt.show()
plot_initial(data)

# testing on validation data
""" train = data[:int(0.8*(len(data)))]
valid = data[int(0.8*(len(data))):]
model = VAR(endog = train)
model_fit = model.fit()

prediction = model_fit.forecast(model_fit.y,steps = len(valid))
prediction_df = pd.DataFrame(index = range(0,len(prediction)),columns=[cols])

for j in range(0,13):
    for i in range(0, len(prediction)):
       prediction_df.iloc[i][j] = prediction[i][j]

print(prediction_df.head()) """

#training on full data
# model = VAR(endog = data)
# model_fit = model.fit()
# model_fit.save('model_VAR.pkl')
# prediction2 = model_fit.forecast(model_fit.y,steps = 1)
# print(prediction2)