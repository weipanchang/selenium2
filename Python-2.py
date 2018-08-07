import datetime, quandl
quandl.ApiConfig.api_key = "xHRiHvCsbAsbzmE2dvxy"
mydata = quandl.get("FRED/GDP")
ndq = quandl.get("NASDAQOMX/COMP-NASDAQ", 
              trim_start='2018-03-01', 
              trim_end='2018-04-03')

print(ndq.head(4))