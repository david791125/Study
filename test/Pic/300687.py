import tushare as ts
import os
d = ts.get_hist_data('300687',start='2019-03-01',end='2019-03-18')
print(d)