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


class Cart(object):

    def __init__(self):
        self.items = {}

    
    def add_item(self, item):
        if item[0] in self.items: 
            itemInfo = self.items[item[0]]
            oldQty = itemInfo[0]
            price = itemInfo[1]
            self.items[item[0]] = (oldQty + item[1], price) 
        else:
            self.items[item[0]] = (item[1], item[2])

    def remove_item(self, itemName, qty):
         if itemName in self.items: 
            itemInfo = self.items[itemName]
            newQty = max(0 , itemInfo[0] - qty)
            price = itemInfo[1]
            self.items[itemName] = (newQty, price) 

    def get_total(self):
        total = 0

        for itemTuple in self.items.values():
            qty = itemTuple[0]
            unit_price = itemTuple[1]
            total = total + (qty * unit_price)

        return total

    def get_items(self):
        return self.items
    
    def get_json(self):
        var_json = {
            'items': self.items,
            'total': self.get_total()
        }
        
        return var_json
