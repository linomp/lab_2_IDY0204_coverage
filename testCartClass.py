from unittest import TestCase
from functionality import *

class CartClassTest(TestCase):

    def test_add_item(self):
        """
        Testing if add item to cart works
        """
        cart = Cart()

        item = ('item1', 1, 20)
        item_repeated = ('item1', 1, 20)

        cart.add_item(item)
        
        self.assertTrue(item[0] in cart.get_items())
        self.assertEqual(len(cart.get_items().keys()), 1)
    
    def test_remove_item(self):
        """
        Testing if possible to remove item from cart
        """   
        cart = Cart()

        item = ('item1', 2, 20)

        cart.add_item(item)

        cart.remove_item(item[0], 1)
        
        self.assertTrue(item[0] in cart.get_items())
        
        newQty = cart.get_items()[item[0]][0]
        self.assertEqual(newQty, 1)
            

    def test_total(self):
        """
        Testing if total is calculated correctly
        """      
        cart = Cart()

        item1 = ('item1', 5, 20)
        item2 = ('item2', 1, 30)

        cart.add_item(item1)
        cart.add_item(item1)
        cart.add_item(item2)

        self.assertEqual(cart.get_total(), 230)

    def test_get_json(self):
        """
        Testing if method get_json gives valid json
        """
        cart = Cart()

        item1 = ('item1', 5, 20)
        item2 = ('item2', 1, 30)

        cart.add_item(item1)
        cart.add_item(item2)


        valid_json_response = {
            'items': {'item1': (5, 20), 'item2': (1, 30)},
            'total': 130,
        }
        
        test_json = cart.get_json()

        self.assertEqual(test_json,valid_json_response)

