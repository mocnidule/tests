from selenium.webdriver.common.by import By
from driver import driver
from helpers.element_helpers import click
from locators.element_locators import *


def select_solflare_web():
    click(driver.instance, By.XPATH, solflare)