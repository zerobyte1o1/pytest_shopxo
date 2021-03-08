from model.login.loginElement import LoginElement

class LoginOperating(LoginElement):
    def __init__(self):
        LoginElement.__init__(self)
    def click_button_login(self):
        self.get_buttom_login().click()
    def send_input_username(self,username):
        self.get_input_username().send_keys(username)
    def send_input_pwd(self,pwd):
        self.get_input_pwd().send_keys(pwd)
    def click_button_loginin(self):
        self.get_button_loginin().click()
    def test_a_out(self):
        return self.get_a_out().text
    def click_a_out(self):
        self.get_a_out().click()