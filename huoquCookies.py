from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://192.168.1.202:8108/#/Login")
driver.maximize_window()
shur = driver.find_element_by_css_selector("#app > div > div > div:nth-child(2) > label > input[type=text]")
shur.click()
shur.send_keys("admin")
password= driver.find_element_by_css_selector("#app > div > div > div:nth-child(3) > label > input[type=password]")
password.click()
password.send_keys("admmin")

driver.find_element_by_css_selector("#app > div > div > div.item.verifyCode > img").click()

code= driver.find_element_by_css_selector("#verifyCode")
code.click()
coed11=input("请输入验证码")
code.send_keys(coed11)

driver.find_element_by_css_selector("#app > div > div > button").click()

print(1)