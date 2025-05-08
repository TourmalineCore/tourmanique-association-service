from domain.data_access_layer.db import db


class Association(db.Model):
    __tablename__ = 'associations'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(2048), nullable=False)

    photo_association = db.relationship("PhotoAssociation", back_populates='association')

    def __repr__(self):
        return f'<Association {self.id!r} name:{self.name!r}>'