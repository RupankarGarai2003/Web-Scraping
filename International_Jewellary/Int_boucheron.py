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
driver.get("https://www.boucheron.com/en/catalogsearch/")
time.sleep(9)
driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div/div/div[2]/div/div/button").click()
print("This is the data of boucheron......")
driver.implicitly_wait(3)

# Function to perform search
def search(keyword):
    click_search_btn=driver.find_element(By.XPATH,"/html/body/div[2]/header/div[3]/nav/li[3]/button").click()
    time.sleep(3)
    search_input = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[3]/div/div[2]/div/div[2]/div/div/div/section[3]/div/div[1]/form/input")
    time.sleep(2)
    search_input.send_keys(keyword, Keys.ENTER)
    
def Total_item():
    try:
        item_no_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/main/div[3]/div/div[1]/div/div/div[2]")))
        text = item_no_element.text.strip()
        # Extracting only the digits from the text
        total_item_no = ''.join(filter(str.isdigit, text))
    except TimeoutException:
        print("Timeout: Element not found or not visible")
        total_item_no = "N/A"
    return total_item_no

def Time_Back():
    time.sleep(5)
    driver.get("https://www.boucheron.com/en/catalogsearch/")
    time.sleep(3)

# Create a list to store the data
data = []

# Perform searches and retrieve total item counts
keywords = ["Men", "Women", "Men's Rings", "Women's Rings","Men's Earring", "Women's Earring", "Diamond", "Men's Diamond", "Women's Diamond", "Silver", "Men's Silver", "Women's Silver","Necklaces", "Men's Necklaces", "Women's Necklaces", "Bracelets", "Men's Bracelets", "Women's Bracelets","Pendant Sets", "Men's Pendant Sets", "Women's Pendant Sets","Necklace Sets", "Men's Necklace Sets", "Women's Necklace Sets","Bangles", "Men's Bangles", "Women's Bangles", "Male's Bangles","Gold Coins","Head Jewellary","Brooches"]
for keyword in keywords:
    search(keyword)
    item_count = Total_item()
    print(item_count)
    data.append([keyword, item_count])
    Time_Back()
    
csv_file_path = './boucheron.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Keyword', 'Total Item Count'])
    writer.writerows(data)

print("Data saved to", csv_file_path)
driver.quit()
