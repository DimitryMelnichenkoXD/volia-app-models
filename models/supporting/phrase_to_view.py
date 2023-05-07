from pydantic import BaseModel


class PhraseToView(BaseModel):
    uuid_phrase: str
    phrase: str
    number_of_views: int
    url_negative: str
    url_positive: str
