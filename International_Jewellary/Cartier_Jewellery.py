
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
driver.get("https://www.cartier.com/en-in/jewellery/collections/")
print("This is the data of Cartier ...... ")
driver.implicitly_wait(3)
time.sleep(5)
# ----------------------For Tor browser---------------------------------------
            # from selenium import webdriver
            # import time
            # from selenium.webdriver.firefox.options import Options as FirefoxOptions
            # from selenium.webdriver.firefox.service import Service as FirefoxService
            # from webdriver_manager.firefox import GeckoDriverManager
            # from selenium.webdriver.common.by import By
            # from selenium import webdriver

            # # Set the path to the Tor Browser binary
            # tor_binary_path = 'D:\\tor\\Tor Browser\\Browser\\firefox.exe'

            # # Create Tor options
            # tor_options = webdriver.FirefoxOptions()
            # tor_options.binary_location = tor_binary_path
            # tor_options.add_argument('--proxy-server=socks5://127.0.0.1:9150')  # Set Tor proxy

            # # Initialize WebDriver with Tor Browser
            # driver = webdriver.Firefox(options=tor_options)

            # # Navigate to the Cartier website or any other desired URL
            # driver.get("https://www.cartier.com/en-in/jewellery/collections/")
            # print("This is the data of Cartier using Tor Browser...")

            # # Add any other actions you need here
            # driver.implicitly_wait(3)
            # time.sleep(5)

# Close the Tor Browser
# driver.quit()

click_him=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[1]/div/ol/li[2]/a/span[1]").click()
time.sleep(4)
TOtal_men_jewellary=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span")
Total_jewellary_for_men=list(TOtal_men_jewellary.text)
Total_jewellary_for_men = Total_jewellary_for_men[0:2]
Total_jewellary_for_men=''.join(Total_jewellary_for_men)
print("---------------------------------------------------")
print("Total no. of Men's jewellaries are",Total_jewellary_for_men)
driver.implicitly_wait(3)
time.sleep(5)



# click_him=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[1]/div/ol/li[2]/a/span[1]").click()
# time.sleep(2)
click_bracelet=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[1]/a/span[1]').click()
time.sleep(5)
men_bracelet=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span')
Total_no_of_men_bracelet=list(men_bracelet.text)
Total_no_of_men_bracelet = Total_no_of_men_bracelet[0:2]
Total_no_of_men_bracelet=''.join(Total_no_of_men_bracelet)
print("---------------------------------------------------")
print("Total no. of Men's bracelets are",Total_no_of_men_bracelet)
driver.implicitly_wait(3)
time.sleep(5)

click_bracelet=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[1]/a/span[1]').click()
time.sleep(4)
click_more_btn=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[12]/button").click()
time.sleep(3)
click_necklace=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[9]/a/span[1]').click()
men_necklace=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span')
men_necklace=list(men_necklace.text)
men_necklace = men_necklace[0:2]
men_necklace=''.join(men_necklace)
print("---------------------------------------------------")
print("Total no. of Men's necklaces are",men_necklace)
driver.implicitly_wait(3)
time.sleep(2)


click_necklace_r=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div/ol/li[3]/a/span").click()
time.sleep(5)
click_more_btn=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[12]/button").click()
time.sleep(3)
click_ring=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[10]/a/span[1]").click()
time.sleep(5)
men_ring=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span')
Men_rings=list(men_ring.text)
Men_rings = Men_rings[0:3]
Men_rings=''.join(Men_rings)
print("---------------------------------------------------")
print("Total no. of Men's Rings are",Men_rings)
driver.implicitly_wait(3)
time.sleep(5)

click_rings_r=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div/ol/li[3]/a/span").click()
time.sleep(5)
click_more_btn=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[12]/button").click()
time.sleep(3)
click_earrings=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[6]/a/span[1]").click()
time.sleep(5)
men_earring=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span')
men_earring=list(men_earring.text)
men_earring = men_earring[0:2]
men_earring=''.join(men_earring)
print("---------------------------------------------------")
print("Total no. of Men's Earrings are",men_earring)
driver.implicitly_wait(3)
time.sleep(5)


click_to_remove_all=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div/ol/li[1]/button").click()
time.sleep(3)
click_to_her=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[1]/div/ol/li[1]/a/span[1]").click()
time.sleep(3)

Total_women=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span")
Total_women_jewellary=list(Total_women.text)
Total_women_jewellary = Total_women_jewellary[0:5]
Total_women_jewellary=''.join(Total_women_jewellary)
print("---------------------------------------------------")
print("Total no. of Women's jewellaries are are",Total_women_jewellary)
driver.implicitly_wait(3)
time.sleep(2)
# click_to_remove_all=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div/ol/li[1]/button").click()

# time.sleep(3)
driver.refresh()
time.sleep(4)
# click_to_her=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[1]/div/ol/li[1]/a/span[1]").click()
# time.sleep(3)
click_more_btn=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[18]/button").click()
time.sleep(3)
click_bracelet=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[1]/a/span[1]').click()
time.sleep(4)
women_bracelets=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span")
women_bracelets=list(women_bracelets.text)
women_bracelets = women_bracelets[0:3]
women_bracelets=''.join(women_bracelets)
print("---------------------------------------------------")
print("Total no. of Women's bracelets are",women_bracelets)
driver.implicitly_wait(3)
time.sleep(2)

click_to_remove_all=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div/ol/li[1]/button").click()
time.sleep(4)
click_to_her=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[1]/div/ol/li[1]/a/span[1]").click()
time.sleep(5)
click_more_btn=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[18]/button").click()
time.sleep(3)
click_brooches=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[9]/a/span[1]').click()
time.sleep(3)

women_brooches=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span")
women_brooches=list(women_brooches.text)
women_brooches = women_brooches[0:3]
women_brooches=''.join(women_brooches)
print("---------------------------------------------------")
print("Total no. of Women's brooches are",women_brooches)
driver.implicitly_wait(3)
time.sleep(2)


click_to_remove_all=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div/ol/li[1]/button").click()
time.sleep(4)
click_to_her=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[1]/div/ol/li[1]/a/span[1]").click()
time.sleep(5)
click_earrings_women=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[3]/a/span[1]').click()
time.sleep(3)


women_earrings=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span")
women_earrings=list(women_earrings.text)
women_earrings = women_earrings[0:2]
women_earrings=''.join(women_earrings)
print("---------------------------------------------------")
print("Total no. of Women's earrings are",women_earrings)
driver.implicitly_wait(3)
time.sleep(4)


click_to_remove_all=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div/ol/li[1]/button").click()
time.sleep(4)
click_to_her=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[1]/div/ol/li[1]/a/span[1]").click()
time.sleep(5)
click_more_btn=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[18]/button").click()
time.sleep(3)
click_rings_women=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[15]/a/span[1]').click()
time.sleep(4)

driver.refresh()
time.sleep(7)
women_rings=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span")
women_rings=list(women_rings.text)
women_rings = women_rings[0:3]
women_rings=''.join(women_rings)
print("---------------------------------------------------")
print("Total no. of Women's rings are",women_rings)
driver.implicitly_wait(3)
time.sleep(4)

click_to_remove_all=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div/ol/li[1]/button").click()
time.sleep(4)
click_to_her=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[1]/div/ol/li[1]/a/span[1]").click()
time.sleep(5)
click_more_btn=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[18]/button").click()
time.sleep(3)
click_necklaces_women=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[1]/div[2]/div[1]/div/div[3]/div[3]/div[10]/div/ol/li[13]/a/span[1]').click()
time.sleep(4)

women_necklace=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[1]/div[1]/div[3]/span")
women_necklace=list(women_necklace.text)
women_necklace = women_necklace[0:3]
women_necklace=''.join(women_necklace)
print("---------------------------------------------------")
print("Total no. of Women's necklaces are",women_necklace)
driver.implicitly_wait(3)
time.sleep(4)

Total_Men_jewellaries=[]
Total_no_of_Women_Jewellery=[]
Total_Rings_for_men=[]
Total_no_of_Men_Bracelets=[]
Necklaces_and_Pendants_for_Men=[]
Men_Earrings=[]
Women_rings=[]
Women_Bracelets=[]
Necklaces_and_Pendants_for_Women=[]
Women_Brooches=[]
              
data_records={
              'Total_Men_jewellaries':[Total_jewellary_for_men],
              'Total_no_of_Women_Jewellery':[Total_women_jewellary],
              'Total_no_of_Men_Bracelets':[Total_no_of_men_bracelet],
              'Women_Bracelets':[women_bracelets],
              'Total_Rings_for_men':[Men_rings],
              'Women_Rings':[women_rings],
              'Necklaces_and_Pendants_for_Men':[men_necklace],
              'Necklaces_and_Pendants_for_Women':[women_necklace],
              'Men_Earrings':[men_earring],
              'Women_Earrings':[women_earrings],
              'Women_Brooches':[women_brooches]}
df=pd.DataFrame(data_records)
df.to_csv("Cartier.csv", index=False)