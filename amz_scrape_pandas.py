import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


page_count = 2

def get_data(pageNum):  
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    URL = requests.get('https://www.amazon.com/s?k=amazon+echo&page='+str(pageNum)+'&qid=1607639088&ref=sr_pg_'+str(pageNum), headers=headers)
    content = URL.content
    time.sleep(1)
    soup = BeautifulSoup(content, "lxml")

    data_list = []

    # Scrape product titles by attributes    
    for s in soup.findAll('div', attrs={'class':'a-section a-spacing-medium'}):
    
        name = s.find_all('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})

        data_list2 = []

        # Append scraped data to the empty list
        if name is not None:
            for n in name:
                names = n.text
                data_list2.append(names)

        data_list.append(data_list2)

    return data_list


# Run the function for each page
final_result = []
for i in range(1, page_count+5):
    final_result.append(get_data(i))


# Export the result as a csv file using pandas
data_set = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(data_set(final_result),columns=['Product Title'])
df.to_csv('products_title.csv', index=False, encoding='utf-8')

df = pd.read_csv("products_title.csv")
df.shape
