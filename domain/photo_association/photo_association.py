from domain.data_access_layer.db import db


class PhotoAssociation(db.Model):
    __tablename__ = 'photo_association'

    photo_id = db.Column(db.BigInteger, nullable=False, primary_key=True)
    association_id = db.Column(db.BigInteger, db.ForeignKey('associations.id'), primary_key=True)

    association = db.relationship("Association", back_populates='photo_association')

    def __repr__(self):
        return f'<PhotoAssociation photo_id:{self.photo_id!r} association_id:{self.association_id!r}>'