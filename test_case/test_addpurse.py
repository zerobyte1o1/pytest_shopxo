from model.addpurse.addpurseComtroller import AddpurseComtroller
import pytest

class Test_Addpurse():

    def test_ap01(self):
        addpursecomtroller=AddpurseComtroller()
        addpursecomtroller.addpurse()