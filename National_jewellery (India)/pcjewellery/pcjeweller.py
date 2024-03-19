import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Create an instance of Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize WebDriver with ChromeDriverManager and the options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.pcjeweller.com/")
print("This is the data of pcjeweller......")
driver.implicitly_wait(3)

# Input "Men" into the search field and submit the search
click_1 = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[1]/div/div[2]/div[1]/div/input").send_keys("Men")
search_1 = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[1]/div/div[2]/div[1]/div/span[2]/input").click()
time.sleep(5)
# Retrieve the total count of men's jewelries displayed on the page
men_jewellary_no = driver.find_element(By.ID, 'productsCount')
text = men_jewellary_no.text
total_count_men = int(text.split()[0])  # Extract the count and convert it to an integer
print("---------------------------------------------------")
print("Total no. of men's Items are : ", total_count_men)
time.sleep(5)

#clear the input field
input_field = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[1]/div/div[2]/div[1]/div/input")
input_field.clear()


# Input "Women" into the search field and submit the search
click_2 = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[1]/div/div[2]/div[1]/div/input").send_keys("WoMen")
search_2 = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[1]/div/div[2]/div[1]/div/span[2]/input").click()
time.sleep(5)
# Retrieve the total count of men's jewelries displayed on the page
women_jewellary_no = driver.find_element(By.ID, 'productsCount')
text = women_jewellary_no.text
total_count_women = int(text.split()[0])  # Extract the count and convert it to an integer
print("---------------------------------------------------")
print("Total no. of Women's Items are : ", total_count_women)
time.sleep(5)

#clear the input field
input_field = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div[1]/div/div[2]/div[1]/div/input")
input_field.clear()
# Navigate back to the original URL
driver.get("https://www.pcjeweller.com/")
time.sleep(5)

# Input "Total jewellery" into the search field and submit the search
Total_jewellery = driver.find_element(By.XPATH, '//a[@href="/all-jewellery.html"]').click()
# Retrieve the total count of men's jewelries displayed on the page
total_jewellary_no = driver.find_element(By.ID, 'productsCount')
text = total_jewellary_no.text
total_count_jewellery= int(text.split()[0])  # Extract the count and convert it to an integer
print("---------------------------------------------------")
print("Total no. of jewelries are : ", total_count_jewellery)
time.sleep(5)


# Input "Total Rings" into the search field and submit the search
Total_Rings = driver.find_element(By.XPATH, '//a[@href="/jewellery/rings.html"]').click()
time.sleep(5)
# Retrieve the total count of men's jewelries displayed on the page
total_Rings_no = driver.find_element(By.ID, 'productsCount')
text = total_Rings_no.text
total_count_Rings= int(text.split()[0])  # Extract the count and convert it to an integer
print("---------------------------------------------------")
print("Total no. of Rings are : ", total_count_Rings)
time.sleep(5)

# Input "Total Earrings" into the search field and submit the search
Total_Earrings = driver.find_element(By.XPATH, '//a[@href="/jewellery/earrings.html"]').click()
time.sleep(5)
# Retrieve the total count of men's jewelries displayed on the page
total_Earrings_no = driver.find_element(By.ID, 'productsCount')
text = total_Earrings_no.text
total_count_Earrings= int(text.split()[0])  # Extract the count and convert it to an integer
print("---------------------------------------------------")
print("Total no. of Earings are : ", total_count_Earrings)
time.sleep(5)


#Total number of Men's Jewellery :

#it is for Men's Jewellery:
web_Men_jewellery= requests.get("https://www.pcjeweller.com/all-jewellery.html?filter=gender:Men~*963")
soup_Men_jewellery= BeautifulSoup(web_Men_jewellery.content, "html.parser")

count_element_Men_jewellery = soup_Men_jewellery.find(id='productsCount')

if count_element_Men_jewellery:
    count_Men_jewellery = count_element_Men_jewellery.get_text()
    print("---------------------------------------------------")
    print("Total Men's Jewellery are : ",count_Men_jewellery)
else:
    print("No element found with ID 'productsCount'.")
time.sleep(5)

#it is for Women's Jewellery:
web_Women_jewellery= requests.get("https://www.pcjeweller.com/all-jewellery.html?filter=gender:Women~*372")
soup_Women_jewellery= BeautifulSoup(web_Women_jewellery.content, "html.parser")

count_element_Women_jewellery = soup_Women_jewellery.find(id='productsCount')

if count_element_Women_jewellery:
    count_Women_jewellery = count_element_Women_jewellery.get_text()
    print("---------------------------------------------------")
    print("Total Women's Jewellery are : ",count_Women_jewellery)
else:
    print("No element found with ID 'productsCount'.")
time.sleep(5)

#total no of men's rings
web_Men_Rings= requests.get("https://www.pcjeweller.com/jewellery/rings.html?filter=gender:Men~*963")
soup_Men_Rings= BeautifulSoup(web_Men_Rings.content, "html.parser")

count_element_Men_Rings = soup_Men_Rings.find(id='productsCount')

if count_element_Men_Rings:
    count_Men_Rings = count_element_Men_Rings.get_text()
    print("---------------------------------------------------")
    print("Total Men's Rings are : ",count_Men_Rings)
else:
    print("No element found with ID 'productsCount'.")
time.sleep(5)

#total no of Women's rings
web_WoMen_Rings= requests.get("https://www.pcjeweller.com/jewellery/rings.html?filter=gender:Women~*372")
soup_WoMen_Rings= BeautifulSoup(web_WoMen_Rings.content, "html.parser")

count_element_WoMen_Rings = soup_WoMen_Rings.find(id='productsCount')

if count_element_WoMen_Rings:
    count_WoMen_Rings = count_element_WoMen_Rings.get_text()
    print("---------------------------------------------------")
    print("Total Women's Rings are : ", count_WoMen_Rings)
else:
    print("No element found with ID 'productsCount'.")
time.sleep(5)


#total no of Women's EARRINGS
web_WoMen_EARRINGS= requests.get("https://www.pcjeweller.com/jewellery/earrings.html?filter=gender:Women~*372")
soup_WoMen_EARRINGS= BeautifulSoup(web_WoMen_EARRINGS.content, "html.parser")

count_element_WoMen_EARRINGS = soup_WoMen_EARRINGS.find(id='productsCount')

if count_element_WoMen_EARRINGS:
    count_WoMen_EARRINGS = count_element_WoMen_EARRINGS.get_text()
    print("---------------------------------------------------")
    print("Total Women's EARRINGS are : ", count_WoMen_EARRINGS)
else:
    print("No element found with ID 'productsCount'.")
time.sleep(5)

#total no of men's silver
web_Men_silver= requests.get("https://www.pcjeweller.com/jewellery/silver.html?filter=gender:Men~*963")
soup_Men_silver= BeautifulSoup(web_Men_silver.content, "html.parser")

count_element_Men_silver = soup_Men_silver.find(id='productsCount')

if count_element_Men_silver:
    count_Men_silver = count_element_Men_silver.get_text()
    print("---------------------------------------------------")
    print("Total men's silver are : ", count_Men_silver)
else:
    print("No element found with ID 'productsCount'.")
time.sleep(5)

#total no of Women's silver
web_WoMen_silver= requests.get("https://www.pcjeweller.com/jewellery/silver.html?filter=gender:Women~*372")
soup_WoMen_silver= BeautifulSoup(web_WoMen_silver.content, "html.parser")

count_element_WoMen_silver = soup_WoMen_silver.find(id='productsCount')

if count_element_WoMen_silver:
    count_WoMen_silver = count_element_WoMen_silver.get_text()
    print("---------------------------------------------------")
    print("Total Women's silver are : ", count_WoMen_silver)
else:
    print("No element found with ID 'productsCount'.")
time.sleep(5)

# Data to be written to the CSV file
data = [
    ["Category", "Total Count"],
    ["Men's Items", total_count_men],
    ["Women's Items", total_count_women],
    ["Total Jewellery", total_count_jewellery],
    ["Total Rings", total_count_Rings],
    ["Total Earrings", total_count_Earrings],
    ["Men's Jewellery", count_Men_jewellery],
    ["Women's Jewellery", count_Women_jewellery],
    ["Men's Rings", count_Men_Rings],
    ["Women's Rings", count_WoMen_Rings],
    ["Women's Earrings", count_WoMen_EARRINGS],
    ["Men's Silver", count_Men_silver],
    ["Women's Silver", count_WoMen_silver]
]

# Preferred location for saving the CSV file
csv_file_location = "D:\\pcjewellery\\pcjeweller_data.csv"   #you can change your path location

# Writing data to the CSV file
with open(csv_file_location, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data saved to", csv_file_location)


driver.quit()  # Quit the WebDriver session
