from model.delpurse.delpurseOperating import DelpurseOperating

class DelpurseComtroller(DelpurseOperating):
    def __init__(self):
        DelpurseOperating.__init__(self)
    def delpurse(self):
        self.click_div_shopcar()
        self.click_a_del()
        self.click_span_alert()



if __name__ == '__main__':
    DelpurseComtroller().delpurse()