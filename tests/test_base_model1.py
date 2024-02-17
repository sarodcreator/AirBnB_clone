#!/usr/bin/pyhton
''' Unittesting BaseModel '''
import os
import unittest
from models.base_model import BaseModel #imports class BaseModel

class TesBaseModel(unittest.TestCase):
    '''Unittest for BaseModel '''
    
    def setUp(self):
        ''' setup for file path'''
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        ''' Tear down for temporary file path '''
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        ''' Test for init '''
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        ''' Test for saving '''
        my_model = BaseModel()  

        initial_update_at = my_model.updated_at

        current_update_at = my_model.save()

        self.assertNotEqual(initial_update_at, current_update_at)

    def test_to_dict(self):
        ''' Test to_dict method '''
        my_model = BaseModel()           

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], 'Base_model')
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isfromat())        
        self.assertEqual(my_model_dict['updated_at'], my_model.created_at.isfromat())

    def  test_str(self):
        ''' Test str '''
        my_model = BaseModel()   

        self.assertTrue(str(my_model).startswitch('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()
