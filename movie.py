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
driver = webdriver.Chrome()
driver.maximize_window()

BMS_url="https://in.bookmyshow.com/mumbai/movies/hanuman/ET00311673"

driver.get(BMS_url) 
driver.execute_script("window.scrollTo(0, 10000);")
# document.documentElement.scrollHeight




# Get the HTML content after scrolling and waiting
html_content = driver.page_source

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

target_div = soup.find('div', class_='sc-qswwm9-5 ghYvew')

span_element = soup.find('span', class_='one-line-image-info__Title-sc-ec6ph5-3 gZTkaq')
print("*******************************************")
print("rating : "+span_element.text.strip())
a_element = soup.find('a', class_='event-attributes__LinkedElements-sc-2k6tnd-2 fGsLFN')
print("screen format : "+a_element.text.strip())
div_element = soup.find_all('div', class_='event-attributes__EventAttributesContainer-sc-2k6tnd-1 jwbjBD')
details=div_element[1].text.strip().split(' • ');
print("duration : "+details[0].strip())
print("genre : "+details[1].strip())
print("release date : "+details[3].strip())
# print("duration : "+div_element.text.strip())
section=soup.find('section', id='component-1')
about=section.find('span').text.replace('About the movie', '').strip()

print("description : "+about)
print("*******************************************")
# print(section)
time.sleep(20)
driver.quit()

