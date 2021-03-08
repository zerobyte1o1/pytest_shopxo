from model.updateprofile.upprofileComtroller import UpprofileComtroller
import pytest,os,time

class Test_Upprofile():
    imgpath = os.path.abspath('../../data/01.jpg')
    def test_up01(self,imgpath):
        upprofilecomtroller=UpprofileComtroller()
        upprofilecomtroller.updateprofile(imgpath)