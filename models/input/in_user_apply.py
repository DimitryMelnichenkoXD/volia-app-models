import re
from typing import Optional

from flask import abort
from pydantic import BaseModel, validator


class InUserApply(BaseModel):
    email: str
    phrase: str
    captcha: Optional[str]

    @validator("email")
    def validate_email(cls, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise abort(400, 'email check failed')
        return email

    @validator("phrase")
    def validate_phrase(cls, phrase):
        pattern = r"^[А-ЯҐЄІЇа-яґєіїa-zA-ZäöüÄÖÜß0-9\s'!?,.\-:]*$"
        phrase = phrase.strip()
        if len(phrase) > 88:
            raise abort(400, 'phrase check failed: too long')
        if len(re.findall(pattern, phrase)) == 0:
            raise abort(400, 'phrase check failed: wrong symbols')
        return phrase
