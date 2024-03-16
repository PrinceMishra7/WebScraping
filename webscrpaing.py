from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up the webdriver
chrome_options = Options()
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
driver.maximize_window()

# BMS_url="https://insider.in/all-events-in-mumbai/tour"
BMS_url="https://in.bookmyshow.com/explore/movies-mumbai"

driver.get(BMS_url) 
driver.execute_script("window.scrollTo(0,10000);")

html_content = driver.page_source

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

selected_links = soup.select('a.commonStyles__LinkWrapper-sc-133848s-11.style__CardContainer-sc-1ljcxl3-1.biDHta')
# print(selected_links[0])
for link in selected_links:
    href_value = link['href']
    
    print(href_value)


# selected_links.pop(0)
# 
time.sleep(10)
driver.quit()

