# Exponential Move Average
""" Exponential Move Average (EMA)

Moving average are financial indicators which are used to analyze stock values
over a long period of time. EMA is a type of moving average. It help users to filter noise 
and produce a smooth curve.

```
EMAToday=( ValueToday*(Constant/ (1 + No. Of Days)) )+( EMAYesterday*(1-(Constant/(1+No. Of Days))))
```

# Using ewm method in Pandas
```
Syntax: DataFrameName.ewm(com=value)
`````

"""


import pandas as pd
import matplotlib.pyplot as plt

# create a dataframe
stockValues = pd.DataFrame(
    {"Stock_Values": [60, 102, 103, 104, 101, 105, 102, 103, 103, 102]}
)

# Finding EMA
# Use any good contant value that result in smoothe curve

ema = stockValues.ewm(com=0.4).mean()
plt.plot(stockValues, label="Stock Values")
plt.plot(ema, label="EMA values")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.show()
