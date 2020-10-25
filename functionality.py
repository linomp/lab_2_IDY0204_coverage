import random

class Artist(object):

    def __init__(self,name,surname,email):
        
        self.name = name
        self.surname = surname
        self.email = email
        self.likes = 0
        self.arts = []
        self.json = {}

    
    def add_art(self,artname):
        if artname not in self.arts:
            self.arts.append(artname)
    
    def get_artnames(self):
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
    
    def remove_arts(self):
        while self.arts != []:
            self.arts.pop()
    
    def get_json(self):
        var_json = {
            'name': self.name,
            'surname': self.surname,
            'likes': self.likes,
            'arts': {
            }
        }
        
        for key in var_json:
            if key == 'arts':
                var_json[key]['artnames'] = []
                for art in self.arts:
                    var_json[key]['artnames'].append(art)
        
        return var_json
