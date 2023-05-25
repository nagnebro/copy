from ursina import *

from scene.renscene import RenScene


class Npc(SpriteSheetAnimation):
    def __init__(self, **kwargs):
        super().__init__('Tressa', tileset_size=(6, 5), fps=4, animations={
            'idle_left': ((1, 4), (1, 4)),
            'idle_right': ((0, 4), (0, 4)),

            'walk_down': ((0, 3), (4, 3)),
            'walk_up': ((0, 2), (4, 2)),
            'walk_left': ((0, 1), (4, 1)),
            'walk_right': ((0, 0), (4, 0)),
        })
        self.play_animation('idle_right')
        self.z = -0.5
        self.scale_x = 0.6
        self.rotation_x = -90

        self.conversation = None

        self.cube = Entity(parent=self, model='cube', collider='box', color=color.clear)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        if key == 'e' and self.cube.intersects(self.target):
            self.conversation = RenScene(Empty(
                script=self.script,
                font="NanumSquareRoundR.ttf",
            ))
            
    def update(self):
        self.intersects(self.target)
