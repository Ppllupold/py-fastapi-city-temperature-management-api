from pydantic import BaseModel


class CityBase(BaseModel):
    name: str
    additional_info: str | None = None


class CityPut(BaseModel):
    pass


class CityCreate(CityBase):
    pass


class CityRead(CityBase):
    id: int

    class Config:
        from_attributes = True
