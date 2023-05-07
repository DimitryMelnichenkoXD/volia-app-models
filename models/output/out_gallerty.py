from typing import List

from pydantic import BaseModel

from models.supporting.phrase_to_view import PhraseToView


class OutGallery(BaseModel):
    max_pages: int = 0
    gallery: List[PhraseToView] = []

    @classmethod
    def create_model(cls, phrase_gallery, max_pages):
        phrase_gallery = [PhraseToView.create_model(phrase) for phrase in phrase_gallery]
        return cls(max_pages=max_pages, gallery=phrase_gallery)
