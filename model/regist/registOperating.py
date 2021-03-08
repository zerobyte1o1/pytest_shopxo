from selenium.webdriver import ActionChains

from model.regist.registElement import RegistElement

class RegistOperating(RegistElement):
    def __init__(self):
        RegistElement.__init__(self)
    def click_button_regist(self):
        self.get_buttom_regist().click()
    def send_input_username(self,username):
        self.get_input_username().send_keys(username)
    def send_input_pwd(self,pwd):
        self.get_input_pwd().send_keys(pwd)

    # def click_box_success(self):
    #     ActionChains(self.driver).move_to_element(self.get_box_success()).click().perform()
    def click_button_registin(self):
        self.get_button_registin().click()
    def test_a_out(self):
        return self.get_a_out().text
    def click_a_out(self):
        self.get_a_out().click()

















