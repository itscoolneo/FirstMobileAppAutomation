import time

from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
desired_cap = {
    "deviceName": "fyordueij7cq7xug",
    "platformName": "Android",
    "appPackage": "com.champion.mpay",
    "appWaitActivity": "com.champion.mpay.Splash_Activity",
    "app": "D:\\Appium\\MasterPayPro.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
time.sleep(5)
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/skipBtn").click()
driver.find_element(By.ID,"com.android.packageinstaller:id/permission_allow_button").click()
driver.find_element(By.ID,"com.android.packageinstaller:id/permission_allow_button").click()
driver.find_element(By.ID,"com.champion.mpay:id/input_email").click()
driver.find_element(By.ID,"com.champion.mpay:id/input_email").send_keys('*****')
driver.find_element(By.ID,"com.champion.mpay:id/input_password").send_keys("*****")
driver.press_keycode(66)
driver.find_element(By.ID,"com.champion.mpay:id/btn_login").click()


'''driver.execute_script('mobile: performEditorAction',{'action':'search'})

common actions includes = go,search,send,next,done,previous'''