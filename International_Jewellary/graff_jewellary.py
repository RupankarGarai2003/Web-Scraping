import pandas as pd
from selenium import webdriver
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
driver.get("https://www.graff.com/international-en/")#https://www.graff.com/international-en/jewellery-collections/view-by-category/mens-jewellery/
print("This is the data of graff ...... ")
driver.implicitly_wait(3)
time.sleep(2)


driver.get("https://www.graff.com/international-en/jewellery-collections/view-by-category/mens-jewellery/")
men_jewellary_no=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/span')
Total_men_jewellary=list(men_jewellary_no.text)
# parts = Total_men_jewellary.split()  # Split the string by whitespace
Total_men_jewellary = Total_men_jewellary[0:2]
Total_men_jewellary=''.join(Total_men_jewellary)
print("---------------------------------------------------")
print("Total no. of men's jewellaries are",Total_men_jewellary)
driver.implicitly_wait(3)


click_1=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/span[1]").click()
time.sleep(3)
click_2=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/ul/li[1]/div/label/span[2]").click()
time.sleep(3)
men_ring=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/span')
Men_rings=list(men_ring.text)
Men_rings = Men_rings[0:2]
Men_rings=''.join(Men_rings)
print("---------------------------------------------------")
print("Total no. of Men's Rings are",Men_rings)
driver.implicitly_wait(3)
time.sleep(2)

click_3=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[4]/div[2]/span").click()
time.sleep(2)
click_to_category=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/span[1]").click()
time.sleep(2)
click_to_bracelet=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/ul/li[2]/div/label/span[2]").click()
time.sleep(2)
men_bracelet=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/span')
Total_no_of_men_bracelet=list(men_bracelet.text)
Total_no_of_men_bracelet = Total_no_of_men_bracelet[0:2]
Total_no_of_men_bracelet=''.join(Total_no_of_men_bracelet)
print("---------------------------------------------------")
print("Total no. of Men's bracelets are",Total_no_of_men_bracelet)
driver.implicitly_wait(3)
time.sleep(2)

click_to_clear=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[4]/div[2]/span").click()
time.sleep(3)
click_to_category=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/span[1]").click()
time.sleep(2)
click_men_necklaces_and_pendants=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/ul/li[3]/div/label/span[2]')
click_men_necklaces_and_pendants.click()
time.sleep(4)
men_necklaces_and_pendants=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/span')
men_necklaces_and_pendants=list(men_necklaces_and_pendants.text)
men_necklaces_and_pendants = men_necklaces_and_pendants[0:2]
men_necklaces_and_pendants=''.join(men_necklaces_and_pendants)
print("---------------------------------------------------")
print("Total no. of Men's necklaces and pendants are",men_necklaces_and_pendants)
driver.implicitly_wait(3)
time.sleep(2)

driver.refresh()
time.sleep(7)
click_to_clear=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[4]/div[2]/span").click()
time.sleep(2)
click_to_category=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/span[1]").click()
time.sleep(2)
click_men_cufflinks=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[4]/div/ul/li[4]/div/label/span[2]')
click_men_cufflinks.click()
time.sleep(2)

men_cufflinks=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/span')
men_cufflinks=list(men_cufflinks.text)
men_cufflinks = men_cufflinks[0:2]
men_cufflinks=''.join(men_cufflinks)
print("---------------------------------------------------")
print("Total no. of Men's necklaces and pendants are",men_cufflinks)
print("---------------------------------------------------")
driver.implicitly_wait(3)
time.sleep(2)
# driver.quit()



print("\n \n This is the data of the Women jewellary of GRAFF......")
driver.refresh()
driver.get("https://www.graff.com/international-en/jewellery-collections/view-by-collection/?cgid=jewellerycollections_viewbycollection")
click_to_category=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/span[1]").click()
time.sleep(2)

Total_Women_Jewellary=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/span")
Total_Women_Jewellary=list(Total_Women_Jewellary.text)
Total_Women_Jewellary = Total_Women_Jewellary[0:3]
Total_Women_Jewellary=''.join(Total_Women_Jewellary)
print("---------------------------------------------------")
print("Total no. of Women's rings are",Total_Women_Jewellary)
driver.implicitly_wait(3)
time.sleep(2)


click_women_rings=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/ul/li[1]/div/label/span[2]')
click_women_rings.click()
time.sleep(7)

women_rings=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/span")
women_rings=list(women_rings.text)
women_rings = women_rings[0:3]
women_rings=''.join(women_rings)
print("---------------------------------------------------")
print("Total no. of Women's rings are",women_rings)
driver.implicitly_wait(3)
time.sleep(2)

driver.refresh()
time.sleep(7)


click_to_clear_2=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[4]/div[2]/span")
click_to_clear_2.click()
time.sleep(6)
driver.implicitly_wait(6)
click_to_category=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/span[1]").click()
time.sleep(2)
click_women_rings=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/ul/li[2]/div/label/span[2]')
driver.implicitly_wait(6)
click_women_rings.click()
time.sleep(7)


women_earrings=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/span")
women_earrings=list(women_earrings.text)
women_earrings = women_earrings[0:3]
women_earrings=''.join(women_earrings)
print("---------------------------------------------------")
print("Total no. of Women's earrings are",women_earrings)
driver.implicitly_wait(3)
time.sleep(2)

click_to_clear_2=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[4]/div[2]/span")
click_to_clear_2.click()
time.sleep(3)
click_to_category=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/span[1]").click()
time.sleep(2)
click_women_bracelets=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/ul/li[4]/div/label/span[2]')
click_women_bracelets.click()
time.sleep(7)

women_bracelets=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/span")
women_bracelets=list(women_bracelets.text)
women_bracelets = women_bracelets[0:3]
women_bracelets=''.join(women_bracelets)
print("---------------------------------------------------")
print("Total no. of Women's bracelets are",women_bracelets)
driver.implicitly_wait(3)
time.sleep(2)

click_to_clear_2=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[4]/div[2]/span")
click_to_clear_2.click()
time.sleep(3)
click_to_category=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/span[1]").click()
time.sleep(2)
click_women_necklaces_and_pendants=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/ul/li[5]/div/label/span[2]')
click_women_necklaces_and_pendants.click()
time.sleep(7)

women_necklaces_and_pendants=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/span")
women_necklaces_and_pendants=list(women_necklaces_and_pendants.text)
women_necklaces_and_pendants = women_necklaces_and_pendants[0:3]
women_necklaces_and_pendants=''.join(women_necklaces_and_pendants)
print("---------------------------------------------------")
print("Total no. of Women's necklaces and pendats are",women_necklaces_and_pendants)
driver.implicitly_wait(3)
time.sleep(2)


click_to_clear_2=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[4]/div[2]/span")
click_to_clear_2.click()
time.sleep(3)
click_to_category=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/span[1]").click()
time.sleep(2)
click_women_cufflinks=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[4]/div/ul/li[6]/div/label/span[2]')
click_women_cufflinks.click()
time.sleep(7)

women_cufflinks=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/span")
women_cufflinks=list(women_cufflinks.text)
women_cufflinks = women_cufflinks[0:2]
women_cufflinks=''.join(women_cufflinks)
print("---------------------------------------------------")
print("Total no. of Women's cufflinks are",women_cufflinks)
print("---------------------------------------------------")
driver.implicitly_wait(3)
time.sleep(2)
Total_Men_jewellaries=[]
Total_Rings_for_men=[]
Total_no_of_Men_Bracelets=[]
Necklaces_and_Pendants_for_Men=[]
Men_Cufflinks=[]
Total_no_of_Women_Jewellery=[]
Women_rings=[]
Women_Earrings=[]
Women_Bracelets=[]
Necklaces_and_Pendants_for_Women=[]
Women_Cufflinks=[]

data_records={'Total_Men_jewellaries':[Total_men_jewellary],
              'Total_Rings_for_men':[Men_rings],
              'Total_no_of_Men_Bracelets':[Total_no_of_men_bracelet],
              'Necklaces_and_Pendants_for_Men':[men_necklaces_and_pendants],
              'Men_Cufflinks':[men_cufflinks],
              'Total_no_of_Women_Jewellery':[Total_Women_Jewellary],
              'Women_Rings':[women_rings],
              'Women_Earrings':[women_earrings],
              'Women_Bracelets':[women_bracelets],
              'Necklaces_and_Pendants_for_Women':[women_necklaces_and_pendants],
              'Women_Cufflinks':[women_cufflinks]}
df=pd.DataFrame(data_records)
df.to_csv("GRAFF_data.csv", index=False)

driver.quit()
