from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
class base:
    def getDriver(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        return self.driver

    def type(self, element, text):
        self.driver.find_element(By.XPATH, element).send_keys(text)

    def clk(self, element):
        self.driver.find_element(By.XPATH, element).click()

    def option(self, element, data):
        element = self.driver.find_element(By.XPATH, element)
        s = Select(element)
        s.select_by_visible_text(data)

    def option_value(self, element, data):
        element = self.driver.find_element(By.XPATH, element)
        s = Select(element)
        s.select_by_value(data)



