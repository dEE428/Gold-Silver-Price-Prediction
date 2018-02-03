''''
This routine implements the Augmented Dickey-Fuller test to check whether time series is stationary or non-stationary, or -  in different words - how strongly a time series is defined by an  trend underlying noisy data.


Null Hypothesis (H0): the time series has some time-dependent trend.
Alternate Hypothesis (H1): the time series is stationary.

We interpret this result using the p-values, that is a p-value below a fixed threshold (e.g. 1%) indicates that we reject the null hypothesis, otherwise a p-value above that threshold indicates that we accept the null hypothesis.
'''

from statsmodels.tsa.stattools import adfuller
import pandas as pd, sys, matplotlib.pyplot as plt

if len(sys.argv) <2:
    print 'Syntax: python ADFuller.py silver'
    exit()

commodity = pd.read_csv(sys.argv[1].capitalize()+' Futures Historical Data.csv',parse_dates=[0],index_col=0, thousands=',')

X = commodity.Price.values
result = adfuller(X, autolag='AIC')
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, val in result[4].items():
	print('\t%s: %.3f' % (key, val))
print


'''
In the 2nd part of code we train an ARIMA model, use it to make a prediction, and inspect the confidence interval.

The dataset is split into a training (all the observations but the last point) and test dataset (the last single observation)/ We make a prediction for the latter to be compared with the real measurement.

Note that the alpha argument on the forecast() function specifies the (1-alpha) confidence level. The second last point of the measurement should be coompared (look at the generated plot) to the aformentioned confidence level to assess whether we can predict if the price of the commodidity is increasing or decreasing
'''

from statsmodels.tsa.arima_model import ARIMA
X_train, X_test = X[:len(X)-1], X[len(X)-1:]
model = ARIMA(X_train, order=(5,1,1))
res=model.fit(disp=False,maxiter=1000)
forecast, err, conf_lev = res.forecast(alpha=0.05)
print; print('95%% Confidence Level range of the prediction: %.3f to %.3f' % (conf_lev[0][0], conf_lev[0][1]))



fig, ax = plt.subplots()
fig = res.plot_predict(len(X_train)-10, len(X_train)+1, dynamic=False, ax=ax,plot_insample=True)
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Prediction of price of '+sys.argv[1]+' vs. Observations')
fig.savefig(sys.argv[1]+"_prediction.pdf")







