import time
from typing import List, Optional, Set
from scraplib.drivers.base.base_driver import BaseDriver
from scraplib.automation.element_types import ElementConfig, AutomationConfig
from scraplib.drivers.constants import EDrivers

from scraplib.drivers.driver_types import EGender, FriendFilter
from utils.env_utils import getEnv
from utils.execution_utils import safe_execute
from utils.sytem_utils import notify_sound


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
        self.automation.switch_to_parentframe()
    
    def __close_alert_box(self):
        alert_no_button_xpath ="//div[@class='card__actions']/button[div[@class='btn__content' and contains(text(), 'No')]]"
        alert_no_button = ElementConfig(id=alert_no_button_xpath, BY='xpath')
        safe_execute(self.automation.wait_until_element_visibilty, alert_no_button, 10)
        safe_execute(self.automation.click_element,alert_no_button)
        
    def __initiate_random_chat(self):
        goto_chat_button = ElementConfig(id= 'Goto chat', BY='text', parentSelecter='button')
        
        self.automation.wait_until_element_visibilty(goto_chat_button)
        
        self.automation.click_element(goto_chat_button)
        
        
        message_loaded = ElementConfig(id="Messages you receive will show up here", BY="text")
        self.automation.wait_until_element_present(message_loaded)
        
        random_chat_button = ElementConfig(id="New Random Chat", BY="text" )
        random_user = ElementConfig(id="Random User", BY="text" )
        chat_trigger_buttons = [random_chat_button, random_user]
        chat_trigger_button = next((button for button in chat_trigger_buttons if safe_execute(self.automation.get_element_by_config, button)[1]), None)    
        assert chat_trigger_button, "Chat Trigger Button Not found"
        self.automation.click_element(chat_trigger_button)
        
    def __send_random_chat_message(self, message: str):
        input_element_xpath = "//div[@class='private-chat-container']//*[@placeholder='Type a message...']"
        input_element = ElementConfig(id=input_element_xpath,BY="xpath")
        self.automation.wait_until_element_visibilty(input_element, 30)
        self.automation.input_element(input_element, message)
        send_button = ElementConfig(id="private-send-button", BY="class name" )
        self.automation.click_element(send_button)
        
    def __new_random_chat(self):
        new_patner_button = ElementConfig(id="//button[descendant::span[contains(text(), 'New')]]", BY="xpath")
        really_button =  ElementConfig(id="//button[descendant::span[contains(text(), 'Really')]]", BY="xpath")
        
        new_patner_button_ele =  safe_execute(self.automation.get_element_by_config, new_patner_button)[0]
        
        if(new_patner_button_ele):
            self.automation.click_element(new_patner_button)
            
        really_button_ele =  safe_execute(self.automation.get_element_by_config, really_button)[0]
        if(really_button_ele):
            self.automation.click_element(really_button)
     
        self.automation.wait_until_element_visibilty(ElementConfig(id="End", BY="text"))
        
    def __get_chat_messages(self) -> List[str]:
        chat_message_xpath = "//div[contains(@class, 'private-chat-container')]//div[contains(@class, 'message left')]//div[contains(@class, 'text')]/span"
        return self.automation.get_elements_text(ElementConfig(id=chat_message_xpath, BY='xpath'))
        
                
        
    def findFriends(self, filter: Optional[FriendFilter] = None):
        
        self.__initiate_random_chat()
        self.__close_alert_box()
        
        isNewChat = True
        while True:
            if(isNewChat):
                safe_execute(self.__send_random_chat_message, 'M')
        
            isNewChat = safe_execute(self.automation.wait_until_element_visibilty, ElementConfig(id="Chat with another person", BY="text"), 7)[1]
            
            if(not isNewChat):               
                messages = safe_execute(self.__get_chat_messages)[0]
                if(messages and len(messages)>=1 and filter):
                  isNewChat = not any([ self.message_gender_detection(message) == filter.gender for message in messages[0: 5]])
                else: 
                    isNewChat = True
                    
            if(isNewChat):
                safe_execute(self.__new_random_chat)
                time.sleep(0.7)
            else:
                notify_sound()
                input("Press any key yo continue....")
            
        self.automation.wait_until_element_visibilty(ElementConfig(id='asd', BY="id"), 100)
        # self.__new_random_chat()
        
        
        
