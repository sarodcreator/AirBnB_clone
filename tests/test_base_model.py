#!/usr/bin/python
''' Unittest for base_model module '''

import unittest

class TestBaseModel(unittest.TestCase):
    ''' Unittest for BaseModel '''
    def test_init(self):
        ''' Test for the init module '''
        my_model = BaseModel()
        ''' Test if returns valid value'''
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        ''' Test for updated_at is updated to current datetime '''
        my_model = BaseModel()

        start_updated_at = my_model.updated_at
        current_updated_at = my_model.save()

        self.assertNotEqual(start_updated_at, current_updated_at)

    def test_to_dict(self):
        ''' Test to for to_dict method '''
        my_model = BaseModel()

        my_model_to_dict = my_model.to_dict()

        self.assertIsInstance(my_model_to_dict, dict)

        self.assertEqual(my_model_to_dict["__class__"], 'BaseModel')
        self.assertEqual(my_model_to_dict['id'], my_model.id)
        self.assertEqual(my_model_to_dict['created_at'], my_model.created_at.isoformat())
#        self.assertEqual(my_model_to_dict["updated_at"], my_model.created_at.isoformat())

