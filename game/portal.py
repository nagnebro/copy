from ursina import *


class Portal(Entity):
    def __init__(self, **kwargs):
        super().__init__(model='cube', collider='box', origin=(-.5, -.5, .5), scale=1, **kwargs)
        self.next_index = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    def set_next_chapter(self, next_index):
        self.next_index = next_index
