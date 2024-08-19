from typing import Literal, Optional
from pydantic import BaseModel

class ElementConfig(BaseModel):
    id: str
    BY: Literal['id', 'name', 'class name', 'text', 'placeholder', 'xpath'] 
    # like button.div 
    parentSelecter: Optional[str]  = None
    
    
class AutomationConfig(BaseModel):
    url: str
    visibility_identifier: ElementConfig

