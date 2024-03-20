#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updates_at']:
                        setattr(self, key, datetime.
                                strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        return string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict: dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                value = value.isoformat()
            obj_dict[key] = value
        obj_dict['__class__'] = type(self).__name__
        return obj_dict
