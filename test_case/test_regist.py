from model.regist import registController
import pytest,time,os
from cof.readfile import readfile




class Test_login:
    purpath = os.path.join('./data/testdata.xlsx')
    data = readfile(purpath, 'regist')
    @pytest.mark.parametrize('name, pwd', data)
    def test_r01(self,name,pwd):
        regist = registController.RegistController()
        assertText =regist.regist(name,pwd)
        assert assertText == '退出'
        time.sleep(2)