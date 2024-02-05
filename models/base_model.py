#!/user/bin/python3
"""

"""
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """

        """
        self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        """

        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["update_at"] = self.updated_at.isoformat()

        return inst_dict
    
    def __str__(self):
        """
        
        """
        class_name = self.__class__.name__
         
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
