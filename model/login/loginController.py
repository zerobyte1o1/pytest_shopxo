from model.login.loginOperating import LoginOperating
import time
class LoginController(LoginOperating):
    def __init__(self):
        LoginOperating.__init__(self)
    def login(self,username,pwd):
        self.click_button_login()
        self.send_input_username(username)
        self.send_input_pwd(pwd)
        self.click_button_loginin()
        time.sleep(1)
        asstext=self.test_a_out()
        self.click_a_out()

        return asstext

if __name__ == '__main__':
    LoginController().login('liufangjing','199921Liu')