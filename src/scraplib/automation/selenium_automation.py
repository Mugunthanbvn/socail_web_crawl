from collections import namedtuple

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



from scraplib.automation.web_automation import WebAutomation
from scraplib.automation.element_types import AutomationConfig, ElementConfig

class SeleniumAutomation(WebAutomation):
    
    def setup(self, config: AutomationConfig) :
        self.driver = webdriver.Chrome()
        self.driver.get(config.url)
        
        # iframe = self.get_element_by_config(ElementConfig(id="iframe-login", BY='id'))
        # self.driver.switch_to.frame(iframe)
        self.waitUntilElementVisibilty(config.visibility_identifier)


    def waitUntilElementVisibilty(self, element_config: ElementConfig):
        selecter = self.__getElementSelecter(element_config)
        WebDriverWait(self.driver, 100).until(
        EC.visibility_of_element_located((selecter.selecter, selecter.value)))
    
    def __getElementSelecter(self, element_config: ElementConfig):
        selecter_config = namedtuple('selecter_config', ["value", "selecter"])
        
        if element_config.BY == 'text':
            return selecter_config(value=f"//*[contains(text(),'{element_config.id}')]", selecter=By.XPATH)
        elif element_config.BY == 'placeholder':
            return selecter_config(value=f"//input[@placeholder='{element_config.id}']", selecter=By.XPATH)
        else:
            return selecter_config(value=element_config.id, selecter=element_config.BY)
        
        
    def get_element_by_config(self, element_config: ElementConfig) -> WebElement:
        selecter = self.__getElementSelecter(element_config)
        elem = self.driver.find_element(selecter.selecter, selecter.value)
        return elem
    
    def input_element(self, element_config: ElementConfig, text: str):
        elem = self.get_element_by_config(element_config)
        elem.send_keys(text)
        elem.send_keys(Keys.RETURN)
        
    def click_element(self, element_config: ElementConfig):
        elem = self.get_element_by_config(element_config)
        elem.click() 


    def switch_to_iframe(self, element_config: ElementConfig):
        iframe = self.get_element_by_config(element_config)
        self.driver.switch_to.frame(iframe)