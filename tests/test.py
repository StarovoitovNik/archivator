import unittest
from src.archivator.arciv import arc


class TextStatisticsTests(unittest.TestCase):

    def text_arc(self):
        self.assertEqual(arc(), ['Архив данных.zip', 'Данные'])
