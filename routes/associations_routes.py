from flask import Blueprint

from routes.queries.get_associations_query import GetAssociationsQuery

associations_blueprint = Blueprint('results', __name__, url_prefix='/results')


@associations_blueprint.route('/<int:photo_id>', methods=['GET'])
def get_associations_by_photo_id(photo_id):
    associations = GetAssociationsQuery().by_photo_id(photo_id)
    associations_response = [association.name for association in associations]

    return associations_response