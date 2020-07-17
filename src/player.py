# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player():
    def __init__(self, room, name):
        self.room = room
        self.name = name

    def movement(self, decision):
        if hasattr(self.room, f'{decision}_to'):
            self.room = getattr(self.room, f'{decision}_to')
            print(self.room)
            return self.room
        else:
            print('You can\'t go that way. Please try another direction.')
            print(self.room)
            return self.room