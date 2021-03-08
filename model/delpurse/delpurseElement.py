from model.base import Base

class DelpurseElement(Base):
    def __init__(self):
        Base.__init__(self)
    def get_div_shopcar(self):
        return self.driver.find_element_by_xpath('//div[@class="top-nav-items"][4]')
    def get_a_del(self):
        return self.driver.find_element_by_xpath('//*[@class="operation"]/a')
    def get_span_alert(self):
        return self.driver.find_element_by_xpath('//*[@class="am-modal-footer"]/span[2]')