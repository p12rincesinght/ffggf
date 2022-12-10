from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(executable_path="Downloads")
driver.get("https://www.nytimes.com/international/section/science")

Data=driver.page_source
allData=''.join(Data)

arrhead=[]
arrpara=[]
arrlink=[]
soup=BeautifulSoup(allData,'html.parser')
for d in soup.find_all('section',id='stream-panel'):
    title=d.find_all('h2')
    t1=d.find_all('p',class_='css-1pga48a e15t083i1')
    t2=d.find_all('a')

    
    
for u in range(7):
    arrhead.append(title[u].text)
    arrpara.append(t1[u].text)
    arrlink.append(t2[u].get('href'))



df=pd.DataFrame({'Titles':arrhead,'Links':arrlink,'Descriptions':arrpara})
df.to_csv('data.csv',index=False)
print(df)