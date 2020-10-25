from unittest import TestCase
from functionality import *

class Artistclasstest(TestCase):

    def setUp(self): 
        self.artist = Artist('Testname','Testsurname','test@mail.com')
    

    def test_add_arts(self):
        """
        Testing if art added to artist's arts list 
        """

        self.artist.add_art('test_art_name')
        self.assertEqual('test_art_name',self.artist.arts[-1])
    
    def test_get_artnames(self):
        """
        Testing if method get_artnames gives correct artnames
        """

        self.artist.arts = ["art1","art2","art3"]
        artnames = self.artist.get_artnames()
        self.assertEqual(artnames, self.artist.arts)


    


