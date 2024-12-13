from typing import Literal, Optional
from pydantic import BaseModel
from selenium.webdriver.common.by import By

class ElementConfig(BaseModel):
    id: str
    BY: Literal['id', 'name', 'class name', 'text', 'placeholder', 'xpath', 'css selector'] 
    # like button.div 
    parentSelecter: Optional[str]  = None
    
    
class AutomationConfig(BaseModel):
    url: str
    visibility_identifier: ElementConfig

