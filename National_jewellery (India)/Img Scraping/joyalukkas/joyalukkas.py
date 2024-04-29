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

# Global variable to track image count
image_counter = 2071

# Define a function to save images
def save_image(src):
    global image_counter
    img_dir = r'D:\Web Scraping\National_jewellery (India)\Img Scraping\joyalukkas'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    response = requests.get(src)
    if response.status_code == 200:
        file_path = os.path.join(img_dir, f"image_{image_counter}.jpg")
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"Image {image_counter} saved successfully at: {file_path}")
            image_counter += 1  # Increment the global image counter
    else:
        print(f"Failed to download image {image_counter} from {src}, status code: {response.status_code}")

# Create an instance of Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver with ChromeDriverManager and the options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://www.joyalukkas.in/")
print("This is the image data of joyalukkas ......")
driver.implicitly_wait(3)

# Define a function to perform the search
def search(keyword):
    search_input = driver.find_element(By.XPATH, "/html/body/div/main/header/div[1]/div[3]/div[1]/div/form/div/span/span[1]/input")
    search_input.clear()
    search_input.send_keys(keyword, Keys.ENTER)

# Define a function to scroll and extract image sources
def total_img_item():
    global image_counter  # Use the global image counter
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

# Perform searches and retrieve images
keywords = ["Necklace Sets","Harams","Bangles", "Accessories", "Nose Pins","Solitaire",  "Gifts", "Gold Coins"]

for keyword in keywords:
    search(keyword)
    total_img_item()

# Close the WebDriver session
driver.quit()
