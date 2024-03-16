from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests

# Set up the webdriver
chrome_options = Options()
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
driver.maximize_window()
root_url = "https://insider.in"
PYTM_url="https://insider.in/all-events-in-mumbai-today/gaming-and-entertainment"


driver.get(PYTM_url) 
driver.execute_script("window.scrollTo(0,10000);")


# Get the HTML content after scrolling and waiting
html_content = driver.page_source

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
event_cards = soup.find_all('div', {'data-ref': 'event_card'})
# print(event_cards)

for event_card in event_cards:
    # Extract data from <a> tag
    href_value = root_url+event_card.find('a')['href']
    response = requests.get(href_value)
    
    if response.status_code == 200:
        linked_page_html = response.text
        linked_page_soup = BeautifulSoup(linked_page_html, 'html.parser')
        buy_now_link = linked_page_soup.find('a', {'data-ref': 'edp_buy_button_desktop', 'class': 'css-10lu0qa'})
        
        if buy_now_link:
            buy_now_href = root_url + buy_now_link['href']
            print("BUY NOW Href:", buy_now_href)
        else:
            print("BUY NOW link not found on the linked page.")

        
        venue_section = linked_page_soup.find('section', {'id': 'section-venue'})
        if venue_section:
            h3_text = venue_section.find('h3').text if venue_section.find('h3') else None
            p_text = venue_section.find('p').text if venue_section.find('p') else None
            print("Venue Name (h3):", h3_text)
            print("Venue Address (p):", p_text)
        # print("HTML Content of Linked Page:")
        # print(linked_page_html)
        # print("\n")
    else:
        print(f"Failed to fetch content for {href_value}. Status code: {response.status_code}")
    # Extract data from <img> tag
    img_src = event_card.find('img', {'data-ref': 'event_card_image'})['src']

    # Extract text from <span> with class="card-genre css-mrmzh"
    genre_text = event_card.find('span', {'class': 'card-genre css-mrmzh'}).text

    # Extract text from <span> with data-ref="event_card_title"
    title_text = event_card.find('span', {'data-ref': 'event_card_title'}).text

    # Extract text from <p> tag inside <div> with data-ref="event_card_date_string"
    date_text = event_card.find('div', {'data-ref': 'event_card_date_string'}).find('p').text

    # Extract text from <p> tag inside <div> with data-ref="event_card_location"
    location_text = event_card.find('div', {'data-ref': 'event_card_location'}).find('p').text

    # Extract text from <p> tag with class="css-1sh8h77"
    price_text = event_card.find('p', {'class': 'css-1sh8h77'}).text

    # Print or use the extracted data as needed
    print("Href:", href_value)
    print("Img Src:", img_src)
    print("Genre:", genre_text)
    print("Title:", title_text)
    print("Date:", date_text)
    # print("Location:", location_text)
    print("Price:", price_text)
    print("\n")

time.sleep(10)
driver.quit()


