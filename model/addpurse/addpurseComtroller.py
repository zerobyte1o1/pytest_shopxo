from model.addpurse.addpurseOperating import AddpurseOperating
import time

class AddpurseComtroller(AddpurseOperating):
    def __init__(self):
        AddpurseOperating.__init__(self)
    def addpurse(self):
        self.click_div_purse()
        time.sleep(2)
        self.click_button_purse()
        # self.click_a_shopcar()


if __name__ == '__main__':
    AddpurseComtroller().addpurse()