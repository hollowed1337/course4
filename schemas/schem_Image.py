from pydantic import BaseModel

class ImageBase(BaseModel):

    img_url: str

class ImageCreate(ImageBase):
    pass

class Image(ImageBase):

    id: int
    class Config:
        orm_mode = True