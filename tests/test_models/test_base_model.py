#!/usr/bin/python3
"""Defines unittests for models/base_models.py"""

import unittest
from unittest.mock import patch
from datetime import datetime
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for all methods"""

    @patch('models.storage.new')
    def test_init(self, mock_new):
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        self.assertTrue(mock_new.called)

    @patch('models.storage.save')
    def test_save(self, mock_save):
        base_model = BaseModel()
        updated_at_before_save = base_model.updated_at
        base_model.save()
        self.assertNotEqual(updated_at_before_save, base_model.updated_at)
        self.assertTrue(mock_save.called)

    def test_to_dict(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], base_model.id)
        self.assertEqual(
            base_model_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(
            base_model_dict['updated_at'], base_model.updated_at.isoformat())

    def test_to_dict_with_arg(self):
        bm_obj = BaseModel()
        with self.assertRaises(TypeError):
            bm_obj.to_dict(None)

    def test_save_with_arg(self):
        bm_obj = BaseModel()
        with self.assertRaises(TypeError):
            bm_obj.save(None)

    def test_str(self):
        base_model = BaseModel()
        self.assertEqual(
            str(base_model),
            f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
            )


if __name__ == '__main__':
    unittest.main()
