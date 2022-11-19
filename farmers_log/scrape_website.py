from bs4 import BeautifulSoup
from selenium import webdriver
import requests


def scrape_website(url):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content,'html.parser')
    result = '' 
    s = soup.find('body')
    divs = s.find_all('div')
    for div in divs:
        texts = div.find_all('p')
        for text in texts:
            result += text.getText(separator=u' ')
    return result
