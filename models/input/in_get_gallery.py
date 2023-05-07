from models.base.base_model import BaseConfig
from models.supporting.enums.gallery_filter import GalleryFilter


class InGetGallery(BaseConfig):
    page_size: int = 10
    page: int = 1
    gallery_type: GalleryFilter = GalleryFilter.BY_CREATION.value

    @property
    def order_by_type(self):
        if self.gallery_type == GalleryFilter.BY_CREATION.value:
            return "id"
        return "number_of_views"
