
from abc import ABC, abstractmethod
from scraplib.automation.selenium_automation import SeleniumAutomation
from scraplib.drivers.constants import EDrivers


class BaseDriver(ABC):    
    def __init__(self, driver_name: EDrivers) -> None:
        self.driver_name = driver_name
        self.automation = SeleniumAutomation()
        
    @abstractmethod
    def authenticate(self):
        pass
    
    
