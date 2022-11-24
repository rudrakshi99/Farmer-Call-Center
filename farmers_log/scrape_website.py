import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    result = '' 
    try:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content,'html.parser')        
        s = soup.find('body')
        divs = s.find_all('div')

        for div in divs:
            texts = div.find_all('p')
            for text in texts:
                if len(result) < 800:
                    result += text.getText(separator=u' ')
            
            
    except Exception:
        result = None
    return result
