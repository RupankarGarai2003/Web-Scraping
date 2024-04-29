import os
import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Define a function to save images
def save_image(src):
    global image_counter
    img_dir = r'D:\Web Scraping\National_jewellery (India)\Img Scraping\chennaidiamonds\Imgs'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    response = requests.get(src)
    if response.status_code == 200:
        file_path = os.path.join(img_dir, f"image_{image_counter}.jpg")
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"Image {image_counter} saved successfully at: {file_path}")
            image_counter += 1  # Increment the counter after saving
    else:
        print(f"Failed to download image {image_counter} from {src}, status code: {response.status_code}")

# Create an instance of Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver with ChromeDriverManager and the options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get("https://www.chennaidiamonds.in/")
print("This is the image data of chennaidiamonds ......")
driver.implicitly_wait(3)

# Define a function to perform the search and save images
def search_and_save(keyword):
    search_input = driver.find_element(By.ID, 'input_search-box-input-comp-kboono2z')
    search_input.clear()
    search_input.send_keys(keyword, Keys.ENTER)
    time.sleep(3)  # Wait for the search results to load
    
    total_img_item()

    # Navigate back to the main page
    driver.get("https://www.chennaidiamonds.in/")
    time.sleep(3)  # Wait for the main page to load again

# Define a function to scroll and extract image sources
def total_img_item():
    while True:
        # Find all img elements
        img_elements = driver.find_elements(By.TAG_NAME, 'img')
        for index, img_element in enumerate(img_elements):
            try:
                src = img_element.get_attribute("src")
                if src and ".jpg" in src:
                    save_image(src)  # Only pass the src to save_image function
            except StaleElementReferenceException:
                # If element is stale, continue with the loop
                continue

        # Check if "View More" button exists
        try:
            view_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'View More')]")
            view_more_button.click()
            time.sleep(3)  # Wait for the page to load more images
        except NoSuchElementException:
            # If no "View More" button, check for next page button
            try:
                next_page_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
                next_page_button.click()
                time.sleep(3)  # Wait for the page to load
            except NoSuchElementException:
                # If neither "View More" nor "Next" button exists, break the loop as all images are loaded
                break

# Perform searches and retrieve images
keywords = ["Men", "Women" , "Rings", "Men's Rings", "Women's Rings", "Earring", "Men's Earring", "Women's Earring", "Male's Earring", "Diamond", "Men's Diamond", "Women's Diamond", "Female's Diamond", "Silver", "Men's Silver", "Women's Silver", "Male's Silver", "Necklaces", "Men's Necklaces", "Women's Necklaces", "Male's Necklaces", "Bracelets", "Men's Bracelets", "Women's Bracelets", "Male's Bracelets", "Pendant Sets", "Men's Pendant Sets", "Women's Pendant Sets", "Male's Pendant Sets", "Necklace Sets", "Men's Necklace Sets", "Women's Necklace Sets", "Male's Necklace Sets", "Harams", "Women's Harams","Bangles", "Men's Bangles", "Women's Bangles", "Male's Bangles", "Accessories", "Women's Accessorie", "Nose Pins", "Women's Nose Pins", "Solitaire", "Men's Solitaire", "Women's Solitaire", "Gifts", "Men's Gifts", "Women's Gifts", "Men's Gold Coins", "Women's Gold Coins", "Male's Gold Coins"]

# Initialize the global image counter
image_counter = 1

for keyword in keywords:
    search_and_save(keyword)

# Close the WebDriver session
driver.quit()
