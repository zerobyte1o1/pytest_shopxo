from model.delpurse.delpurseElement import DelpurseElement

class DelpurseOperating(DelpurseElement):
    def __init__(self):
        DelpurseElement.__init__(self)

    def click_div_shopcar(self):
        self.get_div_shopcar().click()
    def click_a_del(self):
        self.get_a_del().click()
    def click_span_alert(self):
        self.get_span_alert().click()