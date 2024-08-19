from collections import namedtuple
from typing import Callable, List

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
        self.wait_until_element_visibilty(config.visibility_identifier)


    def wait_until_element_visibilty(self, element_config: ElementConfig, timeout = 20):
        selecter = self.__getElementSelecter(element_config)
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((selecter.selecter, selecter.value))
        )
    
    
    def wait_until_condition(self, check: Callable[[], bool], timeout = 20):
        WebDriverWait(self.driver, timeout).until(lambda driver: check)
        pass
        
    
    def wait_until_element_present(self,  element_config: ElementConfig):
        selecter = self.__getElementSelecter(element_config)
        WebDriverWait(self.driver, 100).until(
        EC.presence_of_element_located((selecter.selecter, selecter.value)))
        
    

    def __construct_xpath(self,  element_config: ElementConfig):
        def add_xpath_prefix(prefix: str, xpath: str):
            return f"//{prefix}[{xpath}]"
        
        xpath = ""
        if element_config.BY == 'text':
            xpath = f"//*[contains(text(),'{element_config.id}')]"
        elif element_config.BY == 'placeholder':
            xpath = f"//*[@placeholder='{element_config.id}']"
        if(element_config.parentSelecter):
            for prefix in element_config.parentSelecter.split('.')[::-1]:
                xpath = add_xpath_prefix(prefix, xpath)
        
        return xpath
        
    def __getElementSelecter(self, element_config: ElementConfig):
        selecter_config = namedtuple('selecter_config', ["value", "selecter"])
        
        
        if element_config.BY  in ["text", "placeholder"]:
           xpath = self.__construct_xpath(element_config)
           return selecter_config(value=xpath, selecter=By.XPATH)
        else:
            return selecter_config(value=element_config.id, selecter=element_config.BY)
        
        
    def get_element_by_config(self, element_config: ElementConfig) -> WebElement:
        selecter = self.__getElementSelecter(element_config)
        
        elem = self.driver.find_element(selecter.selecter, selecter.value)
        return elem
    
    def input_element(self, element_config: ElementConfig, text: str):
        elem = self.get_element_by_config(element_config)
        print('elem: ', elem.is_displayed(), elem.is_enabled(), elem.get_dom_attribute("class"))
        elem.send_keys(text)
        elem.send_keys(Keys.RETURN)
        
    def click_element(self, element_config: ElementConfig):
        elem = self.get_element_by_config(element_config)
        print('elem: ', elem.is_displayed(), elem.is_enabled(), elem.get_dom_attribute("class"))
        elem.click() 


    def switch_to_iframe(self, element_config: ElementConfig):
        iframe = self.get_element_by_config(element_config)
        self.driver.switch_to.frame(iframe)
        
    def switch_to_parentframe(self):
        self.driver.switch_to.parent_frame()
        
    def get_elements_text(self, element_config: ElementConfig)-> List[str]:
        selecter = self.__getElementSelecter(element_config)
        matching_elements = self.driver.find_elements(selecter.selecter, selecter.value)
        return list(map(lambda ele: ele.text, matching_elements))