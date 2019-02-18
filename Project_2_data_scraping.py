import pandas as pd
from bs4 import BeautifulSoup
import requests


def data_scrape(**record):
    job_element = (record['job']).replace(' ', '%2B')
    state_element = record['state']
    years_element = record['years']

    url = 'https://www.dice.com/salary-calculator?title='+job_element+'&location='+state_element+'&experience='+years_element 
    #print(url)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        record['sal_min'] =soup.find('span', id='minSalMbl').text
        record['sal_avg'] = soup.find('span', id='maxSalMbl').text
        
       # print(record) 

    except:
        print("Scraping Failed for "+ url)


    
    return (record)