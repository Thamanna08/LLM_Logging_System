from pydantic import BaseModel

class ChatRequest(BaseModel):

    prompt:str

    provider:str

class LogPayload(BaseModel):

    provider:str

    model:str

    latency:float

    token_usage:int

    status:str