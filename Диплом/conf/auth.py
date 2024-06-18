import ast

from pages.base import BasePage
from pages.locators import *
import time, os


class RegPage(BasePage):
def __init__(self, driver, timeout=10):
super().__init__(driver, timeout)
self.first_name = driver.find_element(*RegLocators.REG_FIRSTNAME)
self.last_name = driver.find_element(*RegLocators.REG_LASTNAME)
self.email = driver.find_element(*RegLocators.REG_ADDRESS)
self.password = driver.find_element(*RegLocators.REG_PASSWORD)
self.pass_conf = driver.find_element(*RegLocators.REG_PASS_CONFIRM)
self.btn = driver.find_element(*RegLocators.REG_REGISTER)

def enter_firstname(self, value):
self.first_name.send_keys(value)

def enter_lastname(self, value):
self.last_name.send_keys(value)

def enter_email(self, value):
self.email.send_keys(value)

def enter_password(self, value):
self.password.send_keys(value)

def enter_pass_conf(self, value):
self.pass_conf.send_keys(value)

def btn_click(self):
self.btn.click()


class AuthPage(BasePage):
def __init__(self, driver, timeout=10):
super().__init__(driver, timeout)
url = os.getenv('MAIN_URL') or 'https://b2c.passport.rt.ru'
driver.get(url)
self.username = driver.find_element(*AuthLocators.AUTH_USERNAME)
self.password = driver.find_element(*AuthLocators.AUTH_PASS)
self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
self.reg_in = driver.find_element(*AuthLocators.AUTH_REG_IN)
self.active_tab = driver.find_element(*AuthLocators.AUTH_ACTIVE_TAB)

def enter_username(self, value):
self.username.send_keys(value)

def enter_password(self, value):
self.password.send_keys(value)

def btn_click_enter(self):
self.btn.click()
time.sleep(10)

def enter_reg_page(self):
self.reg_in.click()
time.sleep(10)

def active_tab(self):
self.active_tab()

def check_color(self, elem):
rgba = elem.value_of_css_property('color')
r, g, b, alpha = ast.literal_eval(rgba.strip('rgba'))
hex_value = '#%02x%02x%02x' % (r, g, b)
return hex_value


class NewPassPage(BasePage):
def __init__(self, driver, timeout=10):
super().__init__(driver, timeout)
url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'
driver.get(url)
self.username = driver.find_element(*NewPassLocators.NEWPASS_ADDRESS)
self.btn = driver.find_element(*NewPassLocators.NEWPASS_BTN_CONTINUE)

def enter_username(self, value):
self.username.send_keys(value)

def btn_click_continue(self):
self.btn.click()
time.sleep(10)

