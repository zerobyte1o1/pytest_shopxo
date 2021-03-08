from model.base import Base

class UpprofileElement(Base):
    def __init__(self):
        Base.__init__(self)
    def get_div_user(self):
        return self.driver.find_element_by_xpath('//div[@class="navigation-user "]')
    def get_a_uppro(self):
        return  self.driver.find_element_by_xpath('//div[@class="items"]/a[1]')
    def get_input_uppro(self):
        return self.driver.find_element_by_xpath('//input[@name="file"]')
    def get_button_uppro(self):
        return self.driver.find_element_by_xpath('//form/button[@type="submit"]')