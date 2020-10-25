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

    def test_add_likes(self):

        self.artist.likes = 0
        self.artist.add_likes()
        self.assertEqual(1, self.artist.likes)
    
    def test_remove_likes(self):
        """
        Testing if method remove_likes working properly
        """
        self.artist.likes = 0
        self.artist.remove_likes()
        self.assertEqual(0,self.artist.likes)

        self.artist.likes = 3
        for _ in range(2):
            self.artist.remove_likes()
        self.assertEqual(1,self.artist.likes)

    def test_get_arts_by_names(self):
        """
         Testing method get_arts_by_artname
        """
        self.artist.add_art('art1')
        self.artist.add_art('art2')

        art1 = self.artist.get_art_by_name('art1')
        self.assertEqual(art1,'art1')

        unkown_art = self.artist.get_art_by_name('some art')
        self.assertEqual(unkown_art,None)

    def test_remove_arts(self):
        """
        Testing if method remove_arts removing all arts
        """

        self.artist.arts = []
        self.artist.remove_arts()
        self.assertEqual([],self.artist.arts)


        self.artist.add_art('art1')
        self.artist.add_art('art2')
        self.artist.remove_arts()
        self.assertEqual([],self.artist.arts)

    def test_get_json(self):
        """
        Testing if method get_json gives valid json
        """

        self.artist.add_art('art1')
        self.artist.add_art('art2')
        for _ in range(5):
            self.artist.add_likes()
    

        valid_json_response = {
            'name': self.artist.name,
            'surname': self.artist.surname,
            'likes': self.artist.likes,
            'arts': {
                'artnames': self.artist.arts
            }
        }

        test_json = self.artist.get_json()

        self.assertEqual(test_json,valid_json_response)

    


