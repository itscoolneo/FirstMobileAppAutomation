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
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap,keep_alive=True)
driver.implicitly_wait(500)
# time.sleep(5)
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/skipBtn").click()
driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
driver.find_element(By.ID,"com.android.permissioncontroller:id/permission_allow_button").click()
# driver.find_element(By.ID,"com.champion.mpay:id/input_email").click()
driver.find_element(By.ID,"com.champion.mpay:id/input_email").send_keys(110001)
driver.find_element(By.ID,"com.champion.mpay:id/input_password").send_keys("nirmal@9033")
# driver.press_keycode(66)
driver.find_element(By.ID,"com.champion.mpay:id/btn_login").click()
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/ivClose").click()
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/layout_mobile_recharge").click()
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/llMobileRecgarge").click()
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/etNumber").send_keys(9318350637)
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/etOperator").click()
driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout").click()
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/etAmount").send_keys(10)
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/btnSubmit").click()
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/btnSubmit").click()
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/etvMPin").send_keys(1234)
driver.find_element(AppiumBy.ID,"com.champion.mpay:id/btnSubmit").click()
status = driver.find_element(AppiumBy.ID,"android:id/message").text
print(status)
if status=="Recharge Request Submitted Successfully.":
    print("Mobile Test Passed...!")
else:
    print("Mobile Test Failed...!")
    driver.find_element(AppiumBy.ID,"android:id/button1").click()
driver.find_element(AppiumBy.ID,"android:id/button1").click()
driver.back()