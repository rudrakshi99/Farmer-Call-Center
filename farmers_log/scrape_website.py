from bs4 import BeautifulSoup
import requests


def scrape_website(url):
    result = '' 
    try:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content,'html.parser')        
        s = soup.find('body')
        divs = s.find_all('div')
        intr = 0
        for div in divs:
            if intr < 5  and intr != 0:
                print('Working', intr)
                texts = div.find_all('p')
                for text in texts:
                    result += text.getText(separator=u' ')
            intr = intr + 1
    except Exception:
        result = None
    return result
