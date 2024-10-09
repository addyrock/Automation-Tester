import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.implicitly_wait(10)

# define function for taking screenshot
def take_screenshot(step_name):
    driver.save_screenshot(f"{step_name}.png")

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#NUMBER OF LINKS
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

take_screenshot("1_laptop")
driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys("Laptop")
time.sleep(2)
take_screenshot("2_Click")
driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
time.sleep(1)
take_screenshot("3_Homepage")
driver.find_element(By.XPATH,"//div[@class='item-grid']//div[1]//div[1]//div[2]//div[3]//div[2]//button[1]").click()
take_screenshot("4_view")
driver.find_element(By.XPATH,"//span[@class='cart-label']").click()
take_screenshot("5_Computers")
driver.find_element(By.LINK_TEXT,"Computers").click()
time.sleep(1)
take_screenshot("6_Desktop")
driver.find_element(By.LINK_TEXT,"Desktops").click()
time.sleep(1)
take_screenshot("7_Notebooks")
driver.find_element(By.LINK_TEXT,"Notebooks").click()
time.sleep(1)
take_screenshot("8_Software")
driver.find_element(By.LINK_TEXT,"Software").click()
time.sleep(1)

#Menu of Electronics
take_screenshot("9_Electronics")
driver.find_element(By.LINK_TEXT,"Electronics").click()
time.sleep(1)
take_screenshot("10_Camera & photo")
driver.find_element(By.LINK_TEXT,"Camera & photo").click()
time.sleep(1)
take_screenshot("11_phones")
driver.find_element(By.LINK_TEXT,"Cell phones").click()
time.sleep(1)
take_screenshot("12_Others")
driver.find_element(By.LINK_TEXT,"Others").click()
time.sleep(1)
#driver.find_element(By.LINK_TEXT,"Notebooks").click()
#driver.find_element(By.LINK_TEXT,"Software").click()
#driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Camera & photo']").click()
#driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Cell phones']").click()
#driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Others']").click()

#Menu of Apparel
take_screenshot("13_Apparel")
driver.find_element(By.LINK_TEXT,"Apparel").click()
time.sleep(1)
take_screenshot("14_Shoes")
driver.find_element(By.LINK_TEXT,"Shoes").click()
time.sleep(1)
take_screenshot("15_clothing")
driver.find_element(By.LINK_TEXT,"Clothing").click()
time.sleep(1)
take_screenshot("16_Accessories")
driver.find_element(By.LINK_TEXT,"Accessories").click()
time.sleep(1)
#driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Shoes']").click()
#driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Clothing']").click()
#driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Accessories']").click()

#Remaining Menu
take_screenshot("17_Digital downloads")
driver.find_element(By.LINK_TEXT,"Digital downloads").click()
time.sleep(1)
take_screenshot("18_books")
driver.find_element(By.LINK_TEXT,"Books").click()
time.sleep(1)
take_screenshot("19_jewelry")
driver.find_element(By.LINK_TEXT,"Jewelry").click()
time.sleep(1)
take_screenshot("20_gift")
driver.find_element(By.LINK_TEXT,"Gift Cards").click()
time.sleep(1)
take_screenshot("21_Homepage")
driver.find_element(By.XPATH,"//img[@alt='nopCommerce demo store']").click()

#Register the Form
take_screenshot("22_Register")
driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
time.sleep(1)
take_screenshot("23_Gender")
driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()
time.sleep(1)
take_screenshot("24_Name")
driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Arslan Arif Gorssi")
time.sleep(1)
take_screenshot("25_Father_Name")
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys("Muhammad Arif")
time.sleep(1)
take_screenshot("26_DOB")
driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']").send_keys("17")
time.sleep(1)
take_screenshot("27_Month")
driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']").send_keys("May")
time.sleep(1)
take_screenshot("28_year")
driver.find_element(By.XPATH,"//select[@name='DateOfBirthYear']").send_keys("1993")
time.sleep(1)
take_screenshot("29_Email")
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("addyrock680@gmail.com")
time.sleep(1)
take_screenshot("30_Company")
driver.find_element(By.XPATH,"//input[@id='Company']").send_keys("Punjab Safe cities Authority")
time.sleep(1)
take_screenshot("31_Password")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("A007arslan")
time.sleep(1)
take_screenshot("32_Password")
driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys("A007arslan")
time.sleep(1)
take_screenshot("33_click_register")
driver.find_element(By.XPATH,"//button[@id='register-button']").click()
time.sleep(1)
# driver.find_element(By.XPATH,"//a[@class='ico-logout']").click()
time.sleep(1)
#Login the Page
take_screenshot("34_Login")
driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").click()
time.sleep(1)
take_screenshot("35_EMAIL")
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("Addyrock680@gmail.com")
time.sleep(1)
take_screenshot("36_Passowrd")
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("A007arslan")
time.sleep(1)
take_screenshot("37_login")
driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
time.sleep(1)
take_screenshot("38_logout")
driver.find_element(By.XPATH,"//a[normalize-space()='Log out']").click()
time.sleep(1)

