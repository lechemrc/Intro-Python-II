# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room, name, inventory=[]):
        self.room = room
        self.name = name
        self.inventory = inventory

    def movement(self, decision):
        if hasattr(self.room, f'{decision}_to'):
            self.room = getattr(self.room, f'{decision}_to')
            print('\n', self.room)
            return self.room
        else:
            print('\nYou can\'t go that way. Please try another direction.\n')
            return self.room

    def player_inventory(self):
        if len(self.inventory) > 0:
            print(f'You have {[item for item in self.inventory]} in your inventory.\n')
        else:
            return f'You have nothing in your inventory.\n'