from scraplib.drivers.base.base_driver import BaseDriver
from scraplib.automation.element_types import ElementConfig, AutomationConfig
from scraplib.drivers.constants import EDrivers

from utils.env_utils import getEnv


class Y99Driver(BaseDriver):
    
    def __init__(self) -> None:
        super().__init__(EDrivers.Y99)
        url = getEnv('BASE_URL', self.driver_name.value)
        self.automation.setup(AutomationConfig( url=url, visibility_identifier=ElementConfig(id= 'login-instead', BY='class name')))
    
    def authenticate(self):
        self.automation.click_element(ElementConfig(id= 'login-instead', BY='class name'))
        user_name = getEnv('USER_NAME', self.driver_name.value)
        password = getEnv('PASSWORD', self.driver_name.value)
        self.automation.input_element(ElementConfig(id= 'Your username', BY='placeholder'), user_name)
        self.automation.input_element(ElementConfig(id= 'Your password', BY='placeholder'), password)
        
        self.automation.switch_to_iframe(ElementConfig(id="iframe-login", BY='id'))
        
        self.automation.click_element(ElementConfig(id= 'CONTINUE', BY='text'))
        self.automation.waitUntilElementVisibilty(ElementConfig(id= 'Goto chat', BY='text'))
        self.automation.click_element(ElementConfig(id='Goto chat', BY='text'))
        self.automation.waitUntilElementVisibilty(ElementConfig(id= 'CONTINUEs', BY='text'))
        
        
        
        
        
        
   