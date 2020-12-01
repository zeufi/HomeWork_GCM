from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd


class Page1:

    alertcookie_xpath = "//*[@id='app']/div/header/div/div[2]/div/button/svg/g/path"
    alertcovid19_xpath = "//*[@id='app']/div/main/div/div[1]/div/svg/g/circle"
    alertcookie_class = "closeBtn____-0Mx plain___3Dl0A"
    alertcovid19_class = "close___2mjSj"
    immatricolazione_id = "firstRegistrationFilter"
    imma_da_xpath = "/html/body/div[1]/div/main/div/div[2]/div/div[3]/div/div/div/div[1]/select"
    imma_a_xpath = "/html/body/div[1]/div/main/div/div[2]/div/div[3]/div/div/div/div[3]/select"

    chilometraggio_id = "kilometersFilter"
    chilo_da_xpath = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[4]/div/div/div/div[1]/select"
    chilo_a_xpath = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[4]/div/div/div/div[3]/select"

    ricercavanzata_id = "advancedFilter"
    applicafiltri_xpath = "/html/body/div[1]/div/main/div/div[2]/div[1]/div[5]/div/div/button"

    annuncipiurecenti_xpath = "/html/body/div[1]/div/main/div/div[2]/div[1]/select"

    container_class = "link___2Maxt linkVisible___1nyfU color-inherit___SyKXO decoration-none___1IENu"
    infoscontainer_xpath = "infoContainer___1OcRd"
    title_xpath = ".//*[@class='title___uRijL adTitle___1MVoL']"
    price_xpath = ".//*[@class='title___uRijL price___1A8DG']"
    when_xpath = ".//*[@class='specItem___2gMHn']"

    def __init__(self, driver):
        self.driver = driver

    def closealert1(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.alertcookie_xpath))).click()
        # self.driver.switch_to.alert.dismiss()
        # self.driver.alert.close()
        # self.driver.find_element(By.CLASS_NAME, self.alertcookie_class).click()
    #
    # def closealert2(self):
    #     # self.driver.find_element(By.CLASS_NAME, self.alertcovid19_class).click()

    def clickimmatri(self):
        self.driver.find_element_by_id(self.immatricolazione_id).click()

    def clickchilo(self):
        self.driver.find_element_by_id(self.chilometraggio_id).click()

    def clickricercavanzata(self):
        self.driver.find_element_by_id(self.ricercavanzata_id).click()

    def clickapplicafitri(self):
        self.driver.find_element(By.XPATH, self.applicafiltri_xpath).click()

    def immadropdown_da(self):
        # self.driver.find_element_by_class_name(self.containerimmatri_class).click()
        element = self.driver.find_element(By.XPATH, self.imma_da_xpath)
        # print('I', len(Select(element).options))
        # for option in Select(element).options:
        #     print(option.text)
        Select(element).select_by_visible_text(text='2015')

    def immadropdown_a(self):
        element = self.driver.find_element(By.XPATH, self.imma_a_xpath)
        # print(len(Select(element).options))
        Select(element).select_by_visible_text(text='2020')

    def chilodropdown_da(self):
        # self.driver.find_element_by_class_name(self.containerimmatri_class).click()
        element = self.driver.find_element(By.XPATH, self.chilo_da_xpath)
        # print(len(Select(element).options))
        # for option in Select(element).options:
        #     print(option.text)
        Select(element).select_by_index(index='0')

    def chilodropdown_a(self):
        element = self.driver.find_element(By.XPATH, self.chilo_a_xpath)
        # print(len(Select(element).options))
        Select(element).select_by_index(index='1')

    def annucipiurecenti(self):
        element = self.driver.find_element(By.XPATH, self.annuncipiurecenti_xpath)
        # print(len(Select(element).options))
        Select(element).select_by_visible_text(text='Prezzo più alto')

    def imagecars(self):
        # page = self.driver.find_element_by_tag_name('html')
        # page.send_keys(Keys.END)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        cars = self.driver.find_elements(By.CLASS_NAME, self.infoscontainer_xpath)
        car_list = []
        # for scrol in page:
        #     scrol.execute_script("window.scrollTo(0,100)")
        #     time.sleep(3)
        for car in cars:
            title = car.find_element(By.XPATH, self.title_xpath).text
            price = car.find_element(By.XPATH, self.price_xpath).text
            when = car.find_element(By.XPATH, self.when_xpath).text
            # print(title, price, when)
            if int(when) > 2015:
                print(title, '-> Immatricolata dopo il 2015')
            else:
                self.driver.get_screenshot_as_file(r"C:\Users\jojo\Desktop\Test_Tecnico_GCM\Reports\primadel2015.jpg")
                print(title, ' immatricolata prima del 2015')
            car_item = {
                'Title': title,
                'Price': price,
                'When': when
            }
            car_list.append(car_item)
        df = pd.DataFrame(car_list)
        print(df)
