import os
import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

# Define a global count variable
img_count = 40

# Define a function to save images
def save_image(src):
    global img_count  # Access the global count variable
    img_dir = r'D:\Web Scraping\National_jewellery (India)\Img Scraping\Orra Fine Jewellery\Imgs'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    response = requests.get(src)
    if response.status_code == 200:
        img_count += 1  # Increment the count
        file_path = os.path.join(img_dir, f"image_{img_count}.jpg")  # Use count in the file name
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"Image {img_count} saved successfully at: {file_path}")
    else:
        print(f"Failed to download image from {src}, status code: {response.status_code}")

# Create an instance of Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver with ChromeDriverManager and the options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://www.orra.co.in/")
print("This is the image data of Orra Fine Jewellery ......")
driver.implicitly_wait(3)

def search(keyword):
    time.sleep(2)  # Add a brief delay before searching for the element
    search_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/form/div[1]/div/input"))
    )
    search_input.clear()
    search_input.send_keys(keyword, Keys.ENTER)


# Define a function to scroll and extract image sources
def total_img_item():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Adjust sleep time according to your needs
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # Find all img elements
    img_elements = driver.find_elements(By.TAG_NAME, 'img')
    for img_element in img_elements:
        try:
            src = img_element.get_attribute("src")
            if src and ".jpg" in src:
                save_image(src)
        except StaleElementReferenceException:
            # If element is stale, continue with the loop
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            # Handle SSL handshake errors
            if isinstance(e, (requests.exceptions.SSLError, requests.exceptions.ConnectionError)):
                print("SSL handshake error encountered. Waiting and retrying...")
                time.sleep(10)  # Wait for some time before retrying
                continue

# Perform searches and retrieve images
keywords = ["Harams", "Bangles", "Accessories", "Nose Pins", "Solitaire", "Gifts", "Gold Coins", "Silver", "Necklaces", "Bracelets", "Pendant Sets", "Rings", "Earing", "Gold", "Silver"]

for keyword in keywords:
    search(keyword)
    total_img_item()

# Close the WebDriver session
driver.quit()
