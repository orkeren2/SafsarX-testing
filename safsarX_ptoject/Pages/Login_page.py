
from selenium.webdriver.common.by import By

from tests.conftest import driver
from .Basic_Page import BasePage
class LoginPage(BasePage):
    """Class to represent the login page actions"""
    loginPage_baseUrl = 'https://portal-dev.safsarglobal.link/'
    input_sms_locator = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/input')
    loginbutton_locator = (By.XPATH, '/html/body/div/div[1]/div/nav/div[1]/ul/a')
    input_phone_locator = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/input')
    enter_button_locator = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/button')
    confirmbtn_locator = (By.XPATH, '//*[@id="root"]/main/div/div[2]/div/form/button')



    # def enter_username(self,username):
    #     """Enter the username in the username field"""
    #     self.enter_text(self.USERNAME_FIELD,username)
    # def enter_password(self,password):
    #     self.enter_text(self.PASSWORD_FIELD,password)
    #     """enters password in password field"""
    # def click_login (self):
    #     self.click_element(self.LOGIN_BUTTON)