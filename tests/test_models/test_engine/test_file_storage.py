"""Test cases."""
import unittest
import pep8
from models.engine.file_storage import FileStorage


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def setUpClass(cls):
        """Set up class before start testing."""
        cls.FS1 = FileStorage()
        cls.FS2 = FileStorage()

    def test_docstring(self):
        """tests class and method documentation."""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_FileStorageinit(self):
        """tests for initial state of FileStorage instances."""
        cls = type(self)

        self.assertIsNot(cls.FS1, cls.FS2)
        self.assertIsInstance(cls.FS1, FileStorage)
        self.assertIsInstance(cls.FS2, FileStorage)
