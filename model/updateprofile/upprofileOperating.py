from model.updateprofile.upprofileElement import UpprofileElement

class UpprofileOperating(UpprofileElement):
    def __init__(self):
        UpprofileElement.__init__(self)
    def click_div_user(self):
        self.get_div_user().click()
    def click_a_uppro(self):
        self.get_a_uppro().click()
    def click_input_uppro(self,img):
        self.get_input_uppro().send_keys(f'''{img}''')
    def click_button_uppro(self):
        self.get_button_uppro().click()