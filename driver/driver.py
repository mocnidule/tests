from selenium import webdriver

instance = None


def initialize():
    global instance
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    instance = webdriver.Chrome(options=options)
    instance.implicitly_wait(2)
    return instance


def quit_driver():
    global instance
    instance.quit()



