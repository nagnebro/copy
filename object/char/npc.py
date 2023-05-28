from ursina import *

from ui.scene.renscene import RenScene


class Npc(SpriteSheetAnimation):
    def __init__(self, **kwargs):
        super().__init__('Tressa', tileset_size=(6, 5), fps=4, animations={
            'idle_left': ((1, 4), (1, 4)),
            'idle_right': ((0, 4), (0, 4)),

            'walk_down': ((0, 3), (4, 3)),
            'walk_up': ((0, 2), (4, 2)),
            'walk_left': ((0, 1), (4, 1)),
            'walk_right': ((0, 0), (4, 0)),
        }, **kwargs)
        self.play_animation('idle_right')
        self.z = -0.5
        self.scale_y = 1.5
        self.scale_x = 0.9
        self.rotation_x = -45

        self.conversation = None

        self.obj = Empty(
            script=self.script,
            evil=0,
            font="NanumSquareRoundR.ttf",
        )

        self.cube = Entity(parent=self, model='cube', collider='box', color=color.clear)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def disable(self):
        self.cube.disable()
        super().disable()

    def input(self, key):
        if key == 'e':
            print(self.cube.enabled)
            if self.cube.intersects(self.target):
                print(self.obj.evil)
                self.conversation = RenScene(
                    image=self.image,
                    background=self.background,
                    variables_object=self.obj
                )
