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

        self.intersect_ui = Entity(
            parent=camera.ui,
            model=Quad(radius=.005),
            scale=(.1, .2),
            origin=(-.5, .5),
            position=(.12, .1, 8),
            color=color.white)

        Text("상호작용: E", parent=self.intersect_ui, )
        evidence_text = Text("~로 추궁하기: R", parent=self.intersect_ui)
        self.intersect_ui.disable()

        self.conversation = None
        self.cube = Entity(parent=self, model='plane', collider='box', color=color.clear)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def disable(self):
        self.intersect_ui.disable()
        self.cube.disable()
        super().disable()

    def input(self, key):
        if key == 'e':
            print(self.cube.enabled)
            if self.cube.intersects(self.target):
                print(self.target.data.sample_data)
                self.conversation = RenScene(
                    background=self.background,
                    script=self.script,
                    font="NanumSquareRoundR.ttf",
                    variables_object=self.target.data
                )

    def update(self):
        if self.cube.intersects(self.target):
            if not self.intersect_ui.enabled:
                print('intersect?')
                self.intersect_ui.enable()
        else:
            self.intersect_ui.disable()
