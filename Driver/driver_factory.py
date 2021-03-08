#单例模式:为了解决测试用例执行的时候打开多个浏览器的问题
from selenium import webdriver
from cof.config import  host_port
import time

class DriverFactory:
    #静态属性
    driver = None

    @classmethod
    def get_driver(cls, browser,flag):
        #静态属性可以通过类名的方式来调用，判断如果driver为None,则还没有打开浏览器，
        if DriverFactory.driver == None:
            if browser == "chrome":
                DriverFactory.driver = webdriver.Chrome()
            DriverFactory.driver.maximize_window()
            DriverFactory.driver.implicitly_wait(20)

            #用户登录
            if flag:
                DriverFactory.login('liufangjing', '199921Liu')
            DriverFactory.driver.get(host_port)
        return DriverFactory.driver

    #用户登录
    @classmethod
    def login(cls, username, password):
        #打开登录首页
        DriverFactory.driver.get(host_port+'index.php?s=/index/user/logininfo.html')

        #输入用户名
        DriverFactory.driver.find_element_by_name('accounts').send_keys(username)
        #输入密码
        DriverFactory.driver.find_element_by_name('pwd').send_keys(password)

        #点击登录按钮
        DriverFactory.driver.find_element_by_xpath("//div[@class='am-form-group am-form-group-refreshing']/button").click()

        DriverFactory.driver.get(host_port)


if __name__ == '__main__':
    DriverFactory.get_driver('chrome')