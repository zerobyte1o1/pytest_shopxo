from model.base import Base

class RegistElement(Base):
    def __init__(self):
        Base.__init__(self,False)

    def get_buttom_regist(self):
        return self.driver.find_element_by_xpath("//div[@class='menu-hd']//a[2]")


    def get_input_username(self):
        return self.driver.find_element_by_xpath('//*[@name="accounts"]')
    def get_input_pwd(self):
        return self.driver.find_element_by_xpath('//*[@name="pwd"]')
    # def get_box_success(self):
    #     return self.driver.find_element_by_name('is_agree_agreement')
    def get_button_registin(self):
        return self.driver.find_element_by_xpath("//form[@class='am-form form-validation-username']//button[@type='submit']")
    def get_a_out(self):
        return self.driver.find_elements_by_link_text('退出')[-1]