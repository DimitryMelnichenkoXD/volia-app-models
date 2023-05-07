import time
from uuid import uuid4

from pydantic import BaseModel


class UserPhraseModel(BaseModel):
    uuid_phrase: str
    email: str
    phrase: str
    image_generated_id: int
    number_of_views: int
    created: float

    @classmethod
    def create_model(cls, email: str, phrase: str, image_generated_id: int):
        return cls(
            email=email,
            phrase=phrase,
            uuid_phrase=uuid4().hex,
            image_generated_id=image_generated_id,
            number_of_views=0,
            created=time.time()
        )

    @classmethod
    def create_user(cls, data, image_generated):
        return cls.create_model(
            email=data.email,
            phrase=data.phrase,
            image_generated_id=image_generated.id
        )
