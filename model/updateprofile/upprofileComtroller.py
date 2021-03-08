from model.updateprofile.upprofileOperating import UpprofileOperating
import os,time

class UpprofileComtroller(UpprofileOperating):
    def __init__(self):
        UpprofileOperating.__init__(self)
    def updateprofile(self,img):
        self.click_div_user()
        self.click_a_uppro()
        self.click_input_uppro(img)
        time.sleep(1)
        self.click_button_uppro()

if __name__ == '__main__':
    imgpath = os.path.abspath('../../../shopxoapi/data/01.jpg')
    print(imgpath)

    UpprofileComtroller().updateprofile(imgpath)