from appium import webdriver

desired_cap = {
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "appPackage": "com.champion.mpay",
    "appWaitActivity": "com.champion.mpay.Splash_Activity",
    "app": "D:\\Appium\\MasterPayPro.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
