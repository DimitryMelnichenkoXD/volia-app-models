from enum import Enum


class GalleryFilter(str, Enum):
    BY_POPULARITY = "BY_POPULARITY"
    BY_CREATION = "BY_CREATION"


class BountyType(str, Enum):
    REGULAR = "REGULAR"
    PROGRESSIVE = "PROGRESSIVE"
