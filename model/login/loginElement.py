from model.base import Base

class LoginElement(Base):
    def __init__(self):
        Base.__init__(self,False)

    def get_buttom_login(self):
        return self.driver.find_element_by_xpath("//div[@class='menu-hd']//a[1]")
    def get_input_username(self):
        return self.driver.find_element_by_xpath('//*[@name="accounts"]')
    def get_input_pwd(self):
        return self.driver.find_element_by_xpath('//*[@name="pwd"]')
    def get_button_loginin(self):
        return self.driver.find_element_by_xpath("//form[@class='am-form form-validation']//button")
    def get_a_out(self):
        return self.driver.find_elements_by_link_text('退出')[-1]