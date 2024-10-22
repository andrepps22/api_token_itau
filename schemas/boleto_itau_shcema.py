from pydantic import BaseModel


class BoletoSchema(BaseModel):
    crt: str
    key: str
    dados:dict
    Authorization: str
    ContentType: str
    xitauapikey: str
    xitauflowID: str
    xitaucorrelationID: str