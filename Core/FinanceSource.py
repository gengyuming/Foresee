import pandas_datareader as pdr
import fix_yahoo_finance as yf

yf.pdr_override('yahoo')
start_date = "2021-3-1"
end_date = "2021-5-1"
data = pdr.data.DataReader('600406.SZ', 'yahoo', start=start_date, end=end_date)

print(data.describe)



