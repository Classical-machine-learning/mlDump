# README

Time series
- Series of data points indexed in a line order in time.
- Timestamps
- May contain info we need to extract

Two types:
1) Univariate
- just one dependant variable

2) Multivariate
- more than one dependant variable
- Using VAR: Vector Auto regression
- Each variable is a linear function of the past values of itself as well as the past values of the other variables.
- Unlike AR, relationship between variables is used.
- Dynamic behavior of data

timeseries.py uses VAR
timese.py uses Keras : LSTM
