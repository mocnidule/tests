from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


instance = None


def initialize():
    global instance
    profile = webdriver.FirefoxProfile()
    profile.set_preference('intl.accept_languages', 'en-US, en')
    options = Options()
    options.headless = True
    instance = webdriver.Firefox(options=options, firefox_profile=profile, executable_path=GeckoDriverManager().install())
    instance.implicitly_wait(2)
    # instance.install_addon(r'/Users/dusankovacevic/Desktop/streamflow-web-tests/driver/solflare_wallet-1.40.3.xpi')
    instance.install_addon(r'/test_env/driver/solflare_wallet-1.40.3.xpi')
    # instance.install_addon(r'/Users/dusankovacevic/Desktop/streamflow-web-tests/driver/rise_wallet-1.4.0.xpi')
    instance.install_addon(r'/test_env/driver/rise_wallet-1.4.0.xpi')
    return instance


def quit_driver():
    global instance
    instance.quit()



