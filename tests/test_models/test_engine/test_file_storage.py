#!/usr/bin/python3
"""Unit tests for the FileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        self.storage.reload()
        self.storage.save()

    def test_all(self):
        objects = self.storage.all()
        self.assertIsNotNone(objects)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        objects = self.storage.all()
        self.assertIn(new_model, objects.values())

    def test_save(self):
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            data = f.read()
            self.assertTrue(len(data) > 0)

    def test_reload(self):
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        self.assertTrue(len(objects) > 0)


if __name__ == '__main__':
    unittest.main()
