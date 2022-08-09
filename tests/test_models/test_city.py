#!/usr/bin/python3
"""
Unit Test for City Class
"""
import unittest
from datetime import datetime
import models
import json

City = models.city.City
BaseModel = models.base_model.BaseModel


class TestCityDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   City Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nCity Class from Models Module\n'
        actual = models.city.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'City class handles all application cities'
        actual = City.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new city'
        actual = City.__init__.__doc__
        self.assertEqual(expected, actual)


class TestCityInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  City Class  .........')
        print('.................................\n\n')

    def setUp(self):
<<<<<<< HEAD
        """initializes new city for testing"""
        self.city = City()

    def test_instantiation(self):
        """... checks if City is properly instantiated"""
        self.assertIsInstance(self.city, City)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.city)
        my_list = ['City', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        self.city = City()
        my_str = str(self.city)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.city.save()
        actual = type(self.city.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.city_json = self.city.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.city_json)
        except Exception:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """... to_json should include class key with value City"""
        self.city_json = self.city.to_json()
        actual = None
        if self.city_json['__class__']:
            actual = self.city_json['__class__']
        expected = 'City'
        self.assertEqual(expected, actual)

    def test_email_attribute(self):
        """... add email attribute"""
        self.city.state_id = 'IL'
        if hasattr(self.city, 'state_id'):
            actual = self.city.state_id
        else:
            actual = ''
        expected = 'IL'
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main
=======
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        o = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
>>>>>>> parent of 73da16d... initial checks
