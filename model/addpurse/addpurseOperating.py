from model.addpurse.addpurseElement import AddpurseElement

class AddpurseOperating(AddpurseElement):
    def __init__(self):
        AddpurseElement.__init__(self)
    def click_div_purse(self):
        self.get_div_purse().click()
    def click_button_purse(self):
        self.get_button_purse().click()
    def click_a_shopcar(self):
        self.get_a_shopcar().click()