#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Initialize any objects or variables needed for testing
        self.obj = BaseModel()

    def tearDown(self):
        # Clean up after each test
        pass

    def test_id_is_string(self):
        self.assertIsInstance(self.obj.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.obj.updated_at
        self.obj.save()
        new_updated_at = self.obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.obj.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_class_name(self):
        obj_dict = self.obj.to_dict()
        self.assertIn('__class__', obj_dict)


if __name__ == '__main__':
    unittest.main()
