from bs4 import BeautifulSoup
import requests


def scrape_website(url,tag = 0):
    result = '' 
    try:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content,'html.parser')        
        s = soup.find('body')
        divs = s.find_all('div')

        for div in divs:
            texts = div.find_all('p')
            for text in texts:
                if len(result) < 900 or tag == 0:
                    result += text.getText(separator=u' ')
            
            
    except Exception:
        result = None
    return result
