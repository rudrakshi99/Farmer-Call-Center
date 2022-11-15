from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service


def scrape_website(URL):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    service = Service("/home/ubuntu/selenium_drivers/chromedriver")
    # URL = "https://extension.psu.edu/controlling-birds-on-fruit-crops"
    try:
        driver = webdriver.Chrome(service = service, options = options)
        driver.get(URL)
        driver.implicitly_wait(2)
        html_content = driver.page_source
        driver.quit()
    except WebDriverException:
        driver.quit()

    soup = BeautifulSoup(html_content,'html.parser')
    text = soup.getText(separator=u' ')

    result = ''
    for each in ['body']:
        s = soup.find(each)
        divs = s.find_all('div')
        for div in divs:
            texts = div.find_all('p')
            for text in texts:
                result += text.getText(separator=u' ')
    return result