from pydantic import BaseModel

class ConsoleBase(BaseModel):
    name: str

class Console(ConsoleBase):
    id: int

    class Config:
        from_attributes = True

class ConsoleCreate(ConsoleBase):
    pass
