# %%
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get('https://auto-abonnement.centraalbeheer.nl/app/showroom')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a', href=True)
car_links = [link.get('href') for link in links if '/app/showroom' in link.get('href')]

print(car_links)

# %%

def single_brand_all_urls_scraper(driver, website_base_url, brand_specific_url_end):
    driver.get(website_base_url + brand_specific_url_end)
    html = driver.page_source
    
    return(html)

html_tesla = single_brand_all_urls_scraper(driver = driver, website_base_url='https://auto-abonnement.centraalbeheer.nl', brand_specific_url_end= '/app/showroom/Tesla/Model%203')
tesla_soup = BeautifulSoup(html_tesla, 'html.parser')
divs = tesla_soup.find_all('div') 

# need to find a specific div : grid gap-5 but it does not seem to 
# be present in the html strangely. As if the driver is not 
# picking up the js stuff












# session = HTMLSession()

# r = session.get('https://auto-abonnement.centraalbeheer.nl/app/showroom')

# p = r.html.find('ul class ="grid grid-cols-2 gap-5 md:grid-cols-3"', first=True)




# print(p)


# html = requests.get('https://auto-abonnement.centraalbeheer.nl/app/showroom')
# soup = BeautifulSoup(html.text, 'lxml')
# li = soup.find_all('ul')

# print(soup.html)


# links = soup.find_all('a href')

# print(links)

# %%
