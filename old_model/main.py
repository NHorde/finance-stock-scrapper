# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:50:37 2019

@author: Nicolas
"""

import  equests
from bs4 import BeautifulSoup
import re
from json import loads
from pprint import pprint as pp
import pandas as pd
from time import sleep

from progressbar import ProgressBar
pbar = ProgressBar()

col = ['Ticker','Total_Shares', 'Total_Cash','Total_Debt', 'Current_Price', 'Cash_Per_Share','Potential']
##list_company_data = pd.DataFrame([[0,0,0,0,0,0]], columns= col)
list_company_data = []
print(list_company_data)

#http://finance.yahoo.com/quote/AAPL/profile?p=AAPL
def scrap_data_company(ticker):
    print('Current Ticker: ', i)
    soup = BeautifulSoup(requests.get("https://finance.yahoo.com/quote/%s/key-statistics?p=%s" %(ticker, ticker)).content, 'lxml')
    script = soup.find("script",text=re.compile("root.App.main")).text
    data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))
    
    
    stores = data['context']['dispatcher']['stores']
    ## Check that there are data for this ticker:
    if 'QuoteSummaryStore' not in stores:
#        pass
        print('There are no data at all for this ticker')
    else:     
        quote_summary = stores['QuoteSummaryStore']
        
        ## Cash, debt and price per share
        if 'financialData' not in quote_summary:
 #           pass
            print('There are no statistics for this ticker')
        else: 
            financial_data = quote_summary['financialData']
            if 'currentPrice' not in financial_data:
 #              pass
               print('There are no current price for this ticker')
            else:
                curr_price = financial_data['currentPrice']['raw']
                
                ## Shares outstanding
                if quote_summary['defaultKeyStatistics'] == {}:
                    pass
                else:
                    if quote_summary['defaultKeyStatistics']['sharesOutstanding'] == {}:
#                      pass
                       print('There are no shares outstanding data for this ticker')
                    else:
                        
                        shares_outs = quote_summary['defaultKeyStatistics']['sharesOutstanding']['raw']
                        ## Company has no cash
                        if financial_data['totalCash'] == {}:
                            total_cash = 0
                        else:
                                total_cash = financial_data['totalCash']['raw'] 
                        ## Company has no debt
                        if financial_data['totalDebt'] == {}:
                            total_debt = 0
                        else:
                            total_debt = financial_data['totalDebt']['raw']
    
                        ## Cash per share
                        if shares_outs == 0:
                            cash_per_share = 0
                        else:
                            cash_per_share = (total_cash - total_debt) / shares_outs 
                        
                        ## Potential
                        if curr_price == 0:
                            potential = 0
                        else:
                            potential = (cash_per_share - curr_price) / curr_price
                        
                        ## Append into list
                        company_data = [ticker, shares_outs, total_cash, total_debt, curr_price, cash_per_share, potential]
                        list_company_data.append(company_data)
                        print('Ticker has been completed')
        return 



file = pd.read_csv('C:\\Users\\Nicolas\\Documents\\Investment\\Python\\Scrapping\\companylist.csv')


sleep_time = 2
num_retries = 4

for i in pbar(file['Symbol']):
    for x in range(0, 4):  # try 4 times
        str_error = 0
        try: 
            scrap_data_company(i)
            str_error = 0
        except :
            str_error = 1
        if str_error == 1:
            sleep(sleep_time)  # wait before trying to fetch the data again
            sleep_time *= 2  # Implement your backoff algorithm here i.e. exponential backoff
        else:
            break

    
print('Completed with success')

df = pd.DataFrame(list_company_data, columns = col)

df.to_excel('company_scrapped.xlsx', sheet_name='data')





