import pytest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import sys
import logging
sys.path.append(r'C:/Users/jojo/Desktop/Test_Tecnico_GCM')
from POM.SearchPage import Page1


class TestLogin:

    logging.basicConfig(filename=r"CC:\Users\jojo\Desktop\Test_Tecnico_GCM\Logs\log_file.txt",
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%y %I:%M:%S:%p', level=logging.DEBUG)

    baseurl = "https://www.autohero.com/it/search/"
    driver = webdriver.Chrome(ChromeDriverManager().install())

    @pytest.fixture()
    def setup(self):
        print('----------SetUp----------------')
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        yield
        time.sleep(5)
        print('----------TearDown----------------')
        # self.driver.close()
        # self.driver.quit()

    def test_immatricolazionebtn(self, setup):
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
