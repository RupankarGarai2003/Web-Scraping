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

# Initialize WebDriver with ChromeDriverManager and the options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.chennaidiamonds.in/")
print("This is the data of chennaidiamonds......")
driver.implicitly_wait(3)

# Function to perform search
def search(keyword):
    search_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/header/div/div[2]/div[2]/div/div/section[1]/div[2]/div[1]/div[2]/div/div[4]/div/div[1]/form/div/div[3]/div/div/div/input")
    search_input.send_keys(keyword, Keys.ENTER)

# Function to retrieve total item count
def Total_item():
    try:
        item_no = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "snA2M55")))
        text = item_no.text.strip()
        if text:
            total_item_no = text.split()[0]
        else:
            total_item_no = "N/A"
    except TimeoutException:
        print("Timeout: Element not found or not visible")
        total_item_no = "N/A"
    except IndexError:
        print("IndexError: Unable to split text")
        total_item_no = "N/A"
    return total_item_no

# Function to navigate back to main page
def Time_Back():
    time.sleep(5)
    driver.get("https://www.chennaidiamonds.in/")
    time.sleep(3)

# Create a list to store the data
data = []

# Perform searches and retrieve total item counts
keywords = ["Men", "Women", "Male", "Rings", "Men's Rings", "Women's Rings", "Male's Rings", "Female's Rings", "Earring", "Men's Earring", "Women's Earring", "Male's Earring", "Female's Earring", "Diamond", "Men's Diamond", "Women's Diamond", "Male's Diamond", "Female's Diamond", "Silver", "Men's Silver", "Women's Silver", "Male's Silver", "Female's Silver", "Necklaces", "Men's Necklaces", "Women's Necklaces", "Male's Necklaces", "Female's Necklaces", "Bracelets", "Men's Bracelets", "Women's Bracelets", "Male's Bracelets", "Female's Bracelets", "Pendant Sets", "Men's Pendant Sets", "Women's Pendant Sets", "Male's Pendant Sets", "Female's Pendant Sets", "Necklace Sets", "Men's Necklace Sets", "Women's Necklace Sets", "Male's Necklace Sets", "Female's Necklace Sets", "Harams", "Men's Harams", "Women's Harams", "Male's Harams", "Female's Harams", "Bangles", "Men's Bangles", "Women's Bangles", "Male's Bangles", "Female's Bangles", "Accessories", "Men's Accessorie", "Women's Accessorie", "Male's Accessorie", "Female's Accessorie", "Nose Pins", "Men's Nose Pins", "Women's Nose Pins", "Male's Nose Pins", "Female's Nose Pins", "Solitaire", "Men's Solitaire", "Women's Solitaire", "Male's Solitaire", "Female's Solitaire", "Gifts", "Men's Gifts", "Women's Gifts", "Male's Gifts", "Female's Gifts", "Gold Coins", "Men's Gold Coins", "Women's Gold Coins", "Male's Gold Coins", "Female's Gold Coins"]

for keyword in keywords:
    search(keyword)
    item_count = Total_item()
    data.append([keyword, item_count])
    Time_Back()

# Write data to CSV file in a specific directory
csv_file_path = r'D:\\Web Scraping\National_jewellery (India)\\CSV_files\\chennaidiamonds.csv'
  #you can change your path location
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Keyword', 'Total Item Count'])
    writer.writerows(data)

print("Data saved to", csv_file_path)
driver.quit()  # Quit the WebDriver session
