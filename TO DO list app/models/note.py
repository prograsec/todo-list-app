from pydantic import BaseModel

class Note(BaseModel):
    Title:str
    Discription:str
    Important:bool=None