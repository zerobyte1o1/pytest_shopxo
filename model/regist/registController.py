from model.regist.registOperating import RegistOperating
import time
class RegistController(RegistOperating):
    def __init__(self):
        RegistOperating.__init__(self)
    def regist(self,username,pwd):
        self.click_button_regist()
        self.send_input_username(username)
        self.send_input_pwd(pwd)
        # self.click_box_success()
        self.click_button_registin()
        time.sleep(1)
        asstext=self.test_a_out()
        self.click_a_out()

        return asstext