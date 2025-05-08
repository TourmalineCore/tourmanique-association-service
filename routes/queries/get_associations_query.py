from domain.data_access_layer.session import session
from domain import PhotoAssociation, Association


class GetAssociationsQuery:
    def __init__(self):
        pass

    def by_photo_id(self, photo_id):
        with session() as current_session:
            return current_session \
                .query(Association) \
                .join(PhotoAssociation) \
                .filter(PhotoAssociation.photo_id == photo_id) \
                .all()

    def by_name(self, association_name):
        with session() as current_session:
            return current_session \
                .query(Association) \
                .filter(Association.name == association_name) \
                .one_or_none()