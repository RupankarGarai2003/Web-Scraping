import csv
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Create an instance of Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Disable notifications
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver with ChromeDriverManager and the options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://www.kushals.com/")
print("This is the data of Kushal's Fashion Jewellery......")
driver.implicitly_wait(12)

# Function to perform search
def search(keyword):
    try:
        # Wait for the search input field to be clickable
        search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.main-search__input_st.wizzy-search-input")))
        search_input.clear()  # Clear any existing text in the input field
        search_input.send_keys(keyword, Keys.ENTER)
    except Exception as e:
        print("Error occurred while searching:", e)


# Function to retrieve total item count
def Total_item():
    try:
        item_no_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div[1]/div/p")))
        text = item_no_element.text.strip()
        # Extracting only the digits from the text
        total_item_no = ''.join(filter(str.isdigit, text))
    except TimeoutException:
        print("Timeout: Element not found or not visible")
        total_item_no = "N/A"
    return total_item_no




# Function to navigate back to main page
def Time_Back():
    time.sleep(5)
    driver.get("https://www.kushals.com/")
    time.sleep(3)

# Create a list to store the data
data = []

# Perform searches and retrieve total item counts
keywords = ["Men", "Women" , "Rings", "Men's Rings", "Women's Rings", "Earring", "Men's Earring", "Women's Earring", "Male's Earring", "Diamond", "Men's Diamond", "Women's Diamond", "Female's Diamond", "Silver", "Men's Silver", "Women's Silver", "Male's Silver", "Necklaces", "Men's Necklaces", "Women's Necklaces", "Male's Necklaces", "Bracelets", "Men's Bracelets", "Women's Bracelets", "Male's Bracelets", "Pendant Sets", "Men's Pendant Sets", "Women's Pendant Sets", "Male's Pendant Sets", "Necklace Sets", "Men's Necklace Sets", "Women's Necklace Sets", "Male's Necklace Sets", "Harams", "Women's Harams","Bangles", "Men's Bangles", "Women's Bangles", "Male's Bangles", "Accessories", "Women's Accessorie", "Nose Pins", "Women's Nose Pins", "Solitaire", "Men's Solitaire", "Women's Solitaire", "Gifts", "Men's Gifts", "Women's Gifts", "Men's Gold Coins", "Women's Gold Coins", "Male's Gold Coins"]

for keyword in keywords:
    search(keyword)
    item_count = Total_item()
    data.append([keyword, item_count])
    Time_Back()

# Write data to CSV file in a specific directory
csv_file_path = r'D:\\Web Scraping\National_jewellery (India)\\CSV_files\\KushalsFashionJewellery.csv'

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Keyword', 'Total Item Count'])
    writer.writerows(data)

print("Data saved to", csv_file_path)
driver.quit()  # Quit the WebDriver session