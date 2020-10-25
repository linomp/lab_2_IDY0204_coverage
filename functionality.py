import random

class Classtobetested(object):

    def __init__(self,name,surname,email):
        
        self.name = name
        self.surname = surname
        self.email = email
        self.likes = 0
        self.arts = []

    
    def add_pets(self,artname):
        if artname not in self.arts:
            self.arts.append(artname)
    
    def get_artnames(self,artnames):
        return self.arts
    
    def add_likes(self):
        self.likes += 1
    
    def remove_likes(self):
        if self.likes > 0:
            self.likes -= 1
    
    def get_art_by_name(self,artname):
        for art in self.arts:
            if art == artname:
                return art
        return None
    
    