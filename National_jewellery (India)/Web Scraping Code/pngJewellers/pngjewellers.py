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
driver.get("https://www.pngjewellers.com/")
print("This is the data of pngjewellers......")
driver.implicitly_wait(3)

# Function to perform search
def search(keyword):
    search_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/header/div[2]/div/div[3]/div[1]/div[1]/div/div/div/input")
    search_input.send_keys(keyword, Keys.ENTER)

# Function to retrieve total item count
def Total_item():
    try:
        item_no = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/h3")))
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
    driver.get("https://www.pngjewellers.com/")
    time.sleep(3)

# Perform searches and retrieve total item counts
keywords = ["Men", "Women", "Rings", "Earring", "Diamond", "Silver", "Necklaces", "Men's Ring", "Women's Ring", "Men's Earing", "Men's Diamond", "Women's Diamond", "Men's Gold", "Women's Gold","Men's Silver", "Women's Silver","Men's Necklaces","Women's Necklaces"]

# Create a list to store the data
data = []

for keyword in keywords:
    search(keyword)
    item_count = Total_item()
    data.append([keyword, item_count])
    Time_Back()

# Write data to CSV file
csv_file_path = r'D:\\Web Scraping\National_jewellery (India)\\CSV_files\\pngjewellers.csv'
 #you can change your path location
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Keyword', 'Total Item Count'])
    writer.writerows(data)
print("Data saved to ",csv_file_path)
driver.quit()  # Quit the WebDriver session
