from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

instance = None


def initialize():
    global instance
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    # chrome_options.add_extension('./driver/extentions/Phantom.crx')
    instance = webdriver.Chrome(options=options)
    # instance = webdriver.Remote('http://localhost:4444/wd/hub', DesiredCapabilities.CHROME, options=options)
    instance.implicitly_wait(2)
    return instance


def quit_driver():
    global instance
    instance.quit()



