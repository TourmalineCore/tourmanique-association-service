import logging
from config.model_config import model_type

from domain import Association
from domain import PhotoAssociation

from pydantic import BaseModel

from domain.data_access_layer.session import session



class NewPhotoAssociationCommand:
    def __init__(self):
        pass
    
    def create(self, entity: Association, photo_id: int):
        with session() as current_session:
            association_instance = current_session \
                    .query(Association) \
                    .filter_by(name=entity.name)\
                    .first()

            if association_instance:
                association_id = association_instance.id
            else:
                association_instance = Association(name=entity.name)
                current_session.add(association_instance)
                current_session.commit()
                association_id = association_instance.id


            current_session.add(PhotoAssociation(photo_id=photo_id,
                                            association_id=association_id))
            current_session.commit()


class AssociationSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


insert_to_db_commands = {
    'associations-model': NewPhotoAssociationCommand,
}

map_result_to_entity = {
    'associations-model': Association,
}

validate_result_with_schema = {
    'associations-model': AssociationSchema,
}

class AppendResultsCommand:
    @staticmethod
    def execute(result_message):
        print(result_message)
        for result in result_message['result']:
            valid_result = validate_result_with_schema[model_type](**result)
            result_entity = map_result_to_entity[model_type](**valid_result.dict())

            insert_to_db_command = insert_to_db_commands[model_type]
            insert_to_db_command().create(
                result_entity, 
                result_message['photo_id'],
                )


