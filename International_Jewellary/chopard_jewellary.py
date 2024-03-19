## Incompleted , Any help would be much appriciated
- Please go through the code once to understand the process before continuing

# -------------------------------------------------------------------------------------------------------------
import pandas as pd
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Create an instance of Options
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
desired_port_number = 9876
driver_service = Service(ChromeDriverManager().install(), port=desired_port_number)
driver = webdriver.Chrome(service=driver_service)
chrome_options.add_argument('ignore-certificate-errors')

# Initialize WebDriver with ChromeDriverManager and the options

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get("https://www.chopard.com/en-intl/jewellery")
print("This is the data of Harrywinston......")
# driver.implicitly_wait(3)

cat_lis=[]
# WebDriverWait(driver,7).until(EC.presence_of_element_located(click_1))
click_1=driver.find_element(By.CLASS_NAME,"filters__start")
click_1.click()
time.sleep(3)
one_time_click=driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
time.sleep(3)
# driver.refresh()
# time.sleep(5)
# one_time_click=driver.find_element(By.ID,"onetrust-accept-btn-handler").click()

driver.find_element(By.CLASS_NAME, 'unisex').click()
cat_lis = driver.find_elements(By.TAG_NAME, "label")
for category in cat_lis:
    print(category.text)
    if category.text == 'Unisex':
        category.click()
        time.sleep(3)
# driver.refresh()
# one_time_click=driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
# cat_lis = driver.find_elements(By.TAG_NAME, "label")
# for category_2 in cat_lis:
#     print(category_2.text)
#     if category_2.text == 'Ring':
#         category_2.click()
# def click_and_clear_based_on_condition(elements, desired_text):
#     for element in elements:
#         print(element.text)
#         if element.text == desired_text:
#             element.click()
#             element = None
#             time.sleep(3)

# # Example usage:
# cat_lis = driver.find_elements(By.TAG_NAME, "label")
# click_and_clear_based_on_condition(cat_lis, "Unisex")
# click_and_clear_based_on_condition(cat_lis, "Ring")









# click_3=driver.find_element(By.XPATH,"/html/body/div[2]/header/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/span/input")
# click_3.click()
# search=driver.find_element(By.XPATH,'/html/body/div[2]/header/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/span/input')
# search.click()
# search.send_keys("men jewellaries")
# search.submit()
# search.submit()
# men_jewellary_no = driver.find_element(By.CLASS_NAME,'grid-page__pagination')
# text = men_jewellary_no.text
# # print(text)
# parts = text.split()  # Split the string by whitespace
# total_count_men = int(parts[-3])  # Extract the third-to-last part and convert it to an integer
# print("---------------------------------------------------")
# print("Total no. of men's jewellaries are",total_count_men)
# driver.implicitly_wait(3)


# click_2=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div/header/div[1]/div[1]/div[2]/button/div")
# click_2.click()
# search_2=driver.find_element(By.ID,'searchInput')
# search_2.click()
# search_2.send_keys("women")
# search_2.submit()
# time.sleep(2)

# women_jewellary_no = driver.find_element(By.CLASS_NAME,'grid-page__found-text')
# text_2 = women_jewellary_no.text
# # print(text_2)
# parts_2 = list(text_2)  # Split the string by whitespace
# total_count_women = parts_2[8:11] 
# total_count_women=''.join(total_count_women)
# print("---------------------------------------------------")
# print("Total no. of women's jewellaries are",total_count_women)
# time.sleep(3)

# click_3=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div/header/div[1]/div[1]/div[2]/button/div")
# click_3.click()
# search_3=driver.find_element(By.ID,'searchInput')
# search_3.click()
# search_3.send_keys("Necklaces & Pendants for men")
# search_3.submit()
# time.sleep(2)

# men_necklaces_pendent = driver.find_element(By.CLASS_NAME,'grid-page__found-text')
# text_3 = men_necklaces_pendent.text
# parts_3 = list(text_3)  # Split the string by whitespace
# men_necklaces_pendent_count = parts_3[8:10] 
# men_necklaces_pendent_count=''.join(men_necklaces_pendent_count)
# print("---------------------------------------------------")
# print("Total no. of Men's necklaces and pendent are",men_necklaces_pendent_count)
# time.sleep(3)

# click_4=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div/header/div[1]/div[1]/div[2]/button/div")
# click_4.click()
# search_4=driver.find_element(By.ID,'searchInput')
# search_4.click()
# search_4.send_keys("Necklaces & Pendants for women")
# search_4.submit()
# time.sleep(3)

# women_necklaces_pendent = driver.find_element(By.CLASS_NAME,'grid-page__found-text')
# text_4 = women_necklaces_pendent.text
# parts_4 = list(text_4)  # Split the string by whitespace
# women_necklaces_pendent_count = parts_4[8:11] 
# women_necklaces_pendent_count=''.join(women_necklaces_pendent_count)
# print("---------------------------------------------------")
# print("Total no. of Women's necklaces and pendent are",women_necklaces_pendent_count)
# time.sleep(3)


# click_5=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div/header/div[1]/div[1]/div[2]/button/div")
# click_5.click()
# search_5=driver.find_element(By.ID,'searchInput')
# search_5.click()
# search_5.send_keys("Men earrings")
# search_5.submit()
# time.sleep(3)

# men_earrings = driver.find_element(By.CLASS_NAME,'grid-page__found-text')
# text_5 = men_earrings.text
# parts_5 = list(text_5)  
# men_earrings = parts_5[8:9] 
# men_earrings=''.join(men_earrings)
# print("---------------------------------------------------")
# print("Total no. of Men's earrings are",men_earrings)
# time.sleep(3)

# click_6=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div/header/div[1]/div[1]/div[2]/button/div")
# click_6.click()
# search_6=driver.find_element(By.ID,'searchInput')
# search_6.click()
# search_6.send_keys("Women earrings")
# search_6.submit()
# time.sleep(3)

# women_earrings = driver.find_element(By.CLASS_NAME,'grid-page__found-text')
# text_6 = women_earrings.text
# parts_6 = list(text_6)  
# women_earrings = parts_6[8:10] 
# women_earrings=''.join(women_earrings)
# print("---------------------------------------------------")
# print("Total no. of Women's earrings are",women_earrings)
# time.sleep(3)

# click_7=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div/header/div[1]/div[1]/div[2]/button/div")
# click_7.click()
# search_7=driver.find_element(By.ID,'searchInput')
# search_7.click()
# search_7.send_keys("Men's rings")
# search_7.submit()
# time.sleep(3)

# men_rings = driver.find_element(By.CLASS_NAME,'grid-page__pagination')
# men_ring_desc=driver.find_element(By.ID,'responsivegrid_hero_banner_copy_cop')
# text_7 = men_rings.text
# men_ring_desc=men_ring_desc.text
# parts_7 = list(text_7)  
# men_rings = parts_7[18:21] 
# men_rings=''.join(men_rings)
# print("---------------------------------------------------")
# print("\n",men_ring_desc,"\n")
# print("Total no. of Men's rings are",men_rings)
# time.sleep(3)

# driver.refresh()
# driver.get("https://www.tiffany.com/")
# click_8=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div/header/div[1]/div[1]/div[2]/button/div")
# click_8.click()
# search_8=driver.find_element(By.ID,'searchInput')
# search_8.click()
# search_8.send_keys("Women's rings")
# search_8.submit()
# time.sleep(3)

# women_rings = driver.find_element(By.CLASS_NAME,'grid-page__pagination')
# text_8 = women_rings.text
# parts_8 = list(text_8)  
# women_rings = parts_8[18:21] 
# women_rings=''.join(women_rings)
# print("---------------------------------------------------")
# print("Total no. of Women's rings are",women_rings)
# print("---------------------------------------------------")
# time.sleep(3)
# Total_Men_jewellaries=[]
# Total_Women_jewellaries=[]
# Necklaces_and_Pendants_for_Men=[]
# Necklaces_and_Pendants_for_Women=[]
# Men_earrings=[]
# Women_earrings=[]
# Men_rings=[]
# Women_rings=[]

# data_records={'Total_Men_jewellaries':[total_count_men],
# 'Total_Women_jewellaries':[total_count_women],
# 'Necklaces_and_Pendants_for_Men':[men_necklaces_pendent_count],
# 'Necklaces_and_Pendants_for_Women':[women_necklaces_pendent_count],
# 'Men_earrings':[men_earrings],
# 'Women_earrings':[women_earrings],
# 'Men_rings':[men_rings],
# 'Women_rings':[women_rings]}
# df=pd.DataFrame(data_records)
# df.to_csv("tiffany_data.csv", index=False)

# driver.quit()
