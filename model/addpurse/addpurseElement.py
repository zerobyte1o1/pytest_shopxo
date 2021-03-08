from model.base import Base

class AddpurseElement(Base):
    def __init__(self):
        Base.__init__(self)
    def get_div_purse(self):
        return  self.driver.find_element_by_xpath('//div[@class="goods-items"][1]')
    def get_button_purse(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return  self.driver.find_element_by_xpath('//button[@title="加入购物车"]')
    def get_a_shopcar(self):
        return  self.driver.find_elements_by_link_text('购物车')[0]
