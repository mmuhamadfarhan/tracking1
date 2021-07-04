from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import re
##scrapping bursa listed companies##
base_url = 'https://www.malaysiastock.biz/Listed-Companies.aspx?type=A&value=' # base_url

 # multiple page numbers
pages = ['0','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
CompanyCode=[]
CompanyFullName=[]
StockShortName=[]
StockCode=[]
MarketName=[]
Shariah=[]
Sector=[]
MarketCap=[]
LastPrice=[]
PEratio=[]
DivYield=[]
ROEquity=[]

driver = webdriver.Chrome(executable_path=r'C:/Users/username1/Desktop/python/chromedriver.exe')
for b in pages:
    driver.get(base_url + b)
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('table',href=False, attrs={'id':'MainContent_tStock'}):
        for c in a.findAll("a"):
            head, sep, tail = c.text.partition(' ')
            StockShortName.append(head)
            CompanyCode.append(re.sub('[^a-zA-Z0-9 \n\.]', '', tail))
        
        for d in a.findAll("img"):
                Shariah.append(d.getText)
            
        for e in a.findAll('td', attrs={'style':'text-align:left;'}):
            Sector.append(e.text)
        
        for f in driver.find_elements_by_xpath('//td[1]/h3[2]'):
            CompanyFullName.append(f.text)
        
        ##for g in driver.find_elements_by_xpath('//td[4]'):
        ##    MarketCap.append(g.text) ##cant trace using xpath. Need to find solution
            


df = pd.DataFrame({'CompanyCode':CompanyCode,
                   'StockShortName':StockShortName,
                   'Shariah':Shariah,
                   'Sector':Sector,
                   'CompanyFullName':CompanyFullName})


df = df.iloc[2:]
df['Date'] = datetime.datetime.now().strftime("%Y%m%d")
df['Shariah'] = df['Shariah'].astype('string')
df.loc[(df.Shariah == '<bound method Tag.get_text of <img src="https://www.malaysiastock.biz/App_Themes/images/Yes.png" width="14"/>>'),'Shariah']='Yes'
df.loc[(df.Shariah == '<bound method Tag.get_text of <img src="https://www.malaysiastock.biz/App_Themes/images/No.png" width="14"/>>'),'Shariah']='No'


df.to_csv('Scrappingbursa.csv', index=False, encoding='utf-8')


