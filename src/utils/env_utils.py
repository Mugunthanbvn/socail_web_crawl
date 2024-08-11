import os
from dotenv import load_dotenv

load_dotenv()



def getEnv(key: str, prefix: str = ""):
    envKey = f"{prefix}_{key}" if prefix else key
    value =  os.getenv(envKey)
    assert value , f"Env {envKey} is not found"
    return value
    
