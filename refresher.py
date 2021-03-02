from selenium import webdriver
import time
import sys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install()) # activate chromedriver.exe

while(True):
    driver.get('https://cp.karabuk.edu.tr/'); # URL you want to get
    
    #Username
    kbu_email = sys.argv[1]
    
    #Password
    kbu_password = sys.argv[2]

    element1 = driver.find_element_by_name("Username")
    element1.send_keys(kbu_email)

    element2 = driver.find_element_by_name("Password")
    element2.send_keys(kbu_password)

    login = driver.find_element_by_xpath("//button[@class='btn btn-primary btn-block btn-lg']").click()

    time.sleep(60) # time between login and logout (60secs)

    logout = driver.find_element_by_xpath("//button[@class='btn text-uppercase btn-block  btn-primary'][@type='submit']").click()
