import unittest
from src.archiver.arciv import arc


class TextStatisticsTests(unittest.TestCase):

    def test_arc(self):
        self.assertEqual(arc(), 'Архив содержимого.zip')
