from selenium.webdriver.support.select import Select
import time
from Driver.driver_factory import DriverFactory

class Base():
    def __init__(self,flag=True):
        self.driver=DriverFactory.get_driver('chrome',flag)
        time.sleep(1)
    def get_select_option(self,select,index):
        s1=Select(select)
        s1.select_by_index(index)
