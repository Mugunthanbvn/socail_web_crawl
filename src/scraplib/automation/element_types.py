from typing import Literal
from pydantic import BaseModel

class ElementConfig(BaseModel):
    id: str
    BY: Literal['id', 'name', 'class name', 'text', 'placeholder'] 
    
    
class AutomationConfig(BaseModel):
    url: str
    visibility_identifier: ElementConfig

