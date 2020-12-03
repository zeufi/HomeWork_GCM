import pytest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
import sys
import logging
sys.path.append(r'C:/Users/jojo/Desktop/Test_Tecnico_GCM')
from POM.SearchPage import Page1

"""
Class for setup and run my TC on different browser
"""


@pytest.fixture(params=["chrome", "firefox", "opera"], scope='class')
def init__driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Chrome(executable_path=GeckoDriverManager().install())
    if request.param == "opera":
        web_driver = webdriver.Chrome(OperaDriverManager().install())
    request.cls.driver = web_driver
    print('----------SetUp----------------')

    yield
    time.sleep(5)
    print('----------TearDown----------------')
    web_driver.close()
    # self.driver.quit()


"""
Class to run my TC
"""


@pytest.mark.usefixtures("init__driver")
class BaseTest:
    pass


class Test_SearchCars(BaseTest):
    logging.basicConfig(filename=r"CC:\Users\jojo\Desktop\Test_Tecnico_GCM\Logs\log_file.txt",
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%y %I:%M:%S:%p', level=logging.DEBUG)

    baseurl = "https://www.autohero.com/it/search/"

    def test_immatricolazionebtn(self):
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        time.sleep(3)
        assert "Compra ora le migliori auto usate online | Autohero.com" in self.driver.title
        # Closes Alerts
        # Page1(self.driver).closealert1()
        # Page1(self.driver).closealert2()

        # Range of cars registration
        time.sleep(5)
        Page1(self.driver).clickimmatri()
        Page1(self.driver).immadropdown_da()
        Page1(self.driver).immadropdown_a()

        # Range of meage
        time.sleep(5)
        Page1(self.driver).clickchilo()
        Page1(self.driver).chilodropdown_da()
        Page1(self.driver).chilodropdown_a()

        # Apply filter
        time.sleep(5)
        Page1(self.driver).clickricercavanzata()
        Page1(self.driver).clickapplicafitri()
        time.sleep(5)
        Page1(self.driver).annucipiurecenti()

        # Verifications
        time.sleep(5)
        Page1(self.driver).imagecars()
