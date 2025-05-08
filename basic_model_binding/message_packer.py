import json

from config.model_config import processing_result_event_name


class MessagePacker:
    def __init__(self, model_type):
        self.model_type = model_type

    @staticmethod
    def unpack_the_message_body(message_body):
        message_str = message_body.decode('utf-8')
        message = json.loads(message_str)

        photo_id = message["photo_id"]

        return photo_id

    def pack_the_result_message_body(self, photo_id: int):
        message_body = {
                'photo_id': photo_id,
                'event': processing_result_event_name,
            }

        return message_body
