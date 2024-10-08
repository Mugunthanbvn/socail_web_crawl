from abc import ABC, abstractmethod
from scraplib.automation.element_types import AutomationConfig, ElementConfig
from typing import Any, List

class WebAutomation(ABC):
    @abstractmethod
    def setup(self, config: AutomationConfig) -> None:
        """Set up the automation framework."""
        pass
    
    @abstractmethod
    def get_element_by_config(self, element_config: ElementConfig) -> Any:
        pass

    @abstractmethod
    def input_element(self, element_config: ElementConfig, text: str):
        pass
    
    @abstractmethod
    def click_element(self, element_config: ElementConfig):
        pass
    
    @abstractmethod
    def switch_to_iframe(self, element_config: ElementConfig):
        pass
    
    @abstractmethod
    def switch_to_parentframe(self):
        pass
    
    @abstractmethod
    def wait_until_element_visibilty(self,  element_config: ElementConfig):
        pass
    
    @abstractmethod
    def wait_until_element_present(self,  element_config: ElementConfig):
        pass

    @abstractmethod
    def get_elements_text(self, element_config: ElementConfig) -> List[str]:
        pass