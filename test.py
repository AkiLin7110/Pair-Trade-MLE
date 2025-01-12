import pandas as pd
import yfinance as yf
candidate = [
             'MMM', 'AA','AAPL',  'AXP',  'T','BAC',    'BA','CAT','CVX','CSCO',
              'KO', 'DD',  'HD', 'INTC','IBM','JNJ',   'JPM','LOW','MCD', 'MRK',
            'MSFT','PEP', 'PFE',   'PG','TRV','UNH','UTX.VI', 'VZ','WMT', 'DIS',
             'APO','XOM',  'GE','GOOGL', 'GS','HPQ'
             ] #UTX.VI: coperate with RTN #APO:purchase yahoo
a = yf.download(candidate, threads = True)['Close']
print(a)
a.to_excel('Data.xlsx')