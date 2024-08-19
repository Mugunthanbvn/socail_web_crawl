
from abc import ABC, abstractmethod
import re
from typing import Optional
from scraplib.automation.selenium_automation import SeleniumAutomation
from scraplib.drivers.constants import EDrivers
from scraplib.drivers.driver_types import EGender, FriendFilter


class BaseDriver(ABC):    
    def __init__(self, driver_name: EDrivers) -> None:
        self.driver_name = driver_name
        self.automation = SeleniumAutomation()
        
    def message_gender_detection(self, message: str):
        male_geneder_keys = set(["m", "boy", "man"])
        female_gender_keys = set(["f", "girl", "female"])
        
        message_keys = {re.sub(r'[^a-zA-Z]', '', key.lower()) for key in message.split(" ")}
        if(len(message_keys.intersection(male_geneder_keys))):
            return EGender.male
        if(len(message_keys.intersection(female_gender_keys))):
            return EGender.female
        
        return
    @abstractmethod
    def authenticate(self):
        pass
    
    @abstractmethod
    def findFriends(self, filter: Optional[FriendFilter] = None):
        pass
    
    
