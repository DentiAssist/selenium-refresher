from selenium import webdriver
import time
import sys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://cp.karabuk.edu.tr/');
time.sleep(5) # Let the user actually see something!

#Username
kbu_email = sys.argv[1]
#Password
kbu_password = sys.argv[2]

element1 = driver.find_element_by_name("Username")
element1.send_keys(kbu_email)

element2 = driver.find_element_by_name("Password")
element2.send_keys(kbu_password)

login = driver.find_element_by_class_name("btn btn-primary btn-block btn-lg").click()
logout = driver.find_element_by_class_name('btn text-uppercase btn-block btn-primary').click()

# driver.findElement(By.cssSelector("div.column a")).click();

time.sleep(60 * 60) # Let the user actually see something!
driver.refresh()
