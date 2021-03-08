from model.login import loginController
import pytest,time




class Test_login:
    @pytest.mark.parametrize('name, pwd', [('liufangjing','199921Liu'),('tiantian','123456')])
    def test_l01(self,name,pwd):
        login = loginController.LoginController()
        assertText =login.login(name,pwd)
        assert assertText == '退出'
        time.sleep(2)