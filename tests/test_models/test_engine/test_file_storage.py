#!/usr/python3
"""Unittest for FileStorage class

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        """Test that FileStorage.__init__() takes no arguments."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """Test that FileStorage.__init__() takes one argument."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Test that the attribute __file_path is a private class attribute."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        """Test that the attribute __objects is a private class attribute."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """Test that storage initializes"""
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test that all() returns the FileStorage.__objects attr"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """Test that all() takes one argument."""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """Test that new() adds an object to the FileStorage.__objects attr"""
        bm = BaseModel()
        us = User()
        st = State()
        ct = City()
        pl = Place()
        rv = Review()
        am = Amenity()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(pl)
        models.storage.new(rv)
        models.storage.new(am)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("City." + ct.id, models.storage.all().keys())
        self.assertIn(ct, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())

    def test_new_with_args(self):
        """Test that new() takes one argument."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """Test that new() takes one argument."""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """Test that save() properly saves objects to file.json"""
        bm = BaseModel()
        us = User()
        st = State()
        ct = City()
        pl = Place()
        rv = Review()
        am = Amenity()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(pl)
        models.storage.new(rv)
        models.storage.new(am)
        models.storage.save()
        save_text = ""
        with open("storage.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + ct.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        """Test that save() takes one argument."""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """Test that reload() properly reloads objects from file.json"""
        bm = BaseModel()
        us = User()
        st = State()
        ct = City()
        pl = Place()
        rv = Review()
        am = Amenity()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(pl)
        models.storage.new(rv)
        models.storage.new(am)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("City." + ct.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("Review." + rv.id, objs)
        self.assertIn("Amenity." + am.id, objs)

    # def test_reload_no_file(self):
    #     """Test that reload() does not fail if file does not exist"""
    #     self.assertRaises(FileNotFoundError, models.storage.reload())

    def test_reload_with_arg(self):
        """Test that reload() takes one argument."""
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()