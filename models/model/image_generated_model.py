from typing import Optional, List
from uuid import uuid4

from pydantic import BaseModel


class ImageGeneratedModel(BaseModel):
    uuid_image_generated: str
    email: Optional[str]
    image_code: List[int]
    url_negative: Optional[str]
    url_positive: Optional[str]

    @classmethod
    def create_model(cls, image_code: list):
        return cls(image_code=image_code, uuid_image_generated=uuid4().hex)
